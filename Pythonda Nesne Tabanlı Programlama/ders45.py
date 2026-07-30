#=======================================
# PYTHON NESNE TABANLI PROGRAMLAMA (OOP)
# DERS 2:
#=======================================

class BankaHesabi:

    def __init__(self, ad, bakiye):
        self.ad = ad
        self.bakiye = bakiye

    # Hesap bilgilerini gösteren metot
    def hesap_bilgisi(self):
        print("\n----- HESAP BİLGİLERİ -----")
        print(f"Hesap Sahibi : {self.ad}")
        print(f"Bakiye       : {self.bakiye} TL")

    # Para yatırma metodu
    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"\n{miktar} TL hesabınıza yatırıldı.")

    # Para çekme metodu
    def para_cek(self, miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"\n{miktar} TL hesabınızdan çekildi.")
        else:
            print("\nYetersiz bakiye!")




hesap = BankaHesabi("Özgür Kavak", 5000)

hesap.hesap_bilgisi()

hesap.para_yatir(1500)
hesap.hesap_bilgisi()

hesap.para_cek(2000)
hesap.hesap_bilgisi()

hesap.para_cek(6000)
            
















