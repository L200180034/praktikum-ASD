class Mahasiswa(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    def katakanPy(self):
        print('Python is cool.')
        
listan = [MhsTIF ('Vara',34,'Surakarta', 255000),
MhsTIF('Aisyah',42,'Wonosobo', 255000),
MhsTIF('Goe',15,'Yogyakarta', 155000),
MhsTIF('Septia',26,'Semarang', 175000),
MhsTIF('Waku',18,'Lembang', 200000),
MhsTIF('Fiita',31,'Magelang', 980000),
MhsTIF('Septin',10,'Tegal', 265000),
MhsTIF('Iqbal',45,'Kutoarjo', 185000),
MhsTIF('Justin',11,'Bekasi', 245000),
MhsTIF('Febrian',21,'Depok', 235000),
MhsTIF('Rio',18,'Bogor', 195000)]

#1
def urutkannim(l):
    n = len(l)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if l[k].nim > l[k+1].nim :
                swap(l,k,k+1)

def checknim (l):
    for i in l :
        print (i.nim)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp
