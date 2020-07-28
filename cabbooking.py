from tkinter import*
import random
import os
#from PIL import ImageTk,Image
creds = 'tempfile2.temp'
distance='tempfile11.temp'
def Signup():
    global pwordE
    global nameE
    global roots
    roots=Tk()
    roots.title('signup')
    roots.geometry("900x500+0+0")
    instruction=Label(roots,text='please enter new credentials\n',font='18,bold')
    instruction.grid(row=0,column=0,sticky=E)
    nameL=Label(roots,text='new user name',font='18,bold')
    pwordL=Label(roots,text='new password',font='18,bold')
    nameL.grid(row=1,column=0,sticky=W)
    pwordL.grid(row=2,column=0,sticky=W)
    nameE=Entry(roots)
    pwordE=Entry(roots,show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)
    signupButton=Button(roots,text='signup',font='18,bold',bg='green',command=FSSignup)
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()
def FSSignup():
    with open(creds,'w')as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()
    roots.destroy()
    Login()
#def image():
   # global ik
    #ik=ImageTk.PhotoImage(Image.open("Cabs_Service.jpg"))
    
def Login():
    global nameEL
    global pwordEL
    global rootA
    rootA=Tk()
    rootA.geometry("900x500+0+0")
    rootA.title('login')
    instruction=Label(rootA,text='please login',font='18,bold')
    instruction.grid(sticky=E)
    nameL=Label(rootA,text='username',font='18,bold')
    pwordL=Label(rootA,text='password',font='18,bold')
    nameL.grid(row=1,sticky=W)
    pwordL.grid(row=2,sticky=W)
    nameEL=Entry(rootA)
    pwordEL=Entry(rootA,show="*")
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)
    loginB=Button(rootA,text='login',font='18,bold',bg='green',command=CheckLogin)
    loginB.grid(columnspan=2,sticky=W)
    reuser=Button(rootA,text='signup',font='18,bold',bg='red',command=DelUser)
    reuser.grid(columnspan=2,sticky=W)
    load=Image.open("booking.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(rootA,image=render)
    img.image=render
    img.place(x=0,y=200)
    rootA.mainloop()
    
def CheckLogin():
    with open(creds) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        pword=data[1].rstrip()
    if nameEL.get()==uname and pwordEL.get()==pword:
        global r
        global e1
        global e2
        global e3
        r=Tk()
        r.title('info')
        r.geometry("900x500+0+0")
        r.configure(background="#ffdddd")
        i=Label(r,text='please enter \n',font=("Times", "18", "bold italic"))
        i.pack()
        t=Label(r,text='enter your location',font=("Times", "18", "bold italic"),fg='white',bg='pink')
        t.pack()
        e1=Entry(r)
        e1.pack()
        p=Label(r,text='enter your destination',font=("Times", "18", "bold italic"),fg='white',bg="pink")
        p.pack()
        e2=Entry(r)
        e2.pack()
        k=Label(r,text="please enter the distance",font=("Times", "18", "bold italic"),fg='white',bg="pink")
        k.pack()
        e3=Entry(r)
        e3.pack()
        confrim=Button(r,text="confrim",font=("Times", "18", "bold italic"),command=Fetch)
        confrim.pack()
        r.mainloop()
    else:
        r=Tk()
        rlbl=Label(r,text="\n[!] invalid login",font=("24,bold"))
        rlbl.pack()
        r.mainloop()
def Fetch():
    with open(distance,'w')as f:
        f.write(e1.get())
        f.write('\n')
        f.write(e2.get())
        f.write('\n')
        f.write(e3.get())
        f.close()
    vehicle()
def display():
    k1=Tk()
    k1.title("conformation")
    k1.geometry("900x500+0+0")
    ab=Label(k1,text="your ride is confirmed and is on it's way.\nThe driver number is:",font=("Times", "24", "bold italic"))
    ab.pack()
    nn=random.randint(8000000000,10000000000)
    drivernum=Label(k1,text=str(nn),font=('Arial',15))
    drivernum.pack()
    ab1=Label(k1,text="Your cab number:",font=("Times", "24", "bold italic"))
    ab1.pack()
    nn1=random.randint(999,9999)
    num=Label(k1,text=str(nn1),font=('Arial',15))
    num.pack()
    ab2=Label(k1,text="The driver's code is:",font=("Times", "24", "bold italic"))
    ab2.pack()
    nn2=random.randint(999,9999)
    drivercode=Label(k1,text=str(nn2),font=('Arial',15))
    drivercode.pack()
    thank=Label(k1,text='THANK YOU!!!!',font=("Times", "28", "bold italic"),fg='orange')
    thank.pack()
    k1.mainloop()
    
def select1():
    r1=Tk()
    r1.title("Proceed to pay")
    r1.geometry("900x500+0+0")
    h=Label(r1,text="you selected auto",font=("Times", "24", "italic"),fg="green")
    h.pack()
    n=int(e3.get())*10
    place=Label(r1,text="The total amount is",font=("Times", "24", "bold italic"))
    place.pack()
    total=Label(r1,text=str(n),font=('Arial',15))
    total.pack()
    book=Button(r1,text="BOOK",font=("Times", "18", "bold italic"),command=display)
    book.pack()
def select2():
    r2=Tk()
    r2.title("proceed to pay")
    r2.geometry("900x500+0+0")
    h1=Label(r2,text="you selected mini",font=("Times", "24", "italic"),fg="green")
    h1.pack()
    n1=int(e3.get())*15
    place1=Label(r2,text="The total amount is",font=("Times", "24", "bold italic"))
    place1.pack()
    total=Label(r2,text=str(n1),font=('Arial',15))
    total.pack()
    book=Button(r2,text="BOOK",font=("Times", "18", "bold italic"),command=display)
    book.pack()
def select3():
    r3=Tk()
    r3.title("proceed to pay")
    r3.geometry("900x500+0+0")
    h2=Label(r3,text="you selected micro",font=("Times", "24", "bold italic"),fg="green")
    h2.pack()
    n2=int(e3.get())*18
    place2=Label(r3,text="The total amount is",font=("Times", "24", "bold italic"))
    place2.pack()
    total=Label(r3,text=str(n2),font=('Arial',15))
    total.pack()
    book=Button(r3,text="BOOK",font=("Times", "18", "bold italic"),command=display)
    book.pack()
def select4():
    r4=Tk()
    r4.title("proceed to pay")
    r4.geometry("900x500+0+0")
    h3=Label(r4,text="you selected prime",font=("Times", "24", "bold italic"),fg="green")
    h3.pack()
    n3=int(e3.get())*20
    place3=Label(r4,text="The total amount is",font=("Times", "24", "italic"))
    place3.pack()
    total=Label(r4,text=str(n3),font=('Arial',15))
    total.pack()
    book=Button(r4,text="BOOK",font=("Times", "18", "bold italic"),command=display)
    book.pack()
def select5():
    r5=Tk()
    r5.title("proceed to pay")
    r5.geometry("900x500+0+0")
    h4=Label(r5,text="you selected suv",font=("Times", "24", "bold italic"),fg="green")
    h4.pack()
    n4=int(e3.get())*22
    place4=Label(r5,text="The total amount is",font=("Times", "24", "italic"))
    place4.pack()
    total=Label(r5,text=str(n4),font=('Arial',15))
    total.pack()
    book=Button(r5,text="BOOK",font=("Times", "18", "bold italic"),command=display)
    book.pack()
def vehicle():
    root=Tk()
        
    root.title('Welcome to Kabs')

   # v=IntVar()

    root.geometry("900x500+0+0")
    root.configure(background="#ffdddd")
    y1=Label(root,text="Select your vehicle",font=("Times", "24", "bold italic"))
    y1.pack()
    x=Button(root,text='Auto',font=("Times", "24", "bold italic"),command=select1)
    x.pack()
    y=Button(root,text='mini',font=("Times", "24", "bold italic"),command=select2)
    y.pack()
    z=Button(root,text='micro',font=("Times", "24", "bold italic"),command=select3)
    z.pack()
    o=Button(root,text='prime',font=("Times", "24", "bold italic"),command=select4)
    o.pack()
    x1=Button(root,text='SUV',font=("Times", "24", "bold italic"),command=select5)
    x1.pack()
    root.mainloop()

    
def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()
if os.path.isfile(creds):
    Login()
else:
    Signup()
