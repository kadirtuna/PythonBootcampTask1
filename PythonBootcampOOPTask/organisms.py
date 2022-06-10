class Canlılar():
    def __init__(self, ad, sınıf, hareketKabiliyeti, beslenme, solunum, üreme, ölüm):
        self.ad = ad
        self.sınıf = sınıf
        self.hareketKabiliyeti = "Var" if hareketKabiliyeti == True else "Yok"
        self.beslenme = beslenme
        self.solunum = solunum
        self.üreme = üreme
        self.ölüm = ölüm

    def bilgileriniYazdır(self):
        return f"\n{self.ad} türünden bu canlının özellikleri şunlardır;\nSınıfı : {self.sınıf}\nHareket Kabiliyeti : {self.hareketKabiliyeti}\nBeslenme şekli : {self.beslenme}\nSolunum Şekli : {self.solunum}\nÜreme Şekli : {self.üreme}\nOrtalama Ölüm Yaşı : {self.ölüm}\n\n"


class Hayvanlar(Canlılar):
    hareketKabiliyeti = True  # A noktasından B noktasına hareket edebilme özelliği
    sınıf = "Hayvan"

    def __init__(self, tür, beslenme, solunum, üreme, ölüm):
        beslenme = Hayvanlar.beslenmeControl(self, beslenme)
        solunum = Hayvanlar.solunumControl(self, solunum)
        üreme = Hayvanlar.hayvanlarÜremeKontrol(self, üreme)
        super().__init__(tür, Hayvanlar.sınıf, Hayvanlar.hareketKabiliyeti, beslenme, solunum, üreme, ölüm)

    def beslenmeControl(self, beslenme):
        while 1:
            beslenmeCesitleri = ["Etçil", "Otçul", "Hepçil"]
            if beslenme in beslenmeCesitleri:
                return beslenme
            else:
                beslenme = input(f"\nBeslenmeyi \"{beslenme}\" olarak girdin.\nBir canlının beslenme şekli sadece \"Etçil\", \"Otçul\"veya \"Hepçil\" olabilir. Beslenme şeklini tekrar giriniz : ")

    def solunumControl(self, solunum):
        solunumCesitleri = ["Deri", "Solungaç", "Trake", "Akciğer"]
        while 1:
            if solunum in solunumCesitleri:
                return solunum
            else:
                print(f"\nSolunum \"{solunum}\" olarak girdin.\nBir canlının solunum şekli sadece")
                for index, i in enumerate(solunumCesitleri):
                    print(f"#{index + 1} - {i}")
                solunum = input("olabilir. Solunum şeklini tekrar harflerle yazarak giriniz : ")

    def hayvanlarÜremeKontrol(self, üreme):
        üremeCesitleri = ["Eşeyli", "Eşeysiz"]
        while 1:
            if üreme in üremeCesitleri:
                return üreme
            else:
                print(f"\nÜreme'yi \"{üreme}\" olarak girdin.\nBir canlının üreme şekli sadece")
                for index, i in enumerate(üremeCesitleri):
                    print(f"#{index + 1} - {i}")
                üreme = input("olabilir. Üreme şeklini tekrar harflerle yazarak giriniz : ")


class Bitkiler(Canlılar):
    sınıf = "Bitki"
    hareketKabiliyeti = False
    solunum = "Fotosentez"
    beslenme = "Toprak"

    def __init__(self, tür, üreme, ölüm):
        üreme = Bitkiler.bitkilerÜremeKontrol(self, üreme)
        super().__init__(tür, Bitkiler.sınıf, Bitkiler.hareketKabiliyeti, Bitkiler.beslenme, Bitkiler.solunum, üreme,
                         ölüm)

    def bitkilerÜremeKontrol(self, üreme):
        üremeCesitleri = ["Vejetatif", "Sporla", "Bölünerek", "Tomurcuklanarak", "Yenilenerek"]
        while 1:
            if üreme in üremeCesitleri:
                return üreme
            else:
                print(f"\nÜreme'yi \"{üreme}\" olarak girdin.\nBir canlının üreme şekli sadece")
                for index, i in enumerate(üremeCesitleri):
                    print(f"#{index + 1} - {i}")
                üreme = input("olabilir. Üreme şeklini tekrar harflerle yazarak giriniz : ")


class Omurgalılar(Hayvanlar):  # Hayvanlar sınıfından Omurgalı Hayvanlar alt sınıfı
    üreme = "Eşeyli"

    def __init__(self, tür, beslenme, solunum, ölüm):
        super().__init__(tür, beslenme, solunum, Omurgalılar.üreme, ölüm)


class Omurgasızlar(Hayvanlar):  # Hayvanlar sınıfından Omurgasız Hayvanlar alt sınıfı
    def __init__(self, tür, beslenme, solunum, üreme, ölüm):
        super().__init__(tür, beslenme, solunum, üreme, ölüm)


class ÇiçekliBitkiler(Bitkiler):  # Hayvanlar sınıfından Omurgalı Hayvanlar alt sınıfı
    def __init__(self, tür, üreme, ölüm):
        super().__init__(tür, üreme, ölüm)


class ÇiçeksizBitkiler(Bitkiler):  # Hayvanlar sınıfından Omurgasız Hayvanlar alt sınıfı
    üreme = "Sporla"

    def __init__(self, tür, ölüm):
        super().__init__(tür, ÇiçeksizBitkiler.üreme, ölüm)
