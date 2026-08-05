# ==============================================================================
# Python Nesne Tabanlı Programlama (OOP) - Özel Metodlar (Dunder / Magic Methods)
# ==============================================================================

class Kitap:
    """
    Kitap nesnelerini temsil eden ve özel metodların (dunder methods) 
    kullanımını gösteren sınıf.
    """
    
    def __init__(self, baslik: str, yazar: str, sayfa_sayisi: int):
        """
        Yapıcı (Constructor) Metod:
        Nesne oluşturulduğunda otomatik olarak çalışır.
        """
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self) -> str:
        """
        Kullanıcı Dostu Metin Temsili:
        print(nesne) veya str(nesne) çağrıldığında dönecek metni belirler.
        """
        return f"'{self.baslik}' - {self.yazar} ({self.sayfa_sayisi} sayfa)"

    def __repr__(self) -> str:
        """
        Geliştirici Dostu Metin Temsili:
        Nesnenin teknik / geliştirici odaklı tanımını döndürür.
        """
        return f"Kitap(baslik='{self.baslik}', yazar='{self.yazar}', sayfa_sayisi={self.sayfa_sayisi})"

    def __len__(self) -> int:
        """
        Uzunluk Metodu:
        len(nesne) çağrıldığında çalışan metottur.
        """
        return self.sayfa_sayisi

    def __add__(self, diger_kitap):
        """
        Toplama Operatörü Overloading (+):
        İki Kitap nesnesi '+' ile toplandığında toplam sayfa sayısını döndürür.
        """
        if isinstance(diger_kitap, Kitap):
            return self.sayfa_sayisi + diger_kitap.sayfa_sayisi
        return NotImplemented

    def __eq__(self, diger_kitap) -> bool:
        """
        Eşitlik Operatörü Overloading (==):
        İki kitabın eşit olup olmadığını (sayfa sayılarına göre) kontrol eder.
        """
        if isinstance(diger_kitap, Kitap):
            return self.sayfa_sayisi == diger_kitap.sayfa_sayisi
        return False

    def __del__(self):
        """
        Yıkıcı (Destructor) Metod:
        Nesne bellekten silindiğinde (del nesne) otomatik olarak çalışır.
        """
        print(f"'{self.baslik}' kitabı bellekten silindi.")


# ==============================================================================
# Kullanım / Test Alanı
# ==============================================================================

if __name__ == "__main__":
    # 1. __init__ kullanımı (Nesne Oluşturma)
    kitap1 = Kitap("Suç ve Ceza", "Dostoyevski", 687)
    kitap2 = Kitap("Simyacı", "Paulo Coelho", 184)
    kitap3 = Kitap("Dönüşüm", "Franz Kafka", 184)

    print("--- 1. __str__ ve __repr__ Kullanımı ---")
    print(kitap1)             # __str__ çalışır
    print(repr(kitap1))       # __repr__ çalışır

    print("\n--- 2. __len__ Kullanımı ---")
    print(f"Kitap 1 sayfa sayısı: {len(kitap1)}")  # __len__ çalışır

    print("\n--- 3. __add__ (+ Operatörü) Kullanımı ---")
    toplam_sayfa = kitap1 + kitap2  # __add__ çalışır
    print(f"İki kitabın toplam sayfa sayısı: {toplam_sayfa}")

    print("\n--- 4. __eq__ (== Operatörü) Kullanımı ---")
    print(f"Kitap 2 ve Kitap 3 eşit mi? {kitap2 == kitap3}")  # True
    print(f"Kitap 1 ve Kitap 2 eşit mi? {kitap1 == kitap2}")  # False

    print("\n--- 5. __del__ Kullanımı ---")
    del kitap1  # __del__ çalışır