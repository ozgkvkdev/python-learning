# ==============================================================================
# PYTHON MANTIKSAL OPERATÖRLER (Logical Operators)
# ==============================================================================

# Mantıksal operatörler birden fazla koşulu birleştirmek için kullanılır.
# 3 temel mantıksal operatör vardır: and, or, not

# ------------------------------------------------------------------------------
# 1. 'and' OPERATÖRÜ (VE)
# ------------------------------------------------------------------------------
# Her iki tarafındaki koşulun da TRUE olması gerekir. Bir tane bile False varsa sonuç False olur.
# True  and True  -> True
# True  and False -> False
# False and False -> False

yas = 20
ehliyet_var = True

# Hem yaş 18'den büyük OLMALI hem de ehliyeti OLMALI
araba_kullanabilir_mi = (yas >= 18) and (ehliyet_var == True)
print("1. 'and' Sonucu (Araba Kullanabilir mi?):", araba_kullanabilir_mi) # Çıktı: True


# ------------------------------------------------------------------------------
# 2. 'or' OPERATÖRÜ (VEYA)
# ------------------------------------------------------------------------------
# Koşullardan sadece BİR TANESİNİN True olması sonucun True çıkması için yeterlidir.
# Sadece iki taraf da False olduğunda False sonucunu verir.
# True  or False -> True
# False or True  -> True
# False or False -> False

bakiye = 100
kredi_karti_onay = False

# Bakiye 500'den büyük OLMALI VEYA kredi kartı onayı OLMALI (biri yetiyor)
urun_satinalabilir_mi = (bakiye >= 500) or (kredi_karti_onay == True)
print("2. 'or' Sonucu (Ürün Satın Alabilir mi?):", urun_satinalabilir_mi) # Çıktı: False


# ------------------------------------------------------------------------------
# 3. 'not' OPERATÖRÜ (DEĞİL)
# ------------------------------------------------------------------------------
# Verilen boolean (True/False) değerin tam tersini alır.
# not True  -> False
# not False -> True

sistem_acik_mi = False

# Sistemin açık olmama durumunu kontrol ediyoruz
print("3. 'not' Sonucu (Sistem Kapalı mı?):", not sistem_acik_mi) # Çıktı: True


# ------------------------------------------------------------------------------
# BİRLEŞİK ÖRNEK (and, or, not Bir Arada)
# ------------------------------------------------------------------------------
# Python bu işlemleri yaparken önce parantez içlerini, sonra 'not', sonra 'and', en son 'or' işlemini yapar.

x, y, z = 5, 10, 15

# Koşul 1: (x < y) -> (5 < 10) -> True
# Koşul 2: (y == z) -> (10 == 15) -> False
# İşlem: True and False -> False
result_1 = (x < y) and (y == z)

# Koşul 1: (x != y) -> (5 != 10) -> True
# Koşul 2: not (z > y) -> not (15 > 10) -> not True -> False
# İşlem: True or False -> True
result_2 = (x != y) or not (z > y)

print("\n--- Birleşik Örnek Sonuçları ---")
print("Result 1:", result_1) # Çıktı: False
print("Result 2:", result_2) # Çıktı: True