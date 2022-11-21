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

def wyswietl():
    tajp=nx.empty_graph()
    if (type(G)==type(tajp)):
        plt.show()
        nx.draw(G)

    return
myButton3 = Button(root,text="Wyswietl",padx=p,pady=p,font=50,command=wyswietl)
myButton3.grid(row=3)

root.mainloop()

