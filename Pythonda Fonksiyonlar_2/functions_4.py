# Decorator fonksiyonu oluşturuyoruz.
# Bu fonksiyon başka bir fonksiyonu parametre olarak alacak.
def giris_kontrol(func):

    # Asıl fonksiyonun etrafına ekstra işlemler ekleyecek
    # wrapper isimli iç fonksiyonu oluşturuyoruz.
    def wrapper():

        # Asıl fonksiyon çalışmadan önce yapılacak işlem.
        print("# Kullanıcı kontrol ediliyor...")

        # Kullanıcının giriş yapıp yapmadığını kontrol ediyoruz.
        kullanici_giris_yapti = True

        # Kullanıcı giriş yaptıysa asıl fonksiyonu çalıştırıyoruz.
        if kullanici_giris_yapti:
            func()

        # Kullanıcı giriş yapmadıysa uyarı mesajı gösteriyoruz.
        else:
            print("# Önce giriş yapmalısınız.")

    # wrapper fonksiyonunu geri döndürüyoruz.
    # Böylece decorator uygulandığında wrapper kullanılacak.
    return wrapper


# @giris_kontrol yazımı,
# profil = giris_kontrol(profil) işleminin kısa halidir.
@giris_kontrol
def profil():

    # Profil fonksiyonunun kendi işlemi.
    print("# Profil sayfası açıldı.")


# Aynı decorator'ı başka bir fonksiyona da uygulayabiliriz.
@giris_kontrol
def ayarlar():

    # Ayarlar fonksiyonunun kendi işlemi.
    print("# Ayarlar sayfası açıldı.")


# Decorator tarafından sarılmış olan profil fonksiyonunu çalıştırıyoruz.
profil()

print()

# Decorator tarafından sarılmış olan ayarlar fonksiyonunu çalıştırıyoruz.
ayarlar()