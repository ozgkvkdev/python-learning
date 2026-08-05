# ==============================================================================
# Python Nesne Tabanlı Programlama (OOP) - Kalıtım (Inheritance) Örneği
# ==============================================================================

class Calisan:
    """
    Ana Sınıf (Parent / Base Class)
    Tüm çalışanlar için ortak olan temel özellikleri ve davranışları barındırır.
    """
    def __init__(self, isim: str, maas: float, departman: str):
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        """Çalışanın temel bilgilerini ekrana yazdırır."""
        print(f"İsim: {self.isim} | Departman: {self.departman} | Maaş: {self.maas} TL")

    def zam_yap(self, oran: float):
        """Mevcut maaşa belirtilen oranda zam uygular."""
        self.maas += self.maas * (oran / 100)
        print(f"{self.isim} için %{oran} zam yapıldı. Yeni Maaş: {self.maas} TL")


class Yonetici(Calisan):
    """
    Türetilmiş Sınıf (Child / Derived Class)
    'Calisan' sınıfından türetilmiştir. Onun tüm özelliklerini devralır,
    ek olarak kendine ait özellikler barındırır.
    """
    def __init__(self, isim: str, maas: float, departman: str, sorumlu_kisi_sayisi: int):
        # super() kullanarak Ana Sınıfın (Calisan) __init__ metodunu çağırıyoruz.
        # Bu sayede isim, maas ve departman atamalarını tekrar yazmamıza gerek kalmaz.
        super().__init__(isim, maas, departman)
        self.sorumlu_kisi_sayisi = sorumlu_kisi_sayisi

    def bilgileri_goster(self):
        """
        Metot Ezme (Method Overriding):
        Ana sınıftaki 'bilgileri_goster' metodunu ezerek Yöneticiye özel 
        ekstra bilgileri de ekrana basacak şekilde güncelliyoruz.
        """
        super().bilgileri_goster()  # Temel bilgileri yazdırır
        print(f"Sorumlu Olduğu Kişi Sayısı: {self.sorumlu_kisi_sayisi}")

    def toplantı_duzenle(self):
        """Yönetici sınıfına özel ekstra bir metot."""
        print(f"{self.isim} ekibiyle toplantı başlattı.")


# ==============================================================================
# Kullanım / Test Alanı
# ==============================================================================

if __name__ == "__main__":
    print("--- 1. Standart Çalışan Nesnesi ---")
    c1 = Calisan("Ahmet Yılmaz", 45000, "İnsan Kaynakları")
    c1.bilgileri_goster()
    c1.zam_yap(10)

    print("\n--- 2. Yönetici Nesnesi (Kalıtım Alan Sınıf) ---")
    y1 = Yonetici("Ayşe Kaya", 75000, "Yazılım", 12)
    
    # Calisan sınıfından devralınan ve ezilen metot:
    y1.bilgileri_goster()
    
    # Calisan sınıfından doğrudan devralınan metot:
    y1.zam_yap(15)
    
    # Sadece Yonetici sınıfına ait metot:
    y1.toplantı_duzenle()