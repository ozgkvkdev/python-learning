import math  # İlk olarak math modülünü projemize dahil ediyoruz.


print("=== 1. MATEMATİKSEL SABİTLER ===")
# Matematikte sıklıkla kullandığımız pi ve e sabitlerini modülden direkt çekebiliriz.
print(f"Pi Sayısı (math.pi): {math.pi}")
print(f"Euler Sayısı (math.e): {math.e}")
print("-" * 40)


print("\n=== 2. YUVARLAMA FONKSİYONLARI ===")
sayi = 4.3
sayi2 = 4.7

# math.ceil() -> Sayıyı her zaman YUKARIYA yuvarlar (Tavan)
print(f"{sayi} sayısının yukarı yuvarlanmış hali (ceil): {math.ceil(sayi)}")

# math.floor() -> Sayıyı her zaman AŞAĞIYA yuvarlar (Taban)
print(f"{sayi2} sayısının aşağı yuvarlanmış hali (floor): {math.floor(sayi2)}")

# math.trunc() -> Sayının ondalık kısmını direkt çöpe atar, tam kısmı bırakır
print(f"5.99 sayısının tam kısmı (trunc): {math.trunc(5.99)}")
print("-" * 40)


print("\n=== 3. GÜÇ, KÖK VE LOGARİTMA ===")
# math.pow(x, y) -> x üssü y hesabı yapar (x^y). Sonucu float döner.
print(f"2 üssü 5 (pow): {math.pow(2, 5)}")

# math.sqrt(x) -> x sayısının karekökünü alır.
print(f"64 sayısının karekökü (sqrt): {math.sqrt(64)}")

# math.log(x, taban) -> Belirtilen tabanda logaritma alır. Taban yazılmazsa doğal logaritma (ln) hesaplar.
print(f"8 sayısının 2 tabanındaki logaritması (log): {math.log(8, 2)}")
print(f"Euler sayısının doğal logaritması (ln(e)): {math.log(math.e)}")
print("-" * 40)


print("\n=== 4. SAYISAL İŞLEMLER (MUTLAK DEĞER VE FAKTÖRİYEL) ===")
# math.fabs(x) -> Sayının mutlak değerini float olarak döner.
print(f"-15 sayısının mutlak değeri (fabs): {math.fabs(-15)}")

# math.factorial(x) -> Pozitif tam sayıların faktöriyelini hesaplar.
print(f"5 faktöriyel (5!): {math.factorial(5)}")

# math.gcd(x, y) -> İki sayının En Büyük Ortak Bölenini (EBOB) bulur.
print(f"18 ve 24 sayılarının EBOB'u (gcd): {math.gcd(18, 24)}")
print("-" * 40)


print("\n=== 5. TRİGONOMETRİK İŞLEMLER ===")
# ÖNEMLİ: math modülündeki trigonometrik fonksiyonlar (sin, cos, tan) RADYAN cinsinden çalışır.
# Dereceyi radyana çevirmek için math.radians() kullanılır.

derece = 30
radyan_karsiligi = math.radians(derece)

print(f"{derece} derecenin radyan karşılığı: {radyan_karsiligi}")
print(f"Sin({derece}) değeri: {math.sin(radyan_karsiligi)}")  # Yaklaşık 0.5 çıkacaktır.
print("-" * 40)

print("\n=== İnceleme Bitti. Kod başarıyla çalıştı! ===")