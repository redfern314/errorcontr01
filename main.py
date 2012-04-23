#Import packages. Only using Gtk right now but the others can be useful.
from gi.repository import Gtk, Gdk, GObject

class ECC(Gtk.Window):

	#Called when new class instance is created
	def __init__(self):
		#Call parent constructor to create the Gtk window
		Gtk.Window.__init__(self,title='Error Control Codes')

		#Create a vertical box to pack widgets into, and a label widget to pack into it
		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		self.result = Gtk.Label('test')

		#Pack the label into the box. Syntax: pack_start(widget,expand,fill,padding). pack_end is also a thing.
		self.vbox.pack_start(self.result,False,True,0)
		self.add(self.vbox) #add the box to the window

#initiate window
win = ECC()
win.connect("delete-event",Gtk.main_quit) #this way, you can close the window
win.show_all()
Gtk.main() #Start the Gtk main loop
