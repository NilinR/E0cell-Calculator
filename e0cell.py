from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
#for images

#creating main tkinter base
root = Tk()
root.title("E*cell Calculator")
#making it full screened
root.state('zoomed')

#creating canvases
canvas =Canvas(root, highlightthickness=7, highlightbackground="black")
canvas.pack(fill=BOTH, expand=True)

sep=Canvas(canvas,width=523,height=650,highlightthickness=3, highlightbackground="black")
sep.place(x=1000,y=4)

con=Canvas(canvas,width=1000,height=650,bg='PaleTurquoise2',highlightthickness=3, highlightbackground="black")
con.place(x=6,y=4)
l=Label(con,text=' E*cell Calculator ', font=('Times', 40))
l.place(x=283,y=20)

#placing images
image=Image.open('be.png')
img= ImageTk.PhotoImage(image)
con.create_image(205,200,anchor=NW,image=img)
i1=Image.open('e.png').resize((70, 300))
ig1=ImageTk.PhotoImage(i1)
i2=Image.open('el.png').resize((72, 288))
ig2=ImageTk.PhotoImage(i2)

#values to be inserted
n1,n2=StringVar(),StringVar()

#creating class for function
class GalvanicCell():

    def __init__(self, ec_series):
        self.ec_series = ec_series
        self.anode,self.cathode = None,None
        
    #figures out anode and cathode
    def checker(self):
        #places image
        con.create_image((255,257),anchor=NW,image=ig1)
        con.create_image((657,247),anchor=NW,image=ig2)

        #takes in input
        m1,m2=n1.get(),n2.get()

        #figuring anode and cathode
        if m1!=m2:
            if self.ec_series[m1] > self.ec_series[m2]:
                self.anode,self.cathode= m2, m1
            else:
                self.anode,self.cathode= m1, m2
            l1=Label(canvas,text=f"Anode is {self.anode}, Cathode is {self.cathode}", font=('Times', 18)).place(x=1150,y=500)
            enotcell =self.ec_series[self.cathode]-self.ec_series[self.anode]
            l2=Label(canvas,text=f"E*cell is {enotcell}", font=('Times', 18)).place(x=1150,y=550)
        else:
            messagebox.showinfo("Error", "Can't enter same metal")

    #taking in values
    def enotcellcalc(self):
        sep2=Canvas(canvas,width=523,height=650,highlightthickness=3, highlightbackground="black")
        sep2.place(x=1000,y=4)
        l3=Label(sep2,text='Enter Metal 1:', font=('Times', 16)).place(x=50,y=20)
        d1=ttk.Combobox(sep2,font=('Times', 18),values=[k  for  k in  ec_series.keys()],textvariable = n1).place(x=50,y=60)
        l4=Label(sep2,text='Enter Metal 2:', font=('Times', 16)).place(x=50,y=110)
        d2=ttk.Combobox(sep2,font=('Times', 18),values=[k  for  k in  ec_series.keys()],textvariable = n2).place(x=50,y=160) 
        b4=Button(sep2,width=5,bg='Light Green', text='>', font=('Times', 19),command=cell.checker).place(x=50,y=300)

    def dis(self):
        sep3=Canvas(canvas,width=523,height=650,highlightthickness=3, highlightbackground="black")
        sep3.place(x=1000,y=4)
        j=20
        for i in ec_series:
            l5=Label(sep3,font=('Times', 17),text=i).place(x=200,y=j)
            j+=30
            
#dictionary of values
ec_series = {
    "Li": -3.05,
    "K": -2.925,
    "Ca": -2.87,
    "Na": -2.714,
    "Mg": -2.37,
    "Al": -1.66,
    "Zn": -0.7628,
    "Cr": -0.74,
    "Fe": -0.44,
    "Cd": -0.403,
    "Ni": -0.25,
    "Sn": -0.14,
    "H2": 0.00,
    "Cu": +0.337,
    "I2": +0.535,
    "Ag": +0.799,
    "Hg": +0.885,
    "Br2": +1.08,
    "Cl2": +1.36,
    "Au": +1.50,
    "F2": +2.87
}

#calling function
cell = GalvanicCell(ec_series)

#adding and placing buttons
b1 =Button(canvas,width=30,bg='light blue', text='Calculate E*cell', font=('Times', 19),cursor='hand2',command=cell.enotcellcalc)
b1.place(x=63, y=700)
b2=Button(canvas, width=30, bg='light blue',text='Display elements', font=('Times', 19),cursor='hand2',command=cell.dis)
b2.place(x=550, y=700)
b3=Button(canvas,width=30,bg='light blue', text='Exit', font=('Times', 19),cursor='hand2',command=root.destroy)
b3.place(x=1037, y=700)

#executing tkinter as loop
root.mainloop()
