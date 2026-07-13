# ==============================================================================
# PYTHON MEMBERSHIP (AİTLİK) VE IDENTITY (KİMLİK) OPERATÖRLERİ
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. MEMBERSHIP OPERATÖRLERİ (in , not in) -> Aitlik Kontrolü
# ------------------------------------------------------------------------------
# Bir elemanın bir listenin, stringin veya koleksiyonun İÇİNDE olup olmadığını kontrol eder.

renkler = ["kırmızı", "mavi", "yeşil", "sarı"]

# 'in' operatörü: İçindeyse True döner.
mavi_var_mi = "mavi" in renkler
print("Listede mavi var mı?:", mavi_var_mi)  # Çıktı: True

# 'not in' operatörü: İçinde DEĞİLSE True döner.
siyah_yok_mu = "siyah" not in renkler
print("Listede siyah yok mu?:", siyah_yok_mu)  # Çıktı: True

# Metinlerde (String) kullanımı:
isim = "özgür"
print("'özg' ismi içinde geçiyor mu?:", "özg" in isim)  # Çıktı: True


# ------------------------------------------------------------------------------
# 2. IDENTITY OPERATÖRLERİ (is , is not) -> Kimlik Kontrolü
# ------------------------------------------------------------------------------
# DİKKAT: 'is' operatörü ile '==' operatörü aynı şey DEĞİLDİR!
# '==', nesnelerin DEĞERLERİ aynı mı diye bakar.
# 'is', nesnelerin bellekteki ADRESLERİ (aynı nesne mi) diye bakar (id() kontrolü yapar).

liste_a = [1, 2, 3]
liste_b = [1, 2, 3]  # liste_a ile aynı değerlere sahip yeni bir liste
liste_c = liste_a    # liste_a'nın adresini doğrudan liste_c'ye eşitliyoruz

print("\n--- Kimlik Kontrolü Sonuçları ---")

# Değer kontrolü (==)
print("liste_a == liste_b:", liste_a == liste_b)  # Çıktı: True (Çünkü içlerindeki sayılar aynı)

# Kimlik/Adres kontrolü (is)
print("liste_a is liste_b:", liste_a is liste_b)  # Çıktı: False (Değerleri aynı ama bellekte farklı yerlerdeler)
print("liste_a is liste_c:", liste_a is liste_c)  # Çıktı: True (Çünkü c, doğrudan a'yı işaret ediyor)

# 'is not' operatörü: Adresleri farklı ise True döner.
print("liste_a is not liste_b:", liste_a is not liste_b)  # Çıktı: True