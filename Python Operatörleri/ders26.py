# ==============================================================================
# PYTHON MANTIKSAL OPERATÖRLER - UYGULAMA SORULARI VE ÇÖZÜMLERİ
# ==============================================================================

print("--- MANTIKSAL OPERATÖRLER PRATİK UYGULAMA TESTİ ---")

# ------------------------------------------------------------------------------
# SORU 1: Burs Başvuru Koşulu ('and' Operatörü)
# Senaryo: Bir öğrencinin burstan yararlanabilmesi için not ortalamasının 85 veya 
# üzeri OLMASI ve devamsızlığının 5 günden az OLMASI gerekmektedir.
# ------------------------------------------------------------------------------
print("\n[Soru 1 - Burs Kontrolü]")
ortalaması = float(input("Not ortalamanızı giriniz: "))
devamsizlik = int(input("Devamsızlık gün sayınızı giriniz: "))

burs_alabilir_mi = (ortalaması >= 85) and (devamsizlik < 5)
print(f"Burs onay durumu: {burs_alabilir_mi}")


# ------------------------------------------------------------------------------
# SORU 2: İşe Alım Mülakatı ('or' Operatörü)
# Senaryo: Bir şirkete başvurmak için ya Bilgisayar Mühendisliği mezunu olmak 
# ya da en az 3 yıl yazılım deneyimine sahip olmak yeterlidir (biri yetiyor).
# ------------------------------------------------------------------------------
print("\n[Soru 2 - İşe Alım Kontrolü]")
mezun_mu = input("Bilgisayar Mühendisliği mezunu musunuz? (evet/hayir): ").lower() == "evet"
deneyim_yili = int(input("Kaç yıllık yazılım deneyiminiz var?: "))

mulakat_daveti = (mezun_mu == True) or (deneyim_yili >= 3)
print(f"Mülakata çağrılma durumu: {mulakat_daveti}")


# ------------------------------------------------------------------------------
# SORU 3: Banka Kredisi Onayı (Çoklu 'and' Kullanımı)
# Senaryo: Kredi onayı için kullanıcının yaşının 18 ile 65 arasında (18 ve 65 dahil)
# olması ve aylık gelirinin 30.000 TL'den fazla olması gerekir.
# ------------------------------------------------------------------------------
print("\n[Soru 3 - Kredi Onay Kontrolü]")
yas = int(input("Yaşınızı giriniz: "))
gelir = float(input("Aylık gelirinizi giriniz (TL): "))

kredi_onay = (yas >= 18) and (yas <= 65) and (gelir > 30000)
print(f"Kredi onay durumu: {kredi_onay}")


# ------------------------------------------------------------------------------
# SORU 4: Premium Üyelik / Kupon Geçerliliği ('or' ve 'and' Birlikte)
# Senaryo: Bir e-ticaret sitesinde sepette indirim uygulanması için ya kullanıcının 
# VIP üye olması ya da sepet tutarının 1000 TL üzerinde OLUP indirim koduna sahip olması gerekir.
# ------------------------------------------------------------------------------
print("\n[Soru 4 - İndirim Kuponu Kontrolü]")
vip_uye = input("VIP üye misiniz? (evet/hayir): ").lower() == "evet"
sepet_tutari = float(input("Sepet tutarını giriniz: "))
kod_var_mi = input("İndirim kodunuz var mı? (evet/hayir): ").lower() == "evet"

# İşlem önceliği için parantez kullanımına dikkat!
indirim_uygula = (vip_uye == True) or ((sepet_tutari > 1000) and (kod_var_mi == True))
print(f"İndirim uygulanacak mı?: {indirim_uygula}")


# ------------------------------------------------------------------------------
# SORU 5: Oyun Giriş Şartı ve Ters Mantık ('not' ve 'and')
# Senaryo: Bir online oyuna girmek için kullanıcının banlı OLMAMASI (not) 
# ve sunucunun bakımda OLMAMASI (not) gerekir.
# ------------------------------------------------------------------------------
print("\n[Soru 5 - Oyuna Giriş Kontrolü]")
is_banned = False       # Kullanıcı banlı değil
is_maintenance = False  # Sunucu bakımda değil

# Banlı DEĞİLSE ve Bakımda DEĞİLSE giriş yapabilir
oyuna_girebilir_mi = (not is_banned) and (not is_maintenance)
print(f"Oyuna giriş izni: {oyuna_girebilir_mi}")


# ------------------------------------------------------------------------------
# SORU 6: Sayı Aralığı Kontrolü
# Senaryo: Kullanıcıdan alınan bir sayının çift olup olmadığını ve aynı zamanda 
# 0 ile 100 arasında (0 ve 100 dahil değil) olup olmadığını kontrol edin.
# ------------------------------------------------------------------------------
print("\n[Soru 6 - Sayı Analizi]")
sayi = int(input("Bir sayı giriniz: "))

# Sayının çift olması -> sayi % 2 == 0
gecerli_sayi = (sayi % 2 == 0) and (sayi > 0) and (sayi < 100)
print(f"Sayı şartları sağlıyor mu?: {gecerli_sayi}")

# ==============================================================================
# DOSYA SONU
# ==============================================================================