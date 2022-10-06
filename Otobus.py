class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str=""
    nereden:str=""
    nereye:str=""
    biletsatilan:int=0
    biletiadeedilen:int=0
    dolukoltuk:int=0


    def __init(self,plaka,nereden,nereye,biletsatilan,biletiadeedilen,dolukoltuk):
        """
        plaka otobüs plakası
        nereden güzergah çıkışı
        nereye güzergah varışı
        biletsatilan stilanbilet
        billetiadeedien iadebilet
        dolukoltuk toplam dolu koltuk
        
        """

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
       # otobuskoltuk=20
        #satilanbilet=biletsatilan
        
        #for satilanbilet

        #otobus1=8
        #otobus2=6
        #otobus3=4
        #otobus=10

        dolukoltuk=otobuskoltuk-(satilanbilet-iadeedilen)
        
        return satilanbilet


        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        iadeedilen=biletiadeedilen;

        otobus1=1
        otobus2=1
        otobus3=2
        otobus4=3

    return iadeedilen
        
    dolukoltuk=otobuskoltuk-(satilanbilet-iadeedilen)
    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("plaka:{},nereden:{},nereye:{},dolukoltuk:{}".format(self.plaka,self.nereden,self.nereye,self.dolukoltuk))
