from tkinter import *
from tkinter.ttk import *

def error(x):    
    eror=Tk()
    eror.title("!!!!!!WARNING!!!!!!")
    eror.geometry('520x120')
    if x==1:
        txt1=Label(eror,text="!!PLEASE ENTER BOTH THE NUMBERS!!",font=("Arial Bold",10))
    elif x==2:
        txt1=Label(eror,text="!!PLEASE SELECT OPTION TO PERFORM!!",font=("Arial Bold",10))
    elif x==3:
        txt1=Label(eror,text="!!PLEASE ENTER INTGER VALUES!!",font=("Arial Bold",10))
    txt1.grid(column=1,row=1,pady=(50,5),padx=(100,0))
    btn1=Button(eror,text="OK",command=eror.destroy)
    btn1.grid(column=2,row=3,pady=(10,10),padx=(10,10))
    btn1.focus()
    eror.mainloop()

def sol():
    if var.get()==1:
        ans=int(box1.get()) & int(box2.get())
        return ans
    elif var.get()==2:
        ans=int(box1.get()) | int(box2.get())
        return ans
    elif var.get()==4:
        ans=int(box1.get()) ^ int(box2.get())
        return ans
    elif var.get()==3:
        ans=~(int(box1.get()) ^ int(box2.get()))
        ans=(+ans)
        return ans


def calc():
    if box1.get()=="" or box2.get()=="":
        error(1)   
    elif ((box1.get()).isdigit() and (box2.get()).isdigit())==FALSE:
        error(3)
    elif var.get()==0:
       print(box1.get())
       error(2)
    else:
        x=sol()
        txt3.configure(text="Result Is  =  "+str(x))        
        
def descr():
    if box1.get()=="" or box2.get()=="":
        error(1)   
    elif ((box1.get()).isdigit() and (box2.get()).isdigit())==FALSE:
        error(3)
    elif var.get()==0:
       print(box1.get())
       error(2)
    else:
        b1=(box1.get())
        b2=(box2.get())
        b1=int(b1)
        b2=int(b2)
        b1=bin(b1)
        b2=bin(b2)
        print(b1)
        print(type(b1))
        b1=b1[2:]
        b2=b2[2:]
        if(len(b1)!=len(b2)):
            b=[]
            if len(b1)<len(b2):
                l=list(b1)
                for i in range(len(b2)-len(b1)):
                    b.append("0")
                l=b+l
                b1=''.join(str(i) for i in l)
            else:
                l=list(b2)
                for i in range(len(b1)-len(b2)):
                    b.append("0")
                l=b+l
                b2=''.join(str(i) for i in l)
        li=["AND","OR","XNOR","XOR"]
        desc=Tk()
        desc.title("Details")
        #desc.geometry('520x200')
        txt7=Label(desc,text="Number 1 = "+box1.get(),font=("Arial",12))
        txt7.grid(column=1,row=1,pady=(10,10),padx=(10,10))
        txt8=Label(desc,text="Number 2 = "+box2.get(),font=("Arial",12))
        txt8.grid(column=1,row=2,pady=(10,10),padx=(10,10))
        space=Label(main,text="         ",font=("Arial",10))
        space.grid(column=2,row=1)
        txt9=Label(desc,text="Binary Of Number 1 = "+b1,font=("Arial",12))
        txt9.grid(column=3,row=1,pady=(10,10),padx=(10,10))
        txt0=Label(desc,text="Binary Of Number 2 = "+b2,font=("Arial",12))
        txt0.grid(column=3,row=2,pady=(10,10),padx=(10,10))
        txt11=Label(desc,text="Operation = "+li[int(var.get())-1],font=("Arial",12))
        txt11.grid(column=1,row=3,pady=(10,10),padx=(10,10))
        x=str(sol())
        if int(x)<0:
            bi=bin(int(x))[3:]
            bl=list(bi)
            bl="-"+bi
            bi = ''.join(str(i) for i in bl)
        else:
            bi=bin(int(x))[2:]
        txt21=Label(desc,text="Binary Answer = "+str(bi),font=("Arial",12))
        txt21.grid(column=3,row=3,pady=(10,10),padx=(10,10))
        txt22=Label(desc,text="Decimal Answer = "+x,font=("Arial",12))
        txt22.grid(column=3,row=4,pady=(10,10),padx=(10,10))
        btn1=Button(desc,text="OK",command=desc.destroy)
        btn1.grid(column=2,row=5,pady=(10,10),padx=(10,10))
        btn1.focus()
        desc.mainloop()
main=Tk()
main.title("BitWise Calculator")
var=IntVar()
answer=0
txt1=Label(main,text="Enter First No. = ",font=("Arial",10))
txt1.grid(column=1,row=1,pady=(10,5),padx=(5,0))
box1=Entry(main,width=15)
box1.grid(column=2,row=1,pady=(10,5))
box1.focus()
space=Label(main,text="         ",font=("Arial",10))
space.grid(column=3,row=1)
txt2=Label(main,text="Enter Second No. =",font=("Arial",10))
txt2.grid(row=1,column=4,pady=(10,5))
box2=Entry(main,width=15)
box2.grid(row=1,column=5,padx=(5,10),pady=(10,5))
rad1 = Radiobutton(main,text='AND  ', value=1,variable=var)
rad2 = Radiobutton(main,text='OR  ', value=2,variable=var)
rad3 = Radiobutton(main,text='XNOR', value=3,variable=var)
rad4 = Radiobutton(main,text='XOR', value=4,variable=var)
rad1.grid(row=2, column=2)
rad2.grid(row=2, column=4)
rad3.grid(row=3, column=2,pady=(0,10))
rad4.grid(row=3, column=4,pady=(0,10))
btn1=Button(main,text="Results",command=calc)
btn1.grid(row=4,column=2,pady=(0,10))
btn2=Button(main,text="Details",command=descr)
btn2.grid(row=4,column=4,pady=(0,10))
txt3=Label(main,text="Result Is  =  ",font=("Arial Bold",12))
txt3.grid(row=5,column=3,pady=(0,10),padx=(0,5))
main.mainloop()