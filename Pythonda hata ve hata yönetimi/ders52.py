"""
Python `raise` ile Hata Nesnesi Oluşturma (Hata Fırlatma)

Bu script, Python'ın kendi kuralları dışında, kendi belirlediğimiz mantıksal 
koşullara göre nasıl manuel hata (Exception) tetikleyeceğimizi ve bunu nasıl 
yöneteceğimizi en sade haliyle göstermek için hazırlanmıştır.
"""

print("==================================================")
# ANA KONU: 'raise' anahtar kelimesi, programın akışını bilerek ve 
# isteyerek durdurup bir hata nesnesi fırlatmamızı sağlar.
# Fırlatılan bu hatalar da yine 'try-except' ile yakalanabilir.
print("        PYTHON `raise` İLE HATA FIRLATMA           ")
print("==================================================")


# ÖRNEK 1: Mantıksal Koşula Göre Hata Fırlatma (ValueError)
# Python yaşın -5 olmasını umursamaz (matematiksel olarak bir sayıdır), 
# ama gerçek hayatta yaş negatif olamaz. Bu mantık hatasını biz fırlatırız.
print("\n[Örnek 1] Yaş Kontrolü ve Hata Fırlatma:")

girilen_yas = -5

try:
    if girilen_yas < 0:
        # Şartımıza uymadığı için manuel olarak bir ValueError nesnesi oluşturup fırlatıyoruz:
        raise ValueError("Bir insanın yaşı sıfırdan küçük olamaz!")
    
    print(f"Yaşınız başarıyla kaydedildi: {girilen_yas}")

except ValueError as hata_mesaji:
    # Fırlattığımız hata nesnesinin içindeki mesajı 'as' kelimesiyle yakalayıp yazdırıyoruz.
    print(f"-> Yakalanan Hata: {hata_mesaji}")


# ÖRNEK 2: Şifre Uzunluğu Kontrolü (Exception)
# Genel bir hata nesnesi fırlatarak şifrenin güvenlik kurallarına uyup uymadığını denetliyoruz.
print("\n[Örnek 2] Şifre Güvenliği Kontrolü:")

kullanici_sifresi = "123"

try:
    if len(kullanici_sifresi) < 6:
        # Şifre çok kısa olduğunda genel bir Exception (Hata) nesnesi oluşturuyoruz:
        raise Exception("Güvenlik Uyarısı: Şifre en az 6 karakterden oluşmalıdır!")
    
    print("Şifreniz güvenli! Giriş yapılıyor...")

except Exception as hata_nesnesi:
    # Fırlatılan hata nesnesini ekrana basıyoruz.
    print(f"-> Yakalanan Hata: {hata_nesnesi}")


print("\n==================================================")
# raise ile fırlattığımız hataları try-except ile kontrol altına aldığımız için program çökmez:
print("   Ders Başarıyla Tamamlandı! Hatalar Yönetildi.  ")
print("==================================================")