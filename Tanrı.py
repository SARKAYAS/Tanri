class Tanrı():
    tapinmaOrani = 0

    def __init__(self):
        print("Tapınma Oranı Görüntüleniyor")
        print(f"Tapınma Oranı: {self.tapinmaOrani}")

    def tapınmaOraniniYukselt(self, oran):
        self.oran = oran

        if self.tapinmaOrani < 100:
            self.tapinmaOrani += oran
            print(f"Yeni Tapınma Oranı: {self.tapinmaOrani}")
        else:
            print("Tapınma oranı maksimum seviyede. Daha fazla arttıramazsın")

        return self.oran, self.tapinmaOrani

    def Zeus(self, yagmurYagdir, simsekCaktir, gunesActir):
        self.yagmurYagdir = yagmurYagdir
        self.simsekCaktir = simsekCaktir
        self.gunesActir = gunesActir

        print(f"{self.yagmurYagdir} ml yağmur yağdı")
        print(f"{self.simsekCaktir} gücünde şimşek çaktırıldı")
        print(f"Güneş {gunesActir} parlaklık gücünde güneş açıldı")
        return self.yagmurYagdir, self.simsekCaktir, self.gunesActir

    def Poseidon(self, depremOlustur, tsunamiYap, sorfDalgasiYap):
        self.depremOlustur = depremOlustur
        self.tsunamiYap = tsunamiYap
        self.sorfDalgasiYap = sorfDalgasiYap

        if self.depremOlustur > 0:
            print(f"{self.depremOlustur} şiddetinde deprem oluşturuldu")
        else:
            print("Deprem oluşturalamadı.0 veya üstü değer giriniz")
        if self.tsunamiYap > 0:
            print(f"{self.tsunamiYap} şiddetinde tsunami oluşturuldu")
        else:
            print("Tsunami oluşturalamadı. 0 veya üstü değer giriniz")
        if self.sorfDalgasiYap > 0:
            print(f"{self.sorfDalgasiYap} cm yüksekliğinde sörf dalgası oluşturuldu ")
        else:
            print("Sörf dalgası oluşturulamadı. 0 veya üstü değer giriniz")

        return self.sorfDalgasiYap, self.tsunamiYap, self.depremOlustur