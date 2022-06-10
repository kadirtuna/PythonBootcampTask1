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
        return f"{self.ad} türünden bu canlının özellikleri şunlardır;\nSınıfı : {self.sınıf}\nHareket Kabiliyeti : {self.hareketKabiliyeti}\nBeslenme şekli : {self.beslenme}\nSolunum Şekli : {self.solunum}\nÜreme Şekli : {self.üreme}\nOrtalama Ölüm Yaşı : {self.ölüm}\n\n"


class Hayvanlar(Canlılar):
    hareketKabiliyeti = True  # A noktasından B noktasına hareket edebilme özelliği
    sınıf = "Hayvan"

    def __init__(self, tür, beslenme, solunum, üreme, ölüm):
        Hayvanlar.beslenmeControl(self, beslenme)
        Hayvanlar.solunumControl(self, solunum)
        super().__init__(tür, Hayvanlar.sınıf, Hayvanlar.hareketKabiliyeti, beslenme, solunum, üreme, ölüm)

    def beslenmeControl(self, beslenme):
        while 1:
            if beslenme == "Etçil":
                break
            elif beslenme == "Otçul":
                break
            elif beslenme == "Hepçil":
                break
            else:
                beslenme = input(
                    f"Beslenmeyi \"{beslenme}\" olarak girdin.\nBir canlının beslenme şekli sadece \"Etçil\", \"Otçul\"veya \"Hepçil\" olabilir. Beslenme şeklini tekrar giriniz : ")

    def solunumControl(self, solunum):
        solunumCesitleri = ["Deri", "Solungaç", "Trake", "Akciğer"]
        while 1:
            if solunum in solunumCesitleri:
                break
            else:
                print(f"Solunum \"{solunum}\" olarak girdin.\nBir canlının solunum şekli sadece")
                for index, i in enumerate(solunumCesitleri):
                    print(f"#{index + 1} - {i}")
                solunum = input("olabilir. Solunum şeklini tekrar harflerle yazarak giriniz : ")

    def üremeControl(self, üreme):
        üremeCesitleri = ["Eşeyli", "Eşeysiz"]
        while 1:
            if üreme in üremeCesitleri:
                break
            else:
                print(f"Üreme'yi \"{üreme}\" olarak girdin.\nBir canlının üreme şekli sadece")
                for index, i in enumerate(üremeCesitleri):
                    print(f"#{index + 1} - {i}")
                üreme = input("olabilir. Üreme şeklini tekrar harflerle yazarak giriniz : ")


class Bitkiler(Canlılar):
    sınıf = "Bitki"
    hareketKabiliyeti = False
    solunum = "Fotosentez"
    beslenme = "Toprak"

    def __init__(self, tür, üreme, ölüm):
        Bitkiler.üremeControl(self, üreme)
        super().__init__(tür, Bitkiler.sınıf, Bitkiler.hareketKabiliyeti, Bitkiler.beslenme, Bitkiler.solunum, üreme,
                         ölüm)

    def üremeControl(self, üreme):
        üremeCesitleri = ["Vejetatif", "Sporla", "Bölünerek", "Tomurcuklanarak", "Yenilenerek"]
        while 1:
            if üreme in üremeCesitleri:
                break
            else:
                print(f"Üreme'yi \"{üreme}\" olarak girdin.\nBir canlının üreme şekli sadece")
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
