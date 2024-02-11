import qrcode
from tkinter import *
from tkinter import filedialog
import threading




root =Tk()
root.geometry("500x280")
root.resizable(False,False)
root.title("Qr Code Maker")


Logo = PhotoImage(file='logo2.png').subsample(2)
qrTitle =Label(root, image=Logo)
qrTitle.place( relx=0.5, rely=0.25 , anchor="center")
 

def make():
    url=qrcode.make(link.get())
    url.save(link2.get() + "/" + link3.get() +".png")
    

def browse():
    directory =filedialog.askdirectory(title="save image")
    link2.delete(0,"end")
    link2.insert(0,directory)



label1= Label(root,text="URL")
label1.place(x=50,y=105)

link = Entry(root,width=50)
link.place(x=90,y=105)

label3= Label(root,text="Name")
label3.place(x=50,y=150)

link3= Entry(root,width=50)
link3.place(x=90,y=152)

label2= Label(root,text="place")
label2.place(x=50,y=195)


link2 = Entry(root,width=50)
link2.place(x=90,y=195)

browse = Button(root,text="Browse" ,command=browse)
browse.place(x=400,y=192)

save = Button(root,text="Make" ,command=make)
save.place(x=220,y=235)



root.mainloop()