from tkinter import *


def plus():
  value1 = entry1.get()
  value2 = entry2.get()
  sum = int(value1) + int(value2)
  result.config(text=str(sum))


def minus():
  value1 = entry1.get()
  value2 = entry2.get()
  res = int(value1) - int(value2)
  result.config(text=str(res))

def multiply():
  value1 = entry1.get()
  value2 = entry2.get()
  res = int(value1) * int(value2)
  result.config(text=str(res))

def divid():
  value1 = entry1.get()
  value2 = entry2.get()
  res = int(value1) / int(value2)
  result.config(text=str(res))

# design:
w = Tk()
w.title("Calcutor app")
w.geometry("1000x600")
Title = Label(text="Calculator App",font=("Arial",28,"bold"))
# first_value = Label(text="value 1: ",font=("Arial",28,"bold"))
# second_value = Label(text="value 2: ",font=("Arial",28,"bold"))
#images
plusimg=PhotoImage(file="Asset 1.png")
minusimg=PhotoImage(file="Asset 3.png")
divideimg=PhotoImage(file="Asset 4.png")
multiplyimg=PhotoImage(file="Asset 5.png")

# text Entery

entry1 = Entry(w,width=20,font=("Arial",28,"bold"))
entry2 = Entry(w,width=20,font=("Arial",28,"bold"))

# add buttons

plusbtn = Button(image=plusimg, command=plus)
minusbtn = Button(image=minusimg, command=minus)
multbtn = Button(image=multiplyimg, command=multiply)
dividbtn = Button(image=divideimg, command=divid)
# result label

result = Label(text="0000",font=("Arial",28,"bold"))
# Elements positioning

Title.place(x=430,y=10)
first_value.place(x=191,y=72)
second_value.place(x=191,y=178)
entry1.place(x=341,y=72)
entry2.place(x=341,y=178)
plusbtn.place(x=207,y=291)
minusbtn.place(x=350,y=291)
multbtn.place(x=493,y=291)
dividbtn.place(x=637,y=291)
result.place(x=393,y=401)
w.mainloop()
