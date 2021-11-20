import sys
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

Gst.init(sys.argv)
# Gst.Pipeline
pipeline = Gst.parse_launch("videotestsrc num-buffers=50 ! autovideosink")

# create pipeline object
pipeline = Gst.Pipeline()

# create Gst.Element by plugin name
src = Gst.ElementFactory.make("videotestsrc")

# as Gst.Element inherit from GObject
# we can use GObject methods to set property of element
src.set_property("num-buffers", 50)

# create Gst.Element by plugin name
sink = Gst.ElementFactory.make("gtksink")

# as Gst.Pipeline is container of Gst.Elements
# add src, sink to Gst.Pipeline
pipeline.add(src, sink)

# link src with sink
# Note: elements should be elements of same Gst.Pipeline
src.link(sink)

pipeline.set_state(Gst.State.PLAYING)