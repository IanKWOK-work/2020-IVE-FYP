import sys
import gi
from gi.overrides import Gtk

gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import Gst, GObject, GstVideo
GObject.threads_init()
Gst.init(None)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        #creat Simple Window
        container = QWidget(self)
        container.setWindowTitle('Test1')

        #container.connect('destroy', self.quit)
        self.setCentralWidget(container)
        self.winId = container.winId()
        self.resize(480, 320)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        # Create GStreamer pipeline
        self.Video_pipeline()

        # Create bus to get events from GStreamer pipeline
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.enable_sync_message_emission()
        self.bus.connect('message::error', self.on_error)
        self.bus.connect('message::eos', self.on_eos)
        self.bus.connect('sync-message::element', self.on_sync_message)
##############################################################################
#VIDEO Pipeline
#|
#|
#V
##############################################################################
    def Video_pipeline(self):
        self.pipeline = Gst.Pipeline()
        self.tcpsrc = Gst.ElementFactory.make('tcpclientsrc','tcpsrc')
        self.tcpsrc.set_property("host", '192.168.12.1')
        self.tcpsrc.set_property("port", 5000)

        self.gdepay = Gst.ElementFactory.make('gdpdepay', 'gdepay')


        self.rdepay = Gst.ElementFactory.make('rtph264depay', 'rdepay')

        self.avdec = Gst.ElementFactory.make('avdec_h264', 'avdec')

        self.vidconvert = Gst.ElementFactory.make('videoconvert', 'vidconvert')

        self.asink = Gst.ElementFactory.make('autovideosink', 'asink')
        self.asink.set_property('sync', False)
        #self.asink.set_property('emit-signals', True)
        #self.set_property('drop', True)

        self.pipeline.add(self.tcpsrc)
        self.pipeline.add(self.gdepay)

        self.pipeline.add(self.avdec)

        self.pipeline.add(self.rdepay)

        self.pipeline.add(self.vidconvert)
        self.pipeline.add(self.asink)

        self.tcpsrc.link(self.gdepay)
        self.gdepay.link(self.rdepay)
        self.rdepay.link(self.avdec)
        self.avdec.link(self.vidconvert)
        self.vidconvert.link(self.asink)
##############################################################################
#^
#|
#|
#VIDEO Pipeline
##############################################################################

    def on_sync_message(self, bus, message):
        if message.get_structure().get_name() == 'prepare-window-handle':
            message.src.set_property('force-aspect-ratio', True)
            message.src.set_window_handle(self.winId)

    def quit(self, container):
        self.pipeline.set_state(Gst.State.NULL)
        #self.pipeline_A.set_state(Gst.State.NULL)
        Gtk.main_quit()

    def on_eos(self, bus, msg):
        print('on_eos(): seeking to start of video')
        self.pipeline.seek_simple(
            Gst.Format.TIME,
            Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT,
            0
        )

    def on_error(self, bus, msg):
        print('on_error():', msg.parse_error())

    def start(self):
        self.pipeline.set_state(Gst.State.PLAYING)
        #self.pipeline_A.set_state(Gst.State.PLAYING)
        self.showMaximized()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.start()
    sys.exit(app.exec_())