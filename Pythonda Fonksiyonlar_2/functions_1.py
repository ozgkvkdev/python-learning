# İÇ İÇE FONKSİYON KULLANIMI #

def sifre_kontrol(sifre):

    def uzunluk_kontrolu():
        return len(sifre) >= 8

    def rakam_kontrolu():
        return any(harf.isdigit() for harf in sifre)

    def buyuk_harf_kontrolu():
        return any(harf.isupper() for harf in sifre)

    if uzunluk_kontrolu() and rakam_kontrolu() and buyuk_harf_kontrolu():
        print("Şifre güçlü.")
    else:
        print("Şifre yeterince güçlü değil.")


sifre = input("Şifrenizi girin: ")

sifre_kontrol(sifre)