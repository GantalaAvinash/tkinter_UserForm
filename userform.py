from tkinter import *
root=Tk()
root.geometry("980x700+0+0")
root.title("Cyber Security")
root.configure(bg="sky blue")

Tops = Frame(root,bg="light blue",width = 980,height=150,relief=SUNKEN)
Tops.pack(side=TOP)


#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="User Registration",fg="steel blue",bg="light green")
lblinfo.grid(row=0,column=1)
lbl = Label(Tops,bg="light blue",bd='50')
lbl.grid(row=0,column=2)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=2,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=3,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=4,column=0)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Name:",bd='15',fg="steel blue",bg="light blue")
lbl.grid(row=5,column=0)
e1 = Entry(Tops,font=('ariel' ,10,'bold') ,justify='left')
e1.grid(row=5,column=1)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Rollno:",bd='15',fg="steel blue",bg="light blue")
lbl.grid(row=6,column=0)
e2 = Entry(Tops,font=('ariel' ,10,'bold'),justify='left')
e2.grid(row=6,column=1)



#-----------------Radio Button------------

v=IntVar()
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Gender:",bd='15',fg="steel blue",bg="light blue")
lbl.grid(row=7,column=0)
r1=Radiobutton(Tops,text="Female",fg="steel blue",bg="light blue",variable=v,value=1)
r1.grid(column=1,row=7)
r2=Radiobutton(Tops,text=" Male ",fg="steel blue",bg="light blue",variable=v,value=2)
r2.grid(column=1,row=8)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Fav Language:",bd='5',fg="steel blue",bg="light blue")
lbl.grid(row=9,column=0)



#-----------------Check Button------------

v1=IntVar()
v2=IntVar()
v3=IntVar()
c1=Checkbutton(Tops,text="python",fg="steel blue",bd='6',bg="light blue",variable=v1,onvalue=1,offvalue=0)
c1.grid(column=1,row=9)
c2=Checkbutton(Tops,text=" Java   ",fg="steel blue",bd='6',bg="light blue",variable=v2,onvalue=1,offvalue=0)
c2.grid(column=1,row=10)
c3=Checkbutton(Tops,text=" C#    ",fg="steel blue",bd='6',bg="light blue",variable=v3,onvalue=1,offvalue=0)
c3.grid(column=1,row=11)
lbl = Label(Tops, font=( 'aria' ,16, 'bold' ),text="Batch:",bd='5',fg="steel blue",bg="light blue")
lbl.grid(row=12,column=0)


#-----------------Spin Box------------

s=Spinbox(Tops,from_=0,to=4)
s.grid(column=1,row=12)

#-----------------Submit Button Calling Function------------
def call():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("User Registration","Enter Your Details")
    else:
        messagebox.showinfo("Login","Hello\t"+e1.get()+"\nRegistration Done \U0001F618")
    import loginpage
   
        
btn=Button(Tops,text="Submit",font=('ariel' ,16,'bold'),command=call)
btn.grid(column=1,row=14)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=16,column=0)
lbl = Label(Tops,bg="light blue")
lbl.grid(row=17,column=0)

root.mainloop()
