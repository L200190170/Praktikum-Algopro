from tkinter import *

my_app=Tk()
my_app.title("Bangun Geometri")

L1=Label(my_app, text="Bangun Geometri", font=("Arial", 24))
L1.grid(row=0, column=0, columnspan=2, sticky="W")

L2=Label(my_app, text="Nama")
L2.grid(row=1, column=0, sticky="W")
E2=Label(my_app, text="Balok")
E2.grid(row=1, column=1, sticky="W")

L2=Label(my_app, text="Dimensi")
L2.grid(row=2, column=0, sticky="W")
E2=Label(my_app, text="Bangun Ruang")
E2.grid(row=2, column=1, sticky="W")

L2=Label(my_app, text="Contoh benda")
L2.grid(row=3, column=0, sticky="W")
E2=Label(my_app, text="Kotak Amal")
E2.grid(row=3, column=1, sticky="W")

L2=Label(my_app, text="titik Sudut")
L2.grid(row=4, column=0, sticky="W")
E2=Label(my_app, text="8")
E2.grid(row=4, column=1, sticky="W")

L1=Label(my_app, text="panjang")
L1.grid(row=5, column=0, sticky="W")
panjang=StringVar()
E1=Entry(my_app, textvariable=panjang)
E1.grid(row=5, column=1)

L1=Label(my_app, text="Lebar")
L1.grid(row=6, column=0, sticky="W")
lebar=StringVar()
E2=Entry(my_app, textvariable=lebar)
E2.grid(row=6, column=1)

L3=Label(my_app, text="tinggi")
L3.grid(row=7, column=0, sticky="W")
tinggi=StringVar()
E3=Entry(my_app, textvariable=tinggi)
E3.grid(row=7, column=1)

def hitungLuas():
    a=float(panjang.get())
    b=float(lebar.get())
    c=float(tinggi.get())
    hasil=2*a*b+2*a*c+2*b*c
    Hasil.config(text=hasil)
B1=Button(my_app, text="Hitung Luas", command=hitungLuas)
B1.grid(row=8, column=0, sticky="W")

LabelHasil=Label(my_app, text="Panjang")
LabelHasil.grid(row=5, column=0, sticky="W")
Hasil=Label(my_app, text="0")
Hasil.grid(row=9, column=3)

my_app.mainloop()

