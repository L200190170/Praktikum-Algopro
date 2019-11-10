##Program Akun
##Dibuat oleh Selvianisa L200190170
import random
angka = random.randint(0,1000)

Nama = 'Selvianisa Cahya Mukti'
Tanggallahir = '20 April 2001'
NamaSingkat = Nama[0] + '.' + Nama[11] + '.' + Nama[17:23]
Username = Nama[0] + Tanggallahir[0:2] + Tanggallahir[9:13]
Password = Nama[0:3] + str(angka)

print(Nama)
print(Tanggallahir)
print(NamaSingkat)
print(Username)
print(Password)
