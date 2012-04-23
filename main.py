from gi.repository import Gtk, Gdk, GtkSource, GObject

class ECC(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self,title='Error Control Codes')

		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		self.result = Gtk.Label('test')

		self.vbox.pack_start(self.resultFalse,True,0)

		self.add(self.vbox)

#initiate window
win = ECC()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
