Python 2.7.8 (default, Jun 30 2014, 16:08:48) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Selvianisa Cahya Mukti'
>>> NIM = 'L200190170'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> #Karena data "a" menyimpan data berupa bilangan bulat dan tidak mempunyai titik desimal (dan angka dibelakang koma desimal) dan bukan merupakan angka pecahan
>>> type(b)
<type 'int'>
>>> #Karena data "b" menyimpan data berupa len yang artinya menyimpan banyaknya huruf dalam variabel "Nama"
>>> a / b
53
>>> #karena hasil dari 1170 dibagi dengan 22 adalah 53
>>> a // b
53
>>> #karena arti dari  "//" adalah pembagian dengan pembulatan ke bawah
>>> 10 * (a-999)
1710
>>> #Karena nilai "a " dikurangi 999 adalah 171, setelah itu akan dikalikan dengan 10 dan hasilnya adalah 1710
>>> b ** 2
484
>>> #Karena arti dari  "* * " adalah perpangkatan
>>> a % b
4
>>> #Karena arti dari  "%" adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<type 'float'>
>>> #Karena "12.5" adalah bilangan desimal
>>> a / c
93.6
>>> #karena hasil dari 1170 dibagi dengan 12.5 adalah 93.6
>>> a // c
93.0
>>> #Karena arti dari  "//" adalah pembagian dengan pembulatan ke atas
>>> a % c
7.5
>>> #Karena arti dari  "%" adalah sisa hasil bagi
>>> c > b
False
>>> #Karena merupakan hasil perbandingan antara objek "c" dan "b" sehingga menghasilkan nilai boolean
>>> type(c > b)
<type 'bool'>
>>> #Karena data "c > b" mempunyai dua kemungkinan nilai, yaitu True atau False
>>> a > b and b > c
True
>>> #Karena dalam pengambilan keputusan yang membutuhkan banyak perbandingan (dan setiap perbandingan merupakan nilai True atau False) sehingga termasuk operator logika
>>> #Karena True and True hasilnya adalah True
>>> a > 1100 or b < 10
True
>>> #Karena hasil dari a > 1100 adalah "True" atau hasil dari b < 10 adalah "False" maka hasil perbandingannya adalah True
