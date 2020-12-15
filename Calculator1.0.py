from tkinter import *
from tkinter import messagebox
x =Tk()
x.title("Calculator")
o=""
def q ():
       qq=messagebox.askyesno(title="Quit",message="Do you want to quit?")
       if qq==1:
              x.destroy()
def BtnClick(numbers):
       global o
       o=o + str(numbers)
       y.set(o)
def btnclear():
       global o
       o=""
       y.set("")
def btn():
       global o
       oo=str(eval(o))
       y.set(oo)
       o=""
y=StringVar()
z=Entry(x,font=('arial',20,'bold'),textvariable=y,bd=30,insertwidth=3,bg="powder blue",justify='right').grid(columnspan=4)
b1=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="7",command= lambda:BtnClick(7)).grid(row=2,column=0)
b80=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="8",command= lambda:BtnClick(8)).grid(row=2,column=1)
b2=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="5",command= lambda:BtnClick(5)).grid(row=3,column=1)
b3=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="6",command= lambda:BtnClick(6)).grid(row=3,column=2)
b4=Button(x,padx=16 ,pady=16,bd=8,fg='white',bg="grey",font=('arial',20,'bold'),text="+",command= lambda:BtnClick("+")).grid(row=3,column=3)
b5=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="4",command= lambda:BtnClick(4)).grid(row=3,column=0)
b6=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="3",command= lambda:BtnClick(3)).grid(row=4,column=2)
b7=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="2",command= lambda:BtnClick(2)).grid(row=4,column=1)
b8=Button(x,padx=16 ,pady=16,bd=8,fg='white',bg="grey",font=('arial',20,'bold'),text="-",command= lambda:BtnClick("-")).grid(row=2,column=3)
b9=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="1",command= lambda:BtnClick(1)).grid(row=4,column=0)
b10=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="0",command= lambda:BtnClick(0)).grid(row=5,column=0)
b11=Button(x,padx=16 ,pady=16,bd=8,fg='white',bg="grey",font=('arial',20,'bold'),text="/",command= lambda:BtnClick("/")).grid(row=1,column=1)
b11=Button(x,padx=16 ,pady=16,bd=8,fg='white',bg="grey",font=('arial',20,'bold'),text="+/-",command= lambda:BtnClick("(-")).grid(row=1,column=3)
b12=Button(x,padx=16 ,pady=16,bd=8,fg='white',bg="grey",font=('arial',20,'bold'),text="*",command= lambda:BtnClick("*")).grid(row=1,column=2)
b13=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="light blue",font=('arial',20,'bold'),text="C",command= btnclear).grid(row=1,column=0)
b14=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="orange",font=('arial',20,'bold'),text="=",command= btn).grid(row=4,column=3)
b88=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text=".",command= lambda:BtnClick(".")).grid(row=5,column=1)
b800=Button(x,padx=16 ,pady=16,bd=8,bg='black',fg="white",font=('arial',20,'bold'),text="(",command= lambda:BtnClick("(")).grid(row=5,column=2)
b800=Button(x,padx=16 ,pady=16,bd=8,bg='black',fg="white",font=('arial',20,'bold'),text=")",command= lambda:BtnClick(")")).grid(row=5,column=3)
b12=Button(x,padx=16 ,pady=16,bd=8,fg='black',bg="white",font=('arial',20,'bold'),text="9",command= lambda:BtnClick(9)).grid(row=2,column=2)
M=Menu()
m=Menu()
m.add_command(label="Exit",command=q)
M.add_cascade(label="Exit")
x.mainloop()





