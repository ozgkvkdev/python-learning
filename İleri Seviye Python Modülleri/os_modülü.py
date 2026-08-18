# ==========================================
# PYTHON OS MODÜLÜ
# ==========================================

# os modülü, Python üzerinden işletim sistemiyle
# iletişim kurmamızı sağlar.
#
# Dosya ve klasör işlemleri,
# mevcut çalışma dizinini öğrenme,
# ortam değişkenlerine erişme,
# klasör oluşturma ve silme gibi
# işlemlerde kullanılır.

import os


# ==========================================
# 1. MEVCUT ÇALIŞMA DİZİNİNİ ÖĞRENME
# ==========================================

# os.getcwd() programın çalıştığı
# mevcut klasörün yolunu verir.

mevcut_dizin = os.getcwd()

print("Mevcut dizin:", mevcut_dizin)


# ==========================================
# 2. DİZİN DEĞİŞTİRME
# ==========================================

# os.chdir() ile çalışma dizinimizi değiştirebiliriz.
#
# Örnek:
#
# os.chdir("C:/Users/ozgur/Desktop")
#
# Windows'ta dosya yollarında "/" kullanmak
# işlemleri kolaylaştırabilir.

# os.chdir("C:/Users/ozgur/Desktop")


# ==========================================
# 3. KLASÖRDEKİ DOSYALARI LİSTELEME
# ==========================================

# os.listdir() belirttiğimiz klasörde bulunan
# dosya ve klasörleri liste olarak döndürür.

dosyalar = os.listdir()

print("Mevcut klasörde bulunanlar:")

for dosya in dosyalar:
    print(dosya)


# Belirli bir klasörü de listeleyebiliriz.
#
# dosyalar = os.listdir("C:/Users/ozgur/Desktop")


# ==========================================
# 4. KLASÖR OLUŞTURMA
# ==========================================

# os.mkdir() yeni bir klasör oluşturur.

# os.mkdir("yeni_klasor")


# ==========================================
# 5. İÇ İÇE KLASÖRLER OLUŞTURMA
# ==========================================

# os.makedirs() birden fazla iç içe klasör
# oluşturmak için kullanılabilir.

# os.makedirs("proje/data/users")


# ==========================================
# 6. KLASÖR SİLME
# ==========================================

# os.rmdir() boş bir klasörü siler.

# os.rmdir("yeni_klasor")


# ==========================================
# 7. DOSYA SİLME
# ==========================================

# os.remove() bir dosyayı silmek için kullanılır.

# os.remove("test.txt")


# ==========================================
# 8. DOSYA VEYA KLASÖRÜN VARLIĞINI KONTROL ETME
# ==========================================

# os.path.exists() belirttiğimiz yolun
# var olup olmadığını kontrol eder.

dosya = "test.txt"

if os.path.exists(dosya):
    print("Dosya mevcut.")
else:
    print("Dosya bulunamadı.")


# ==========================================
# 9. DOSYA MI KLASÖR MÜ?
# ==========================================

# os.path.isfile() yolun bir dosya olup
# olmadığını kontrol eder.

if os.path.isfile("test.txt"):
    print("Bu bir dosyadır.")


# os.path.isdir() yolun bir klasör olup
# olmadığını kontrol eder.

if os.path.isdir("yeni_klasor"):
    print("Bu bir klasördür.")


# ==========================================
# 10. DOSYA YOLU BİRLEŞTİRME
# ==========================================

# os.path.join() farklı parçaları birleştirerek
# işletim sistemine uygun bir dosya yolu oluşturur.

klasor = "data"
dosya = "users.txt"

dosya_yolu = os.path.join(klasor, dosya)

print("Dosya yolu:", dosya_yolu)

# Windows'ta:
#
# data\users.txt
#
# gibi bir sonuç oluşabilir.


# ==========================================
# 11. DOSYA UZANTISINI AYIRMA
# ==========================================

# os.path.splitext() dosya adını
# isim ve uzantı olarak ayırır.

dosya = "rapor.pdf"

isim, uzanti = os.path.splitext(dosya)

print("Dosya adı:", isim)
print("Uzantı:", uzanti)


# ==========================================
# 12. DOSYA YOLUNU AYIRMA
# ==========================================

# os.path.basename() bir dosya yolundan
# sadece dosya adını alır.

yol = "C:/Users/ozgur/Desktop/proje/main.py"

print("Dosya adı:", os.path.basename(yol))


# os.path.dirname() ise dosyanın
# bulunduğu klasörün yolunu verir.

print("Klasör yolu:", os.path.dirname(yol))


# ==========================================
# 13. DOSYA BOYUTUNU ÖĞRENME
# ==========================================

# os.path.getsize() dosyanın boyutunu
# byte cinsinden verir.

if os.path.exists("test.txt"):

    boyut = os.path.getsize("test.txt")

    print("Dosya boyutu:", boyut, "byte")


# ==========================================
# 14. ORTAM DEĞİŞKENLERİ
# ==========================================

# os.environ işletim sistemindeki
# environment variable değerlerine erişmemizi sağlar.

# Örneğin Windows'taki USERNAME bilgisini alabiliriz.

kullanici = os.environ.get("USERNAME")

print("Bilgisayar kullanıcısı:", kullanici)


# Linux / macOS sistemlerde USER değişkeni
# kullanılabilir.
#
# kullanici = os.environ.get("USER")


# ==========================================
# 15. İŞLETİM SİSTEMİNİ ÖĞRENME
# ==========================================

# os.name işletim sisteminin türünü
# öğrenmemizi sağlar.

print("İşletim sistemi:", os.name)

# Windows -> nt
# Linux / macOS -> posix


# ==========================================
# 16. İŞLETİM SİSTEMİ HAKKINDA BİLGİ
# ==========================================

# os.uname() Linux ve macOS gibi sistemlerde
# işletim sistemi hakkında daha fazla bilgi verir.
#
# Windows'ta bazı durumlarda kullanılamaz.
#
# os.uname()


# ==========================================
# 17. ORTAM DEĞİŞKENİ OLUŞTURMA
# ==========================================

# os.environ üzerinden yeni bir
# environment variable oluşturabiliriz.

os.environ["PROJE_ADI"] = "Python Project"

print("Proje adı:", os.environ.get("PROJE_ADI"))


# ==========================================
# 18. KLASÖRDEKİ TÜM DOSYALARI BULMA
# ==========================================

# os.listdir() ile klasördeki dosyaları
# kontrol ederek belirli uzantıya sahip
# dosyaları bulabiliriz.

dosyalar = os.listdir()

for dosya in dosyalar:

    if dosya.endswith(".py"):
        print("Python dosyası:", dosya)


# ==========================================
# 19. GERÇEK HAYAT ÖRNEĞİ
# ==========================================

# Bir proje içerisinde "logs" klasörü
# oluşturmak istediğimizi düşünelim.

logs_klasoru = os.path.join(os.getcwd(), "logs")

# Klasör mevcut değilse oluşturuyoruz.

if not os.path.exists(logs_klasoru):
    os.mkdir(logs_klasoru)
    print("Logs klasörü oluşturuldu.")

else:
    print("Logs klasörü zaten mevcut.")


# ==========================================
# 20. OS MODÜLÜ ÖZET
# ==========================================

# os.getcwd()
# -> Mevcut çalışma dizinini verir.
#
# os.chdir()
# -> Çalışma dizinini değiştirir.
#
# os.listdir()
# -> Klasördeki dosya ve klasörleri listeler.
#
# os.mkdir()
# -> Yeni klasör oluşturur.
#
# os.makedirs()
# -> İç içe klasörler oluşturur.
#
# os.rmdir()
# -> Boş klasörü siler.
#
# os.remove()
# -> Dosya siler.
#
# os.path.exists()
# -> Dosya veya klasörün varlığını kontrol eder.
#
# os.path.isfile()
# -> Yolun dosya olup olmadığını kontrol eder.
#
# os.path.isdir()
# -> Yolun klasör olup olmadığını kontrol eder.
#
# os.path.join()
# -> Dosya yollarını güvenli şekilde birleştirir.
#
# os.path.splitext()
# -> Dosya adı ve uzantısını ayırır.
#
# os.path.basename()
# -> Dosya yolundan dosya adını alır.
#
# os.path.dirname()
# -> Dosyanın bulunduğu klasör yolunu verir.
#
# os.path.getsize()
# -> Dosya boyutunu byte olarak verir.
#
# os.environ
# -> Ortam değişkenlerine erişmemizi sağlar.
#
# os.name
# -> İşletim sistemi türünü verir.


# ==========================================
# KISA MANTIK
# ==========================================

#                 OS MODÜLÜ
#                     |
#       +-------------+-------------+
#       |             |             |
#    Dosyalar      Klasörler    Sistem Bilgisi
#       |             |             |
#   remove()       mkdir()       environ
#   exists()       rmdir()       name
#   getsize()      listdir()     getcwd()
#   join()         makedirs()    chdir()
#
# OS modülü sayesinde Python programımız
# işletim sistemiyle doğrudan etkileşime
# geçebilir.