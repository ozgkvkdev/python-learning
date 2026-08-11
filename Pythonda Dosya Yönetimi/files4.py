# """
# Python Dosya Güncelleme (File Updating) Temel Eğitimi

# Bu script, Python'da var olan bir dosyanın içeriğini bozmadan nasıl 
# güncelleyeceğimizi ve veri ekleyeceğimizi (Append ve r+ modları) 
# en sade haliyle örneklemek için hazırlanmıştır.
# """

# print("==================================================")
# # ANA KONU: Python'da 'w' modu dosyayı sıfırlar. Dosyayı güncellemek 
# # ve eski verileri korumak için 'a' veya 'r+' modlarını kullanırız.
# print("          PYTHON DOSYA GÜNCELLEME TEMELLERİ        ")
# print("==================================================")

# # DERS İÇİN ÖNCELİKLE GEÇİCİ BİR DOSYA OLUŞTURALIM
# # İçinde sadece tek bir satır olan "rehber.txt" adında bir dosya açıyoruz.
# with open("rehber.txt", "w", encoding="utf-8") as dosya:
#     dosya.write("1. Ahmet Yılmaz\n")


# # ÖRNEK 1: Dosyanın Sonuna Yeni Veri Ekleme ('a' modu)
# # 'a' (append) modu, dosyanın mevcut içeriğine dokunmaz, imleci direkt 
# # dosyanın en sonuna götürür ve yeni yazılanları oraya ekler.
# print("\n[Örnek 1] 'a' Modu ile Dosya Sonuna Ekleme Yapma:")

# with open("rehber.txt", "a", encoding="utf-8") as dosya:
#     # Dosyanın sonuna yeni bir isim ekliyoruz
#     dosya.write("2. Elif Kaya\n")

# # Kontrol etmek için dosyayı okuyalım
# with open("rehber.txt", "r", encoding="utf-8") as dosya:
#     print("-> 'a' sonrası dosya içeriği:\n" + dosya.read())


# # ÖRNEK 2: Dosyanın Başına veya Belirli Bir Yerine Ekleme ('r+' modu)
# # 'r+' modu dosyayı hem okumamızı hem yazmamızı sağlar. Dosyanın başına 
# # veri eklemek için önce mevcut içeriği okur, sonra imleci başa alıp güncelleriz.
# print("[Örnek 2] 'r+' Modu ile Dosyanın Başına Ekleme Yapma:")

# with open("rehber.txt", "r+", encoding="utf-8") as dosya:
#     eski_icerik = dosya.read()  # Önce mevcut veriyi hafızaya alıyoruz
    
#     yeni_baslik = "--- KULLANICI REHBERİ ---\n"
    
#     dosya.seek(0)  # seek(0) ile imleci dosyanın en başına (0. karaktere) taşıyoruz
    
#     # Başa yeni başlığı ve ardından eski içeriği birleştirerek yazıyoruz
#     dosya.write(yeni_baslik + eski_icerik)

# # Son durumu kontrol etmek için tekrar okuyalım
# with open("rehber.txt", "r", encoding="utf-8") as dosya:
#     print("-> 'r+' sonrası son dosya içeriği:\n" + dosya.read())


# print("==================================================")
# print("     Dosya Güncelleme Dersi Başarıyla Bitti!     ")
# print("==================================================")