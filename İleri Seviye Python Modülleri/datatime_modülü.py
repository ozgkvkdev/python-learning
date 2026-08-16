# ==========================================
# PYTHON DATETIME MODÜLÜ
# ==========================================

# datetime modülü;
# tarih ve saat işlemleri yapmak için kullanılır.
#
# Tarih oluşturma, mevcut zamanı alma,
# tarihleri karşılaştırma, tarih üzerinde işlem yapma
# ve tarihleri istediğimiz formata dönüştürme
# gibi işlemlerde kullanılır.


from datetime import datetime, date, time, timedelta


# ==========================================
# 1. ŞU ANKİ TARİH VE SAAT
# ==========================================

# datetime.now() bulunduğumuz anın
# tarih ve saat bilgisini verir.

simdi = datetime.now()

print("Şu an:", simdi)


# ==========================================
# 2. SADECE TARİH
# ==========================================

# date.today() sadece bugünün tarihini verir.

bugun = date.today()

print("Bugünün tarihi:", bugun)


# ==========================================
# 3. TARİH OLUŞTURMA
# ==========================================

# datetime() kullanarak kendi tarih ve saatimizi
# oluşturabiliriz.

tarih = datetime(2026, 8, 16, 14, 30, 0)

print("Oluşturulan tarih:", tarih)


# ==========================================
# 4. TARİHTEN YIL, AY VE GÜN ALMA
# ==========================================

# year  -> yıl
# month -> ay
# day   -> gün

print("Yıl:", tarih.year)
print("Ay:", tarih.month)
print("Gün:", tarih.day)


# ==========================================
# 5. SAAT BİLGİLERİNİ ALMA
# ==========================================

# hour   -> saat
# minute -> dakika
# second -> saniye

print("Saat:", tarih.hour)
print("Dakika:", tarih.minute)
print("Saniye:", tarih.second)


# ==========================================
# 6. TARİHİ STRING'E ÇEVİRME
# ==========================================

# strftime() tarih bilgisini istediğimiz
# metin formatına dönüştürmemizi sağlar.

formatli_tarih = simdi.strftime("%d/%m/%Y")

print("Formatlı tarih:", formatli_tarih)


# Örneğin saat bilgisini de ekleyebiliriz.

formatli_tarih_saat = simdi.strftime("%d/%m/%Y %H:%M:%S")

print("Tarih ve saat:", formatli_tarih_saat)


# Kullanılan bazı formatlar:
#
# %d -> Gün
# %m -> Ay
# %Y -> 4 haneli yıl
# %H -> Saat
# %M -> Dakika
# %S -> Saniye


# ==========================================
# 7. STRING'İ TARİHE ÇEVİRME
# ==========================================

# strptime() bir string'i datetime nesnesine
# dönüştürmek için kullanılır.

tarih_string = "16/08/2026"

tarih = datetime.strptime(tarih_string, "%d/%m/%Y")

print("Datetime:", tarih)


# ==========================================
# 8. TARİHE GÜN EKLEME
# ==========================================

# timedelta() kullanarak tarihler üzerinde
# zaman işlemleri yapabiliriz.

yarin = simdi + timedelta(days=1)

print("Yarın:", yarin)


# 7 gün sonrası

bir_hafta_sonra = simdi + timedelta(days=7)

print("Bir hafta sonra:", bir_hafta_sonra)


# ==========================================
# 9. TARİHTEN GÜN ÇIKARMA
# ==========================================

# timedelta() ile geçmiş bir tarihi de
# kolayca hesaplayabiliriz.

dun = simdi - timedelta(days=1)

print("Dün:", dun)


# 30 gün önce

otuz_gun_once = simdi - timedelta(days=30)

print("30 gün önce:", otuz_gun_once)


# ==========================================
# 10. İKİ TARİH ARASINDAKİ FARK
# ==========================================

tarih1 = datetime(2026, 8, 1)
tarih2 = datetime(2026, 8, 16)

fark = tarih2 - tarih1

print("Tarihler arasındaki fark:", fark)
print("Gün farkı:", fark.days)


# ==========================================
# 11. TARİH KARŞILAŞTIRMA
# ==========================================

tarih1 = datetime(2026, 8, 10)
tarih2 = datetime(2026, 8, 20)

if tarih1 < tarih2:
    print("İlk tarih daha eski.")


# ==========================================
# 12. HAFTANIN GÜNÜNÜ BULMA
# ==========================================

# weekday() haftanın gününü sayı olarak verir.
#
# Pazartesi -> 0
# Salı      -> 1
# Çarşamba  -> 2
# Perşembe  -> 3
# Cuma      -> 4
# Cumartesi -> 5
# Pazar     -> 6

gun = simdi.weekday()

print("Haftanın günü:", gun)


# ==========================================
# 13. TARİHİN HAFTANIN HANGİ GÜNÜ OLDUĞUNU
# YAZI OLARAK BULMA
# ==========================================

gunler = [
    "Pazartesi",
    "Salı",
    "Çarşamba",
    "Perşembe",
    "Cuma",
    "Cumartesi",
    "Pazar"
]

print("Bugün:", gunler[simdi.weekday()])


# ==========================================
# 14. TARİHİN TIMESTAMP DEĞERİNİ ALMA
# ==========================================

# timestamp() tarihi bilgisayarların kullandığı
# timestamp değerine dönüştürür.

timestamp = simdi.timestamp()

print("Timestamp:", timestamp)


# ==========================================
# 15. TIMESTAMP'TEN TARİH OLUŞTURMA
# ==========================================

# fromtimestamp() timestamp değerini
# tekrar datetime nesnesine dönüştürür.

yeni_tarih = datetime.fromtimestamp(timestamp)

print("Timestamp'ten tarih:", yeni_tarih)


# ==========================================
# 16. SADECE SAAT OLUŞTURMA
# ==========================================

# time() sınıfı sadece saat bilgisi
# oluşturmak için kullanılabilir.

saat = time(14, 30, 45)

print("Saat:", saat)


# Saat bilgilerine ayrı ayrı ulaşabiliriz.

print("Saat:", saat.hour)
print("Dakika:", saat.minute)
print("Saniye:", saat.second)


# ==========================================
# 17. TARİHİN GÜN SAYISINI BULMA
# ==========================================

# date() kullanarak sadece tarih oluşturabiliriz.

dogum_tarihi = date(2004, 5, 15)
bugun = date.today()

yas_farki = bugun - dogum_tarihi

print("Doğum tarihinden bugüne geçen gün:",
      yas_farki.days)


# ==========================================
# 18. GERÇEK HAYAT ÖRNEĞİ
# ==========================================

# Bir kullanıcının üyelik başlangıç tarihini
# ve üyelik süresini hesaplayalım.

uyelik_baslangici = datetime(2026, 8, 1)

bugun = datetime.now()

gecen_sure = bugun - uyelik_baslangici

print("Üyelik başlangıcı:", uyelik_baslangici)
print("Geçen gün:", gecen_sure.days)


# ==========================================
# ÖZET
# ==========================================

# datetime.now()
# -> Şu anki tarih ve saati verir.
#
# date.today()
# -> Bugünün tarihini verir.
#
# strftime()
# -> Tarihi string formatına dönüştürür.
#
# strptime()
# -> String'i datetime nesnesine dönüştürür.
#
# timedelta()
# -> Tarihler arasında zaman ekleme/çıkarma
#    işlemlerinde kullanılır.
#
# weekday()
# -> Haftanın gününü 0-6 arasında döndürür.
#
# timestamp()
# -> Tarihi timestamp değerine dönüştürür.
#
# fromtimestamp()
# -> Timestamp değerini datetime'a dönüştürür.
#
# year
# -> Yıl bilgisini verir.
#
# month
# -> Ay bilgisini verir.
#
# day
# -> Gün bilgisini verir.
#
# hour
# -> Saat bilgisini verir.
#
# minute
# -> Dakika bilgisini verir.
#
# second
# -> Saniye bilgisini verir.
#
# datetime()
# -> Belirli bir tarih ve saat oluşturur.
#
# date()
# -> Sadece tarih oluşturur.
#
# time()
# -> Sadece saat oluşturur.


# ==========================================
# KISA MANTIK
# ==========================================

# datetime
#     ↓
# Tarih ve saat işlemleri
#
# date
#     ↓
# Sadece tarih
#
# time
#     ↓
# Sadece saat
#
# timedelta
#     ↓
# Tarihler arasında süre ekleme / çıkarma
#
# strftime
#     ↓
# Tarih → String
#
# strptime
#     ↓
# String → Tarih