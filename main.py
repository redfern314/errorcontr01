#Import packages. Only using Gtk right now but the others can be useful.
from gi.repository import Gtk, Gdk, GObject

class ECC(Gtk.Window):

    #Called when new class instance is created
    def __init__(self):
        #Call parent constructor to create the Gtk window
        Gtk.Window.__init__(self,title='Error Control Codes')

        #make it a decent size
        self.set_default_size(800,500)

        #Create a vertical box to pack widgets into, and a label widget to pack into it
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.result = Gtk.Label('Enter a word to be transmitted (length<=7):')
        self.word = Gtk.Entry()
        self.binaryword = Gtk.Label('')

        self.dialogbutton=Gtk.Button('Open Dialog')
        self.enterbutton=Gtk.Button('Convert my string to binary!')

        #Pack the label into the box. Syntax: pack_start(widget,expand,fill,padding). pack_end is also a thing.
        self.vbox.pack_start(self.result,False,True,0)
        self.vbox.pack_start(self.word,False,False,0)
        self.vbox.pack_start(self.enterbutton,False,False,0)
        self.vbox.pack_start(self.binaryword,False, False,0)
        self.vbox.pack_end(self.dialogbutton,False,False,0)
        self.dialogbutton.connect('clicked',self.opendialog)
        self.enterbutton.connect('clicked',self.converttext)
        self.add(self.vbox) #add the box to the window

    def converttext(self,widget):
        text=self.word.get_text().lower()
        binary=''
        for letter in text:
            binary=binary+bin(ord(letter)-97)[2:].zfill(5)
        self.binaryword.set_text('Your converted string: '+binary)

    def opendialog(self,widget):
        dialog = ErrorDialog(self)
        response = dialog.run()
        dialog.destroy()

class ErrorDialog(Gtk.Dialog):
    def __init__(self,parent):
        #Gtk.Dialog.__init__(self, "Search", parent,Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_FIND, Gtk.ResponseType.OK,Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        Gtk.Dialog.__init__(self, flags=Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT, title="My Dialog", parent=parent, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        
        self.table=Gtk.Table(4,5,True)
        self.labelstart=Gtk.Label('While transmitting your codeword '+'01101'+', magnetic interference created errors within your code.\nSelect which bits to flip:')
        self.label1=Gtk.Label('0')
        self.label2=Gtk.Label('1')
        self.label3=Gtk.Label('1')
        self.label4=Gtk.Label('0')
        self.label5=Gtk.Label('1')
        self.labelend=Gtk.Label('New codeword: '+'01101')
        self.toggle1=Gtk.ToggleButton('Flip')
        self.toggle1.connect('toggled',self.bitflip,1)
        self.toggle2=Gtk.ToggleButton('Flip')
        self.toggle2.connect('toggled',self.bitflip,2)
        self.toggle3=Gtk.ToggleButton('Flip')
        self.toggle3.connect('toggled',self.bitflip,3)
        self.toggle4=Gtk.ToggleButton('Flip')
        self.toggle4.connect('toggled',self.bitflip,4)
        self.toggle5=Gtk.ToggleButton('Flip')
        self.toggle5.connect('toggled',self.bitflip,5)
        self.table.attach(self.labelstart,0,5,0,1)
        self.table.attach(self.label1,0,1,1,2)
        self.table.attach(self.label2,1,2,1,2)
        self.table.attach(self.label3,2,3,1,2)
        self.table.attach(self.label4,3,4,1,2)
        self.table.attach(self.label5,4,5,1,2)
        self.table.attach(self.toggle1,0,1,2,3)
        self.table.attach(self.toggle2,1,2,2,3)
        self.table.attach(self.toggle3,2,3,2,3)
        self.table.attach(self.toggle4,3,4,2,3)
        self.table.attach(self.toggle5,4,5,2,3)
        self.table.attach(self.labelend,0,5,3,4)
        box=self.get_content_area()
        box.add(self.table)

        self.show_all()

    def bitflip(self,widget,number):
        #if widget.get_active():
        if True:
            if number==1:
                if self.label1.get_text()=='0':
                    self.label1.set_text('1')
                else:
                    self.label1.set_text('0')
            elif number==2:
                if self.label2.get_text()=='0':
                    self.label2.set_text('1')
                else:
                    self.label2.set_text('0')
            elif number==3:
                if self.label3.get_text()=='0':
                    self.label3.set_text('1')
                else:
                    self.label3.set_text('0')
            elif number==4:
                if self.label4.get_text()=='0':
                    self.label4.set_text('1')
                else:
                    self.label4.set_text('0')
            elif number==5:
                if self.label5.get_text()=='0':
                    self.label5.set_text('1')
                else:
                    self.label5.set_text('0')
        self.labelend.set_text('New codeword: '+self.label1.get_text()+self.label2.get_text()+self.label3.get_text()+self.label4.get_text()+self.label5.get_text())

#initiate window
win = ECC()
win.connect("delete-event",Gtk.main_quit) #this way, you can close the window
win.show_all()
Gtk.main() #Start the Gtk main loop
