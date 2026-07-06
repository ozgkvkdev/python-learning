# ============================================
# PYTHON DERS 7
# Konu: Karakter Dizileri (String)
# ============================================

# String, çift (" ") veya tek (' ') tırnak içine yazılan metinlerdir.

mesaj = "Merhaba Python"

print(mesaj)

print("---------------------------------")


# ============================================
# Karakter Sayısı (len)
# ============================================

mesaj = "Merhaba Python"

print(len(mesaj))

# len() fonksiyonu karakter sayısını verir.


print("---------------------------------")


# ============================================
# Karakterlere Erişim (Index)
# ============================================

mesaj = "Python"

print(mesaj[0])   # P
print(mesaj[1])   # y
print(mesaj[2])   # t
print(mesaj[3])   # h
print(mesaj[4])   # o
print(mesaj[5])   # n


print("---------------------------------")


# ============================================
# Negatif Index
# ============================================

print(mesaj[-1])  # Son karakter
print(mesaj[-2])  # Sondan ikinci karakter


print("---------------------------------")


# ============================================
# String Dilimleme (Slicing)
# ============================================

mesaj = "Merhaba Python"

print(mesaj[0:7])

print(mesaj[8:14])

print(mesaj[:7])

print(mesaj[8:])

print(mesaj[:])


print("---------------------------------")


# ============================================
# Adım Değeri (Step)
# ============================================

print(mesaj[::2])

print(mesaj[::-1])   # Metni ters çevirir


print("---------------------------------")


# ============================================
# String Birleştirme
# ============================================

ad = "Özgür"
soyad = "Kavak"

adSoyad = ad + " " + soyad

print(adSoyad)


print("---------------------------------")


# ============================================
# String Tekrarlama
# ============================================

print("Python " * 3)