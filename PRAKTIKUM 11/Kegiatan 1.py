from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox

my_app = Tk(className="Aplikasi Data Diri")
L1 = Label(my_app, text="Data Diri", font=("Arial", 24))
L1.grid(row=0, column=0, sticky="W")

L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0, sticky="W")
L2 = Label(my_app, text="Selvianisa Cahya Mukti")
L2.grid(row=1, column=1, sticky="W")

L3 = Label(my_app, text="NIM")
L3.grid(row=2, column=0, sticky="W")
L3 = Label(my_app, text="L200190170")
L3.grid(row=2, column=1, sticky="W")

L4 = Label(my_app, text="Buku Favorite")
L4.grid(row=3, column=0, sticky="W")
L4 = Label(my_app, text="Mantappu Jiwa")
L4.grid(row=3, column=1, sticky="W")

L5 = Label(my_app, text="Idola Kalangan Sahabat")
L5.grid(row=4, column=0, sticky="W")
L5 = Label(my_app, text="Ali Bin Abi Thalib")
L5.grid(row=4, column=1, sticky="W")

L6 = Label(my_app, text="Motto")
L6.grid(row=5, column=0, sticky="W")
L6 = Label(my_app, text="Teruslah Berjuang Tanpa Rasa Mengeluh")
L6.grid(row=5, column=1, sticky="W")

def tutup():
    my_app.destroy()

B = Button(my_app, text="tutup", command=tutup)
B.grid(row=6, column=0)
my_app.mainloop()
