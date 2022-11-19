from tkinter import *

root = Tk()

#label widget
def myClick():
    Label(root, text="xd").grid(row=0)
def save():
    file = open('xdd.txt', 'w')
    file.write('no hej')
    file.close()



myButton1 = Button(root,text="Kliknij mnie  😳",padx=50,pady=50,font=50,command=myClick)
myButton2 = Button(root,text="Zapisz",padx=50,pady=50,font=50,command=save)
myButton1.grid(row=1)
myButton2.grid(row=2)
root.mainloop()

