class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku


class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    def cariUangsaku(self):
        terkecil = self[0].uangSaku
        for i in self:
            if i.uangSaku < terkecil:
                terkecil = i.uangSaku
        return print(terkecil)


c = buatArray()
c[0] = MhsTIF('Aisyah', 1, 'Karanganyar', 275000)
c[1] = MhsTIF('Goe', 43, 'Yogyakarta', 245000)
c[2] = MhsTIF('Vara', 34, 'Surakarta', 255000)
c[3] = MhsTIF('Septia', 45, 'Semarang', 235000)
c[4] = MhsTIF('Waku', 10, 'Salatiga', 265000)
c[5] = MhsTIF('Fiita', 35, 'Wonogiri', 225000)
c[6] = MhsTIF('Septi', 20, 'Sukoharjo', 285000)
c[7] = MhsTIF('Var', 15, 'Klaten', 250000)
c[8] = MhsTIF('Goev', 12, 'Bekasi', 295000)
c[9] = MhsTIF('Syah', 25, 'Depok', 260000)
c[10] = MhsTIF('Ais', 16, 'Bogor', 270000)
