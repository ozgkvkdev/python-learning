"""
Python Hata ve Hata Yönetimi (try-except) Temel Eğitimi

Bu script, Python'da programın çökmesini engelleyen hata yönetimi yapısının
ana mantığını ve en sık karşılaşılan 2 hata türünü örneklemek için hazırlanmıştır.
"""

print("==================================================")
# ANA KONU: Program çalışırken meydana gelebilecek ve kodun durmasına 
# sebep olacak hataları (Exception) 'try-except' blokları ile yakalarız.
# Mantık şudur: "try bloğundaki kodları dene, hata çıkarsa except bloğuna geç."
print("     PYTHON HATA YÖNETİMİ (try-except) TEMELLERİ   ")
print("==================================================")


# ÖRNEK 1: Sıfıra Bölme Hatasını Yakalama (ZeroDivisionError)
# Matematikte bir sayı 0'a bölünemez. Python bunu yapmaya çalışırsak çöker.
print("\n[Örnek 1] Sıfıra Bölme Hatası Yönetimi:")

try:
    sayi = 10
    bolen = 0
    sonuc = sayi / bolen  # Bu satır hata üretecek!
    print(f"Sonuç: {sonuc}")
except ZeroDivisionError:
    # Eğer yukarıda ZeroDivisionError hatası alınırsa program çökmez, burası çalışır.
    print("-> HATA: Bir sayıyı sıfıra bölemezsiniz! Lütfen bölen sayıyı değiştirin.")


# ÖRNEK 2: Tip/Veri Türü Hatasını Yakalama (ValueError)
# Sayı beklediğimiz bir fonksiyona harf veya metin girilirse bu hata tetiklenir.
print("\n[Örnek 2] Hatalı Veri Türü Yönetimi:")

kullanici_girdisi = "Ahmet"  # Kullanıcının sayı yerine ismini girdiğini varsayalım.

try:
    # int() fonksiyonu "Ahmet" metnini sayıya çeviremez ve hata verir.
    yas = int(kullanici_girdisi)
    print(f"Yaşınız: {yas}")
except ValueError:
    # Hata yakalandığı için program durmaz, kullanıcıya kibar bir uyarı gösterilir.
    print(f"-> HATA: '{kullanici_girdisi}' bir sayıya dönüştürülemez! Lütfen sadece rakam girin.")


print("\n==================================================")
# Hata yönetimi sayesinde yukarıdaki hatalara rağmen bu son satır bile başarıyla çalışır!
print("   Program Çökmeden Başarıyla Tamamlandı!   ")
print("==================================================")