#Import packages. Only using Gtk right now but the others can be useful.
from gi.repository import Gtk, Gdk, GObject
from mathCode import *
import pdb

class ECC(Gtk.Window):

    #Called when new class instance is created
    def __init__(self):
        #Call parent constructor to create the Gtk window
        Gtk.Window.__init__(self,title='Error Control Codes')

        #make it a decent size
        self.set_default_size(800,500)

        #Create a vertical box to pack widgets into, and a label widget to pack into it
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.step1 = Gtk.Label('Step 1: Enter a word to be transmitted (length=4):')
        self.word = Gtk.Entry()
        self.binaryword = Gtk.Label('Your converted string: [enter a word]')

        self.flipbits=Gtk.Button('Transmit Message')
        self.enterbutton=Gtk.Button('Convert my string to binary!')
        self.encode=Gtk.Button('Encode my message')
        self.codeword = Gtk.Label('Your encoded message: [press encode]')

        self.step1box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.step1box.pack_start(self.step1,False,False,0)
        self.step1box.pack_start(self.word,False,False,0)
        self.step2 = Gtk.Label('Step 2: Convert string to binary')
        self.step2box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.step2box.pack_start(self.step2,False,False,0)
        self.step2box.pack_start(self.enterbutton,False,False,0)
        self.step2box.pack_start(self.binaryword,False,False,0)
        self.step3 = Gtk.Label('Step 3: Generate codewords for the binary message')
        self.step3box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.step3box.pack_start(self.step3,False,False,0)
        self.step3box.pack_start(self.encode,False,False,0)
        self.step3box.pack_start(self.codeword,False,False,0)
        self.step4 = Gtk.Label('Step 4: Transmit your message!')
        self.step4box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.step4box.pack_start(self.step4,False,False,0)
        self.step4box.pack_start(self.flipbits,False,False,0)

        self.frame1 = Gtk.Frame()
        self.frame1.add(self.step1box)
        self.frame2 = Gtk.Frame()
        self.frame2.add(self.step2box)
        self.frame3 = Gtk.Frame()
        self.frame3.add(self.step3box)
        self.frame4 = Gtk.Frame()
        self.frame4.add(self.step4box)

        #Pack the label into the box. Syntax: pack_start(widget,expand,fill,padding). pack_end is also a thing.
        '''
        self.vbox.pack_start(self.step1,False,True,0)
        self.vbox.pack_start(self.word,False,False,0)
        self.vbox.pack_start(self.enterbutton,False,False,0)
        self.vbox.pack_start(self.binaryword,False,False,0)
        self.vbox.pack_start(self.encode,False,False,0)
        self.vbox.pack_start(self.codeword,False,False,0)
        self.vbox.pack_start(self.flipbits,False,False,0)'''
        self.vbox.pack_start(self.frame1,False,False,0)
        self.vbox.pack_start(self.frame2,False,False,0)
        self.vbox.pack_start(self.frame3,False,False,0)
        self.vbox.pack_start(self.frame4,False,False,0)
        self.flipbits.connect('clicked',self.opendialog)
        self.enterbutton.connect('clicked',self.converttext)
        self.encode.connect('clicked',self.generatecode)
        self.word.connect('key-press-event',self.on_key_press)
        self.add(self.vbox) #add the box to the window

    def converttext(self,widget=None):
        text=self.word.get_text().lower()
        if not text=='':
            binary=''
            for letter in text:
                binary=binary+bin(ord(letter)-97)[2:].zfill(5)
            self.binaryword.set_text('Your converted string: '+binary)
        else:
            self.binaryword.set_text('Your converted string: [enter a word]')

    def generatecode(self,widget=None):
        message=self.binaryword.get_text()[23:]
        #Corrects the error vector
        m=mat([1,0]) 
        print "The original message is:"
        print m
        c=getCodeword(m)
        print "The encoded message before errors is:"
        print c
        c[0,0]=0#introduce error
        print "The code after an error is introduced is:"
        print c
        e=getError(c)
        print "The error is:"
        print e
        print "The codeword after error correction is:"
        print e+c



    def opendialog(self,widget):
        dialog = ErrorDialog(self,self.binaryword.get_text()[23:])
        response = dialog.run()
        dialog.destroy()

    def on_key_press(self,widget,data):
        val=data.keyval
        if val==65288:
            return False
        elif len(self.word.get_text())>=5:
            return True
        elif val==65293:
            self.converttext()
        elif not(val<=122 and val>=65):
            return True


class ErrorDialog(Gtk.Dialog):
    def __init__(self,parent,codeword):
        #Gtk.Dialog.__init__(self, "Search", parent,Gtk.DialogFlags.MODAL, buttons=(Gtk.STOCK_FIND, Gtk.ResponseType.OK,Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        Gtk.Dialog.__init__(self, flags=Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT, title="My Dialog", parent=parent, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        
        self.toggle=[]
        self.table=Gtk.Table(4,5,True)
        self.vboxerror = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        self.labelstart=Gtk.Label('While transmitting your codeword '+codeword+', magnetic interference created errors within your code.\nSelect which bits to flip:')
        self.vboxerror.pack_start(self.labelstart,True,True,0)
        self.tables = []
        if len(codeword)%10 == 0:
            numtables=len(codeword)/10
        else:
            numtables=len(codeword)/10+1
        for i in range(numtables):
            self.tables.append(Gtk.Table(1,10,True))
            self.vboxerror.pack_start(self.tables[i],True,True,0)
        count=0
        for char in codeword:
            self.toggle.append(Gtk.ToggleButton(char))
            self.toggle[count].connect('toggled',self.bitflip,count)
            self.tables[count/10].attach(self.toggle[count],count%10,(count%10)+1,0,1)
            count+=1
        self.labelend=Gtk.Label('New codeword: '+codeword)
        self.vboxerror.pack_start(self.labelend,True,True,0)
        box=self.get_content_area()
        box.add(self.vboxerror)

        self.show_all()

    def bitflip(self,widget,number):
        #if widget.get_active():
        if True:
            if self.toggle[number].get_label()=='0':
                self.toggle[number].set_label('1')
            else:
                self.toggle[number].set_label('0')
        text=''
        for i in range(len(self.toggle)):
            text=text+self.toggle[i].get_label()
        self.labelend.set_text('New codeword: '+text)

#initiate window
win = ECC()
win.connect("delete-event",Gtk.main_quit) #this way, you can close the window
win.show_all()
Gtk.main() #Start the Gtk main loop
