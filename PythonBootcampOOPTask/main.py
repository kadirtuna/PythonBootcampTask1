import organisms as pyOrg

boncuk = pyOrg.Omurgalılar("Kedi", "Etçil", "Akciğer", 15)
max = pyOrg.Omurgalılar("Köpek", "Hepçil", "Akciğer", 10)
doru = pyOrg.Omurgalılar("At", "Otçul", "Akciğer", 25)
denizYıldızı = pyOrg.Omurgasızlar("Deniz Yıldızı", "Etçil", "Solungaç", "Eşeyli", 35)
ahtapot = pyOrg.Omurgasızlar("Ahtapot", "Etçil", "Solungaç", "Eşeyli", 5)
lale = pyOrg.ÇiçekliBitkiler("Lale", "Vejetatif", 0.5)
menekşe = pyOrg.ÇiçekliBitkiler("Menekşe", "Vejetatif", 0.5)
eğreltiOtu = pyOrg.ÇiçeksizBitkiler("Eğrelti Otu", 1)
suYosunu = pyOrg.ÇiçeksizBitkiler("Su Yosunu", 1)
liken = pyOrg.ÇiçeksizBitkiler("Liken", 1)

hayvanlar = [boncuk, max, doru, denizYıldızı, ahtapot]
bitkiler = [lale, menekşe, eğreltiOtu, suYosunu, liken]


while 1:
    print("\n\n---------------MENU------------------\n"
          "1 - Hayvanlar listesinin içindeki elemanların bilgilerini yazdır.\n"
          "2 - Bitkiler listesinin içindeki elemanların bilgilerini yazdır.\n"
          "3 - Hayvanlar listesine yeni eleman ekle.\n"
          "4 - Bitkiler listesine yeni eleman ekle.\n")
    operation = input("Yapmak istediğiniz işlemin numarasını yazınız (Çıkış için \"q\" yazın) : ")

    if operation == "1":
        [print(f"{index + 1}. Canlı {hayvan.bilgileriniYazdır()}")  for index, hayvan in enumerate(hayvanlar)]

    elif operation == "2":
        [print(f"{index + 1}. Canlı {bitki.bilgileriniYazdır()}") for index, bitki in enumerate(bitkiler)]

    elif operation == "3":
        print("1 - Omurgalı hayvan.\n"
              "2 - Omurgasız hayvan.\n")
        hayvanTürü = input("İstediğiniz seçeneğin numarasını giriniz : ")
        if hayvanTürü == "1":
            tür = input("Türünü giriniz : ")
            beslenme = input("Beslenme çeşidini giriniz! (Etçil, Otçul, Hepçil) : ")
            solunum = input("Solunum çeşidini giriniz! (Deri, Solungaç, Trake, Akciğer) : ")
            ölüm = input("Ortalama ömrünü giriniz : ")
            obj1 = pyOrg.Omurgalılar(tür, beslenme, solunum, ölüm)
            hayvanlar.append(obj1)
            print("Omurgalı Hayvan başarıyla hayvanlar listesine eklendi!")
    elif operation == "3":
        print("")
    elif operation == "q":
        break



# for index, hayvan in enumerate(hayvanlar):
#     print(f"{index + 1}. Hayvan;")
#     hayvan.bilgileriniYazdır()
#
# for index, bitki in enumerate(bitkiler):
#     print(f"{index + 1}. Bitki;")
#     bitki.bilgileriniYazdır()

