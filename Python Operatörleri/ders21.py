# ==============================================================================
# PYTHON DEĞİŞKEN ATAMA VE OPERATÖRLER NOTLARI
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. TEMEL VE ÇOKLU DEĞER ATAMA (Variable Assignment)
# ------------------------------------------------------------------------------

# Tekli atama: Her değişkene sırayla değer verilir.
x = 5
y = 10
z = 20

# Çoklu atama (Multiple Assignment): Tek satırda birden fazla değişkene değer atanır.
x, y, z = 5, 10, 15
print("Çoklu Atama Sonucu:", x, y, z)  # Çıktı: 5 10 15


# ------------------------------------------------------------------------------
# 2. ARTTIRIMLI / BİLİŞİK ATAMA OPERATÖRLERİ (Augmented Assignment)
# ------------------------------------------------------------------------------
# Bu operatörler, bir değişkenin mevcut değerini değiştirip tekrar kendisine atar.

x = 5       # Başlangıç değeri

x = x + 5   # x'in değerini 5 artırır (Uzun yöntem) -> x = 10
x += 5      # x'in üzerine 5 ekler (Kısa yöntem)  -> x = 15
x -= 5      # x'ten 5 çıkarır                     -> x = 10
x *= 5      # x'i 5 ile çarpar                    -> x = 50
x /= 5      # x'i 5'e böler (Float sonuç döner)   -> x = 10.0

# Not: Python'da bileşik operatörlerde (%=, //=, **=) araya boşluk konulmaz.
x %= 5      # x'in 5'e bölümünden kalanı bulur (Mod alma) -> x = 0.0
x //= 5     # x'i 5'e tam böler (Taban bölme)             -> x = 0.0
x **= 5     # x'in 5. kuvvetini (üssünü) alır            -> x = 0.0

print("Operatörler Sonrası x Değeri:", x)


# ------------------------------------------------------------------------------
# 3. TUPLE UNPACKING (Demet Çözme / Çoklu Değişkene Dağıtma)
# ------------------------------------------------------------------------------

# Virgülle ayrılmış değerler varsayılan olarak bir 'tuple' (demet) oluşturur.
degerler = 1, 2, 3  

print("Değerler:", degerler)         # Çıktı: (1, 2, 3)
print("Veri Tipi:", type(degerler))  # Çıktı: <class 'tuple'>

# Unpacking: Tuple içindeki elemanları sırasıyla değişkenlere dağıtıyoruz.
# Değişken sayısı ile eleman sayısı eşit olmalıdır.
x, y, z = degerler
print("Unpacking Sonucu:", x, y, z)  # Çıktı: 1 2 3