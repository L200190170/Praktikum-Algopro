Python 2.7.8 (default, Jun 30 2014, 16:08:48) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Selvianisa Cahya Mukti'
>>> NIM = 170
>>> Tinggi = 1.49
>>> Berat = 41
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> #Karena Data "Aku" ditulis dengan tanda kurung biasa dan tiap elemennya ditulis dengan tanda koma sebagai pemisah
>>> Aku[0]
2001
>>> #Karena objek pertama dalam data "Aku" adalah "TahunLahir" dan TahunLahir adalah 2001
>>> a = NIM % 4; Aku[a]
1.49
>>> #Karena sisa hasil pembagian data "a" dari 170 dibagi 4 adalah 2. Kemudian hasil data "a" itu dijadikan urutan dalam data "Aku". Jadi hasil dari Aku[a] adalah "Tinggi" yaitu 1.49
>>> type(Aku[a])
<type 'float'>
>>> #Karena data "Aku[a]" merupakan bilangan yang ditulis menggunakan titik desimal
>>> Aku[a:4]
(1.49, 170)
>>> #Karena data "a" adalah 2, sehingga menjadi data "Aku[2:4]". jadi, terjadi slicing dari indeks 2 hingga indeks 3 adalah (1.49, 170)
>>> type(Aku[4])
<type 'str'>
>>> #Karena data "Aku[4]" berupa huruf dan ditulis menggunakan tanda kutip tunggal
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #Karena data Aku bertipe tuple, dan data tuple tidak dapat diubah. Sehingga terjadi Error
>>> type(Data)
<type 'list'>
>>> #Karena ditulis menggunakan kurung siku dan datanya dapat diubah
>>> type(Data[4])
<type 'str'>
>>> #Karena data pada "Data[4]" berupa huruf dan ditulis menggunakan tanda kutip tunggal
>>> Data[4][5]
'a'
>>> #Karena "Data ke-4" berisi objek "Nama" pada indeks 5 adalah 'a'
>>> Data[4][a:6]
'lvia'
>>> #Karena data "a" adalah 2, sehingga menjadi "Data[4][2:6]". Yang terjadi adalah Data ke-4 berisi "Nama" kemudian pada data "Nama" terjadi slicing dari indeks 2 hingga indeks 5. jadi, hasilnya adalah 'lvia'
>>> Data[0] = 'ok'; Data
['ok', 41, 1.49, 170, 'Selvianisa Cahya Mukti']
>>> #Karena mengubah indeks 0 dari "Data" yang awalnya 2001 menjadi 'ok' (dalam bentuk string)
>>> Data[-a]
170
>>> #Karena data "a" adalah 2, sehingga menjadi "Data[-2]". Hasilnya adalah menampilkan objek dengan urutan ke-2 dari belakang yaitu "170"
>>> range(a)
[0, 1]
>>> #Karena data "a" adalah 2, sehingga menjadi "range(a)". Jadi, hanya menampilkan 2 indeks yaitu [0, 1]
