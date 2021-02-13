class Sinif:
    def __init__(self, kod, erkekSayisi, kizSayisi, panoSayisi):
        self.kod = kod
        self.erkekSayisi = erkekSayisi
        self.kizSayisi = kizSayisi
        self.panoSayisi = panoSayisi

class Ogretmen:
    def __init__(self, isim, yas, uzmanlik, rehberlik_sinifi, maas):
        if isinstance(rehberlik_sinifi, Sinif):
            self.isim = isim
            self.yas = yas
            self.uzmanlik = uzmanlik
            self.rehberlik_sinifi = rehberlik_sinifi
            self.maas = maas
        else:
            print("Verilen parametre -rehberlik_sinifi-, 'Sinif' tipinde degil!")

class Ogrenci:
    def __init__(self, isim, yas, sinif, okulno):
        if isinstance(sinif, Sinif):
            self.isim = isim
            self.sinif = sinif
            self.yas = yas
            self.okulno = okulno
        else:
            print("Verilen parametre -sinif-, 'Sinif' tipinde degil!")

class Calisan:
    def __init__(self, isim, yas, mezun_oldugu_bolum, yaptigi_is, maas):
        self.isim = isim
        self.yas = yas
        self.mezun_oldugu_bolum = mezun_oldugu_bolum
        self.yaptigi_is = yaptigi_is
        self.maas = maas

class Okul:
    def __init__(self):
        self.__ogretmenler = []
        self.__ogrenciler = []
        self.__calisanlar = []

    def ogretmenEkle(self, ogretmen):
        if isinstance(ogretmen, Ogretmen):
            self.__ogretmenler.append(ogretmen)
        else:
            print("Verilen parametre 'Ogretmen' tipinde degil!")

    def ogrenciEkle(self, ogrenci):
        if isinstance(ogrenci, Ogrenci):
            self.__ogrenciler.append(ogrenci)
        else:
            print("Verilen parametre 'Ogrenci' tipinde degil!")
    
    def calisanEkle(self, calisan):
        if isinstance(calisan, Calisan):
            self.__calisanlar.append(calisan)
        else:
            print("Verilen parametre 'Calisan' tipinde degil!")   

    def ogretmenleriGoster(self):
        for ogretmen in self.__ogretmenler:
            print("------------------")
            print(f"Ogretmenin adi: {ogretmen.isim}\nOgretmenin yasi: {ogretmen.yas}\nOgretmenin uzmanligi: {ogretmen.uzmanlik}\nOgretmenin maasi: {ogretmen.maas}")
            print(f"Ogretmenin sinifinin kodu: {ogretmen.rehberlik_sinifi.kod}\nOgretmenin sinifinin erkek sayisi: {ogretmen.rehberlik_sinifi.erkekSayisi}\nOgretmenin sinifinin kiz sayisi: {ogretmen.rehberlik_sinifi.kizSayisi}\nOgretmenin sinifinin pano sayisi: {ogretmen.rehberlik_sinifi.panoSayisi}")
            print("------------------")

    def ogrencileriGoster(self):
        for ogrenci in self.__ogrenciler:
            print("------------------")
            print(f"Ogrencinin adi: {ogrenci.isim}\nOgrencinin yasi: {ogrenci.yas}\nOgrencinin numarasi: {ogrenci.okulno}")
            print(f"Ogrencinin sinifinin kodu: {ogrenci.sinif.kod}\nOgrencinin sinifinin erkek sayisi: {ogrenci.sinif.erkekSayisi}\nOgrencinin sinifinin kiz sayisi: {ogrenci.sinif.kizSayisi}\nOgrencinin sinifinin pano sayisi: {ogrenci.sinif.panoSayisi}")
            print("------------------")

    def calisanlariGoster(self):
        for calisan in self.__calisanlar:
            print("------------------")
            print(f"Calisanin adi: {calisan.isim}\nCalisanin yasi: {calisan.yas}\nCalisanin mezun oldugu bolum: {calisan.mezun_oldugu_bolum}\nCalisanin isi: {calisan.yaptigi_is}\nCalisanin maasi: {calisan.maas}")
            print("------------------")

    def ogretmenleriAl(self):
        return self.__ogretmenler
    
    def ogrencileriAl(self):
        return self.__ogrenciler
    
    def calisanlariAl(self):
        return self.__calisanlar

okul1 = Okul()
okul1.ogretmenEkle(Ogretmen("Selahattin Ali", 41, "Edebiyat", Sinif("6-A", 28, 0, 2), 3000))
okul1.ogretmenEkle(Ogretmen("Aziz Nesin", 63, "Matematik", Sinif("8-D", 14, 28, 4), 2700))
okul1.ogretmenEkle(Ogretmen("Abdulgani Sancar", 74, "Biyoloji", Sinif("7-B", 20, 20, 3), 3200))

okul1.ogrenciEkle(Ogrenci("Sabahattin Ali", 13, Sinif("6-A", 28, 0, 2), 1029))
okul1.ogrenciEkle(Ogrenci("Ali Nesin", 15, Sinif("8-D", 14, 28, 4), 1030))
okul1.ogrenciEkle(Ogrenci("Aziz Sancar", 14, Sinif("7-B", 20, 20, 3), 1031))

okul1.calisanEkle(Calisan("Fatih Kulaber", 28, "Bilgisayar Muhendisligi", "Hademe", 1000))
okul1.calisanEkle(Calisan("Meltem Onat Polat", 26, "Mimarlik", "Hademe", 1000))
okul1.calisanEkle(Calisan("Aristotales", 32, "Felsefe", "Hademe", 1000))

okul2 = Okul()
okul2.ogretmenEkle(Ogretmen("Moritz Zweig", 45, "Edebiyat", Sinif("10-H", 19, 10, 1), 2500))
okul2.ogretmenEkle(Ogretmen("Earl Little", 53, "Kimya", Sinif("11-B", 10, 22, 2), 3100))
okul2.ogretmenEkle(Ogretmen("Adolf Hitler", 29, "Politika", Sinif("9-U", 100, 100, 25), 12000))

okul2.ogrenciEkle(Ogrenci("Stefan Zweig", 17, Sinif("10-H", 19, 10, 1), 803))
okul2.ogrenciEkle(Ogrenci("Malcolm Little", 18, Sinif("11-B", 10, 22, 2), 804))
okul2.ogrenciEkle(Ogrenci("Alois Hitler", 16, Sinif("9-U", 100, 100, 25), 805))

okul2.calisanEkle(Calisan("Mehmet Yagci", 34, "Yok", "Hademe", 1000))
okul2.calisanEkle(Calisan("Ihsan Bunak", 40, "Edebiyat", "Hademe", 1000))
okul2.calisanEkle(Calisan("Merve Tanrikulu", 31, "Yok", "Hademe", 1000))

okul3 = Okul()
okul3.ogretmenEkle(Ogretmen("Recep Tayyip Piskin", 29, "Hayat Bilgisi", Sinif("2-D", 15, 10, 2), 2950))
okul3.ogretmenEkle(Ogretmen("Kim Kardashian", 37, "Cografya", Sinif("10-I", 12, 12, 0), 3500))
okul3.ogretmenEkle(Ogretmen("Mehmet Paker", 39, "Muzik", Sinif("5-G", 15, 7, 1), 3005))

okul3.ogrenciEkle(Ogrenci("Erkan Vural", 9, Sinif("2-D", 15, 10, 2), 407))
okul3.ogrenciEkle(Ogrenci("Murat Bilgisiz", 17, Sinif("10-I", 12, 12, 0), 408))
okul3.ogrenciEkle(Ogrenci("Melike Insafsiz", 12, Sinif("5-G", 15, 7, 1), 409))

okul3.calisanEkle(Calisan("Orkun Isildak", 38, "Reklamcilik", "Hademe", 1000))
okul3.calisanEkle(Calisan("Enes Latur", 27, "Tiyatro", "Hademe", 1000))
okul3.calisanEkle(Calisan("Ruhicen Et", 33, "Bilgisayar Muhendisligi", "Hademe", 1000))

print("Okul 1")
okul1.ogretmenleriGoster()
okul1.ogrencileriGoster()
okul1.calisanlariGoster()

print("Okul 2")
okul2.ogretmenleriGoster()
okul2.ogrencileriGoster()
okul2.calisanlariGoster()

print("Okul 3")
okul3.ogretmenleriGoster()
okul3.ogrencileriGoster()
okul3.calisanlariGoster()