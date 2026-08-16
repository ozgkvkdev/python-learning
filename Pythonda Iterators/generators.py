# ==========================================
# PYTHON GENERATORS
# ==========================================

# Generator, değerleri tek seferde belleğe yüklemek yerine
# ihtiyaç duyuldukça tek tek üreten özel bir yapıdır.
#
# Generator oluşturmak için fonksiyon içerisinde
# "yield" anahtar kelimesini kullanırız.
#
# yield kullanıldığında fonksiyon tamamen bitmez.
# Ürettiği değeri döndürür ve kaldığı yeri hatırlar.


# ------------------------------------------
# 1. Basit Bir Generator Oluşturma
# ------------------------------------------

def sayilar():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# Generator fonksiyonunu çağırıyoruz.
generator = sayilar()

# next() kullanarak değerleri tek tek alabiliriz.
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(next(generator))  # 4
print(next(generator))  # 5

# Generator'da başka değer kalmadığında
# StopIteration oluşur.
#
# print(next(generator))
# StopIteration


# ------------------------------------------
# 2. Generator ve for Döngüsü
# ------------------------------------------

def meyveler():
    yield "Elma"
    yield "Armut"
    yield "Muz"
    yield "Çilek"


# Generator oluşturuyoruz.
meyve_generator = meyveler()

# for döngüsü ile değerleri sırayla alabiliriz.
for meyve in meyve_generator:
    print(meyve)


# ------------------------------------------
# 3. Generator ile Sayı Üretmek
# ------------------------------------------

def sayi_uret(maksimum):

    # 0'dan maksimum değere kadar ilerliyoruz.
    for sayi in range(maksimum):

        # Her sayıyı tek tek üretiyoruz.
        yield sayi


# Generator oluşturuyoruz.
sayilar = sayi_uret(5) # type: ignore

for sayi in sayilar: # pyright: ignore[reportGeneralTypeIssues]
    print(sayi)


# ------------------------------------------
# 4. yield ve return Arasındaki Fark
# ------------------------------------------

# return kullanıldığında fonksiyon tamamen sona erer.

def return_ornek():
    return 10
    return 20
    return 30


print(return_ornek())
# Sadece 10 döner.
# Çünkü return fonksiyonu sonlandırır.


# yield ise değeri üretir ve fonksiyonun
# kaldığı yeri hatırlar.

def yield_ornek():

    yield 10
    yield 20
    yield 30


generator = yield_ornek()

print(next(generator))  # 10
print(next(generator))  # 20
print(next(generator))  # 30


# ------------------------------------------
# 5. Generator Bellek Açısından Avantajlıdır
# ------------------------------------------

# Normal bir liste oluşturduğumuzda bütün değerler
# bellekte tutulur.

sayilar = [sayi for sayi in range(1000000)] # type: ignore

# Bu yapı bir milyon sayıyı bellekte tutar.


# Generator ise değerleri ihtiyaç oldukça üretir.

def buyuk_sayilar():

    for sayi in range(1000000):
        yield sayi


generator = buyuk_sayilar()

# Burada bir milyon sayı aynı anda belleğe yüklenmez.
# Sadece ihtiyaç duyduğumuz değer üretilir.

print(next(generator))
print(next(generator))
print(next(generator))


# ------------------------------------------
# 6. Generator Expression
# ------------------------------------------

# Generator oluşturmanın kısa bir yolu da
# generator expression kullanmaktır.

generator = (sayi * 2 for sayi in range(5))

for sayi in generator:
    print(sayi)


# ------------------------------------------
# 7. Gerçek Hayattan Basit Bir Örnek
# ------------------------------------------

# Örneğin bir sistemde kullanıcı ID'lerini
# tek tek üretmek istediğimizi düşünelim.

def kullanici_idleri():

    id = 1000

    while True:

        # Her çağrıldığında bir ID üretir.
        yield id

        # Sonraki ID'ye geçiyoruz.
        id += 1


kullanici_generator = kullanici_idleri()

print(next(kullanici_generator))  # 1000
print(next(kullanici_generator))  # 1001
print(next(kullanici_generator))  # 1002
print(next(kullanici_generator))  # 1003


# ==========================================
# GENERATOR ÖZET
# ==========================================

# Generator:
# Değerleri ihtiyaç duyulduğunda tek tek üreten yapıdır.
#
# yield:
# Değeri üretir ve fonksiyonun kaldığı yeri hatırlar.
#
# next():
# Generator'ın bir sonraki değerini getirir.
#
# Generator:
# Büyük veri kümelerinde belleği daha verimli kullanabilir.
#
# Generator Expression:
# Generator oluşturmanın kısa yoludur.
#
# Örnek:
#
# generator = (x for x in range(10))
#
# for x in generator:
#     print(x)
#
# Generator'ların temel mantığı:
#
# Fonksiyon
#     ↓
# yield
#     ↓
# değer üretilir
#     ↓
# fonksiyon kaldığı yeri hatırlar
#     ↓
# next()
#     ↓
# sonraki değer üretilir