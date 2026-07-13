# ==============================================================================
# PYTHON KARŞILAŞTIRMA OPERATÖRLERİ - UYGULAMA SORULARI VE ÇÖZÜMLERİ
# ==============================================================================

print("--- KARŞILAŞTIRMA OPERATÖRLERİ PRATİK TESTİ ---")

# ------------------------------------------------------------------------------
# SORU 1: Ehliyet Yaş Kontrolü (Büyük-Eşit Operatörü '>=')
# Senaryo: Kullanıcının girdiği yaşın ehliyet almaya yetip yetmediğini (18 veya daha büyük) kontrol edin.
# ------------------------------------------------------------------------------
print("\n[Soru 1]")
yas = int(input("Yaşınızı giriniz: "))
ehliyet_alabilir_mi = (yas >= 18)

print(f"Ehliyet alabilme durumu (True/False): {ehliyet_alabilir_mi}")


# ------------------------------------------------------------------------------
# SORU 2: E-Ticaret Ücretsiz Kargo Kontrolü (Büyüktür Operatörü '>')
# Senaryo: Sepet tutarı 500 TL'nin üzerindeyse kargo ücretsiz olacaktır. Durumu kontrol edin.
# ------------------------------------------------------------------------------
print("\n[Soru 2]")
sepet_tutari = float(input("Sepet toplamını giriniz (TL): "))
bedava_kargo = (sepet_tutari > 500)

print(f"Ücretsiz kargo hakkı var mı? : {bedava_kargo}")


# ------------------------------------------------------------------------------
# SORU 3: Kritik Stok Uyarısı (Küçük-Eşit Operatörü '<=')
# Senaryo: Bir mağazadaki ürün sayısı 10 veya daha az kaldığında stok alarmı 'True' dönmelidir.
# ------------------------------------------------------------------------------
print("\n[Soru 3]")
stok_adedi = int(input("Kalan ürün adedini giriniz: "))
stok_uyarisi_ver = (stok_adedi <= 10)

print(f"Kritik stok uyarısı aktif mi? : {stok_uyarisi_ver}")


# ------------------------------------------------------------------------------
# SORU 4: Aktivasyon Kodu Doğrulama (Eşittir Operatörü '==')
# Senaryo: Sistemdeki sabit kod ile kullanıcının girdiği kodun eşleşip eşleşmediğini kontrol edin.
# ------------------------------------------------------------------------------
print("\n[Soru 4]")
sistem_kodu = "TR-2026"
kullanici_kodu = input("Aktivasyon kodunuzu giriniz: ")
kod_dogru_mu = (sistem_kodu == kullanici_kodu)

print(f"Aktivasyon başarılı mı? : {kod_dogru_mu}")


# ------------------------------------------------------------------------------
# SORU 5: Kullanıcı Adı Değiştirme Kontrolü (Eşit Değildir Operatörü '!=')
# Senaryo: Kullanıcı yeni bir kullanıcı adı seçerken, bunun eski kullanıcı adından FARKLI olmasını şart koşuyoruz.
# ------------------------------------------------------------------------------
print("\n[Soru 5]")
eski_kullanici_adi = "yazilimci_kanka"
yeni_kullanici_adi = input("Yeni kullanıcı adınızı giriniz: ")
degisim_onaylandi = (yeni_kullanici_adi != eski_kullanici_adi)

print(f"Kullanıcı adı değiştirilebilir mi? : {degisim_onaylandi}")

# ==============================================================================
# DOSYA SONU
# ==============================================================================