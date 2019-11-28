from tkinter import *
from tkinter.ttk import *

def eror(x):
    lo=["Binary","Octal","Decimal","Hexadecimal"]
    eror=Tk()
    eror.title("!!!!!!WARNING!!!!!!")
    if x==1:
        txt1=Label(eror,text="!!PLEASE ENTER THE NUMBER!!",font=("Arial Bold",10))
    elif x==2:
        txt1=Label(eror,text="!!PLEASE SELECT THE NUMBER SYSTEMS!!",font=("Arial Bold",10))
    elif x==3:
        txt1=Label(eror,text="!!Enter Valid "+lo[(var.get()-1)]+" !!",font=("Arial Bold",10))
    txt1.grid(column=1,row=1,pady=(50,5),padx=(100,0))
    btn1=Button(eror,text="OK",command=eror.destroy)
    btn1.grid(column=2,row=3,pady=(10,10),padx=(10,10))
    btn1.focus()
    eror.mainloop()

def check():
    li=list(box1.get())
    if var.get()==1:
        for i in range(len(li)):
            if li[i] not in range(2):
                print(li[i])
                eror(3)
                break
    elif var.get()==2:
        for i in range(len(li)):
            if li[i] not in range(8):
                print(li[i])
                eror(3)
                break
    elif var.get()==3:
        for i in range(len(li)):
            if li[i] not in range(10):
                print(li[i])
                eror(3)
                break
    elif var.get()==4:
        for i in range(len(li)):
            if li[i] not in ['0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','D','d','E','e','f','F']:
                print(li[i])
                eror(3)
                break

def disp(x):
    lx=[0,2,8,10,16]
    lo=["Binary","Octal","Decimal","Hexadecimal"]
    lp=[a.get(),b.get(),c.get(),d.get()]
    res=Tk()
    res.title("Result")
    i=0
    lz=[bin(int(box1.get(),lx[x])),oct(int(box1.get(),lx[x])),(int(box1.get(),lx[x])),hex(int(box1.get(),lx[x]))]
    for i in range(4):
        if lp[i]==1:
            if i==2:
                txt1=Label(res,text=str(lo[i])+" = "+str(lz[i]),font=("Arial Bold",10))
                txt1.grid(column=1,row=i,pady=(10,10),padx=(100,100))
            else:
                txt1=Label(res,text=str(lo[i])+" = "+str(lz[i])[2:],font=("Arial Bold",10))
                txt1.grid(column=1,row=i,pady=(10,10),padx=(100,100))
    btn1=Button(res,text="OK",command=res.destroy)
    btn1.grid(column=2,row=i+1,pady=(10,10),padx=(10,10))
    btn1.focus()
    res.mainloop()
    
def valid():
    if box1.get()=="":
        eror(1)
    elif var.get()==0 or (a.get()==0 and b.get()==0 and c.get()==0 and d.get()==0):
        eror(2)
    check()

def result():
    valid()
    disp(var.get())
    
def desc():
    valid()
    x=var.get()
    lx=[0,2,8,10,16]
    lo=["Binary","Octal","Decimal","Hexadecimal"]
    lp=[a.get(),b.get(),c.get(),d.get()]
    exp=Tk()
    exp.title("Result")
    txt1=Label(exp,text="The Converison of "+lo[(var.get())-1]+" Number "+box1.get()+" are = ",font=("Arial Bold",10))
    txt1.grid(column=1,row=0,pady=(10,10),padx=(100,100))
    i=1
    lz=[bin(int(box1.get(),lx[x])),oct(int(box1.get(),lx[x])),(int(box1.get(),lx[x])),hex(int(box1.get(),lx[x]))]
    for i in range(4):
        if lp[i]==1:
            if i==2:
                txt1=Label(exp,text=str("When you Take Sum of all the digits multiplying the weight "+str(lx[i+1])+" You Get "+lo[i])+" = "+str(lz[i]),font=("Arial Bold",10))
                txt1.grid(column=1,row=i+1,pady=(10,10),padx=(100,100))
            else:
                txt1=Label(exp,text=str("When you Take Sum of all the digits multiplying the weight "+str(lx[i+1])+" You Get "+lo[i])+" = "+str(lz[i][2:]),font=("Arial Bold",10))
                txt1.grid(column=1,row=i+1,pady=(10,10),padx=(100,100))
    btn1=Button(exp,text="OK",command=exp.destroy)
    btn1.grid(column=2,row=i+2,pady=(10,10),padx=(10,10))
    btn1.focus()
    exp.mainloop()
    

main=Tk()
main.title("Number System Converter")
var=IntVar()
txt1=Label(main,text="Enter No. To Be Converted ",font=("arial",10))
txt1.grid(column=1,row=1,pady=(10,5),padx=(5,5))
box1=Entry(main,width=15)
box1.grid(column=2,row=1,pady=(10,5))
box1.focus()
space=Label(main,text="         ",font=("Arial",10))
space.grid(column=3,row=2)
rad1 = Radiobutton(main,text='Binary   ', value=1,variable=var)
rad2 = Radiobutton(main,text='Octal     ', value=2,variable=var)
rad3 = Radiobutton(main,text='Decimal', value=3,variable=var)
rad4= Radiobutton(main,text='Hexadecimal', value=4,variable=var)
rad1.grid(row=3, column=2)
rad2.grid(row=4,column=2)
rad3.grid(row=5, column=2)
rad4.grid(column=2,row=6,padx=(25,0))
a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
txt11=Label(main,text="No. To Be Converted In ",font=("arial",10))
txt11.grid(column=4,row=2,pady=(5,5),padx=(5,5))
ch1=Checkbutton(main,text="Binary            ",variable=a)
ch1.grid(row=3,column=4)
ch2=Checkbutton(main,text="Octal             ",variable=b)
ch2.grid(row=4,column=4)
ch3=Checkbutton(main,text="Decimal        ",variable=c)
ch3.grid(row=5,column=4)
ch4=Checkbutton(main,text="Hexadecimal",variable=d)
ch4.grid(row=6,column=4)
btn1=Button(main,text="Results",command=result)
btn1.grid(row=7,column=3,pady=(5,10))
btn1=Button(main,text="Explanation",command=desc)
btn1.grid(row=7,column=5,pady=(5,10),padx=(10,10))
main.mainloop()