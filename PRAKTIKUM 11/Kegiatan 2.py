from tkinter import Tk, Label, Entry, Button
from tkinter import *

kalkulator = Tk(className="Kalkulator Sederhana")
L1 = Label(kalkulator, text="Angka 1")
L1.grid(row=0, column=0)
angka1 = StringVar()
E1 = Entry(kalkulator, textvariable=angka1)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(kalkulator, text="Angka 2")
L2.grid(row=1, column=0)
angka2 = StringVar()
E2 = Entry(kalkulator, textvariable=angka2)
E2.grid(row=1, column=1, columnspan=3)

def tambah():
    a=float(angka1.get())
    b=float(angka2.get())
    hasil=a+b
    Hasil.config(text=hasil)
B1 = Button(kalkulator, text="+", command=tambah)
B1.grid(row=2, column=0)

def kurang():
    a=float(angka1.get())
    b=float(angka2.get())
    hasil=a-b
    Hasil.config(text=hasil)
B2 = Button(kalkulator, text="-", command=kurang)
B2.grid(row=2, column=1)

def kali():
    a=float(angka1.get())
    b=float(angka2.get())
    hasil=a*b
    Hasil.config(text=hasil)
B3 = Button(kalkulator, text="x", command=kali)
B3.grid(row=2, column=2)

def bagi():
    a=float(angka1.get())
    b=float(angka2.get())
    hasil=a/b
    Hasil.config(text=hasil)
B4 = Button(kalkulator, text=":", command=bagi)
B4.grid(row=2, column=3)

Labelhasil=Label(kalkulator, text="Hasil")
Labelhasil.grid(row=3, column=0)
Hasil=Label(kalkulator, text="0")
Hasil.grid(row=3, column=3)

kalkulator.mainloop()
