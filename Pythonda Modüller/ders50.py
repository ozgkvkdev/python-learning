import random

print("==================================================")
# ANA KONU: random modülü, programlarımızda şans faktörü, 
# çekilişler veya rastgele durumlar oluşturmak için kullanılır.
print("       PYTHON `random` MODÜLÜ ANA TEMELLERİ       ")
print("==================================================")


# ÖRNEK 1: Belirli bir aralıkta rastgele TAM SAYI üretme (randint)
# Bu fonksiyon, yazdığımız iki sınır sayı da dahil olmak üzere aradan rastgele birini seçer.
print("\n[Örnek 1] Rastgele Tam Sayı Üretimi (Zar Simülasyonu):")
zar_sonucu = random.randint(1, 6)  # 1 ile 6 arasında (1 ve 6 dahil) rastgele sayı üretir.
print(f"-> Atılan zar sonucu: {zar_sonucu}")


# ÖRNEK 2: Bir listenin içinden rastgele ELEMAN seçme (choice)
# Bu fonksiyon, verdiğimiz listenin içerisinden tamamen rastgele tek bir eleman cımbızlar.
print("\n[Örnek 2] Listeden Rastgele Seçim Yapma (Çekiliş):")
katilimcilar = ["Ahmet", "Elif", "Can", "Merve", "Bora"]
sansli_kisi = random.choice(katilimcilar)  # Listeden rastgele bir isim seçer.

print(f"-> Çekilişe Katılanlar : {katilimcilar}")
print(f"-> Çekilişi Kazanan Kişi: {sansli_kisi}")


print("\n==================================================")
print("     Öğretici Örnekler Başarıyla Tamamlandı!     ")
print("==================================================")