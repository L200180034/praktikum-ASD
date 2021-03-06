class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us, lk = []):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        self.listkuliah = lk

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUangSaku):
        self.us = self.us + tambahUangSaku
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, newcity):
        self.kota = newcity
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

    def ambilKuliah(self, ambilkuliah):
        self.listkuliah.append(ambilkuliah)
        
m7 = Mahasiswa('Aisyah', 567, 'Surakarta', 899000)
m8 = Mahasiswa('Goe', 456, 'Karanganyar', 786000)
m9 = Mahasiswa('Vara', 895, 'Jakarta', 25670000)
