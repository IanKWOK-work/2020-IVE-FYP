
import pygst
pygst.require('0.10')
import gst

import pygtk
pygtk.require('2.0')
import gtk

# this is very important, without this, callbacks from gstreamer thread
# will messed our program up
gtk.gdk.threads_init()

def main():
 pipeline = gst.Pipeline('pipleline')

 filesrc = gst.element_factory_make("filesrc","filesrc")
 filesrc.set_property('location', 'C:/a.mp3')

 decode = gst.element_factory_make("decodebin","decode")

 convert = gst.element_factory_make('audioconvert', 'convert')

 sink = gst.element_factory_make("autoaudiosink","sink")

 pipeline.add(filesrc, decode, convert, sink)
 gst.element_link_many(filesrc, decode, convert, sink)

 pipeline.set_state(gst.STATE_PLAYING)

 gtk.main()

main()