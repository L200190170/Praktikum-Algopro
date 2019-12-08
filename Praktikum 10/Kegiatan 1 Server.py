import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Program Komunikasi Tentang Data Diri"
data = ""
kamus = {"nama":"Selvianisa Cahya Mukti",
         "NIM":"L200190170",
         "angkatan":"2019",
         "keluar":"Siap!"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Perintah:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, Perintah Tidak Dimengerti")
