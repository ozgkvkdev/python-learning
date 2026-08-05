# ==============================================================================
# Python Konsol Quiz Uygulaması
# OOP Prensipleri ile Modüler Tasarım
# ==============================================================================

class Soru:
    """
    Tek bir soruyu, şıklarını ve doğru cevabını temsil eden sınıf.
    """
    def __init__(self, metin: str, secenekler: list[str], cevap: str):
        self.metin = metin
        self.secenekler = secenekler
        self.cevap = cevap.upper()

    def cevabi_kontrol_et(self, kullanici_cevabi: str) -> bool:
        """Kullanıcının verdiği cevabın doğruluğunu kontrol eder."""
        return self.cevap == kullanici_cevabi.upper().strip()


class Quiz:
    """
    Soruları yöneten, skoru tutan ve testi çalıştıran ana sınıf.
    """
    def __init__(self, sorular: list[Soru]):
        self.sorular = sorular
        self.skor = 0
        self.soru_indeksi = 0

    def soruyu_getir() -> Soru:
        """Mevcut indeksteki soruyu döndürür."""
        return self.sorular[self.soru_indeksi]

    def soruyu_goster(self):
        """Mevcut soruyu ve şıklarını ekrana düzenli bir formatta basar."""
        soru = self.sorular[self.soru_indeksi]
        print(f"\nSoru {self.soru_indeksi + 1} / {len(self.sorular)}:")
        print(f"-> {soru.metin}")
        
        for secenek in soru.secenekler:
            print(f"   {secenek}")

    def quizi_baslat(self):
        """Quiz döngüsünü başlatır ve soruları sırayla sorar."""
        print("=" * 50)
        print("          PYTHON QUIZ UYGULAMASINA HOŞ GELDİNİZ          ")
        print("=" * 50)

        for soru in self.sorular:
            self.soruyu_goster()
            
            # Geçerli bir şık girilene kadar girdi alır
            while True:
                girdi = input("\nCevabınız (A/B/C/D): ").upper().strip()
                if girdi in ["A", "B", "C", "D"]:
                    break
                print("Lütfen sadece A, B, C veya D şıklarından birini giriniz.")

            if soru.cevabi_kontrol_et(girdi):
                print(">> Doğru Cevap! (+10 Puan)")
                self.skor += 10
            else:
                print(f">> Yanlış Cevap! Doğru cevap: {soru.cevap}")

            self.soru_indeksi += 1

        self.sonucu_goster()

    def sonucu_goster(self):
        """Quiz bittiğinde toplam skoru ve başarı durumunu ekrana basar."""
        toplam_soru = len(self.sorular)
        maksimum_skor = toplam_soru * 10
        basari_yuzdesi = (self.skor / maksimum_skor) * 100

        print("\n" + "=" * 50)
        print("                   QUIZ TAMAMLANDI                   ")
        print("=" * 50)
        print(f"Toplam Soru Sayısı : {toplam_soru}")
        print(f"Toplam Puanınız    : {self.skor} / {maksimum_skor}")
        print(f"Başarı Yüzdeniz    : %{basari_yuzdesi:.1f}")
        
        if basari_yuzdesi >= 70:
            print("Tebrikler! Harika bir sonuç.")
        else:
            print("Biraz daha pratik yapmalısın.")
        print("=" * 50)


# ==============================================================================
# Soru Havuzu ve Uygulama Çalıştırma
# ==============================================================================

if __name__ == "__main__":
    # Soru nesnelerinden oluşan liste
    soru_bankasi = [
        Soru(
            "Python'da ekrana yazı yazdırmak için hangi fonksiyon kullanılır?",
            ["A) echo()", "B) print()", "C) write()", "D) console.log()"],
            "B"
        ),
        Soru(
            "Hangisi Python'da değiştirilemez (immutable) bir veri tipidir?",
            ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
            "C"
        ),
        Soru(
            "OOP'de bir sınıfın özelliklerini başka bir sınıfa devretmesine ne ad verilir?",
            ["A) Polymorphism", "B) Encapsulation", "C) Abstraction", "D) Inheritance"],
            "D"
        ),
        Soru(
            "Python'da yapııcı (constructor) metodun adı nedir?",
            ["A) __init__", "B) __start__", "C) __create__", "D) __main__"],
            "A"
        )
    ]

    # Quiz örneği oluşturulur ve başlatılır
    quiz_app = Quiz(soru_bankasi)
    quiz_app.quizi_baslat()