# ==========================================
# PYTHON ITERATORS (YİNELEYİCİLER)
# ==========================================

# Iterator, bir koleksiyon içerisindeki elemanlara
# tek tek ulaşmamızı sağlayan nesnedir.

# Python'da iterator oluşturmak için:
# iter() fonksiyonunu kullanabiliriz.

# Iterator içerisindeki bir sonraki elemana ulaşmak için:
# next() fonksiyonunu kullanırız.


# ------------------------------------------
# 1. Listeyi Iterator'a Dönüştürme
# ------------------------------------------

meyveler = ["Elma", "Armut", "Muz", "Çilek"]

# Listeyi iterator'a dönüştürüyoruz.
meyve_iterator = iter(meyveler)

# next() ile elemanlara sırayla ulaşabiliriz.
print(next(meyve_iterator))  # Elma
print(next(meyve_iterator))  # Armut
print(next(meyve_iterator))  # Muz
print(next(meyve_iterator))  # Çilek


# ------------------------------------------
# 2. Iterator'ın Mantığı
# ------------------------------------------

# Iterator bulunduğu konumu hatırlar.

sayilar = [10, 20, 30, 40]

iterator = iter(sayilar)

print(next(iterator))  # 10
print(next(iterator))  # 20

# Burada iterator 20. elemandan sonra devam eder.
print(next(iterator))  # 30
print(next(iterator))  # 40


# ------------------------------------------
# 3. Iterator Bittiğinde Ne Olur?
# ------------------------------------------

# Iterator içerisindeki tüm elemanlar kullanıldığında
# tekrar next() çağırırsak StopIteration hatası oluşur.

sayilar = [1, 2]

iterator = iter(sayilar)

print(next(iterator))  # 1
print(next(iterator))  # 2

# print(next(iterator))
# StopIteration hatası verir.


# ------------------------------------------
# 4. for Döngüsü ve Iterator
# ------------------------------------------

# Aslında for döngüsü arka planda iterator mantığını kullanır.

isimler = ["Ali", "Ahmet", "Mehmet"]

for isim in isimler:
    print(isim)

# Python burada listeyi iterator'a dönüştürür
# ve elemanları sırayla alır.


# ------------------------------------------
# 5. Iterator'ı Manuel Olarak Kullanmak
# ------------------------------------------

isimler = ["Ali", "Ahmet", "Mehmet"]

isim_iterator = iter(isimler)

while True:

    try:
        # Bir sonraki elemana ulaşılır.
        isim = next(isim_iterator)

        print(isim)

    except StopIteration:
        # Iterator'ın sonuna geldiğimizde
        # StopIteration hatası oluşur.
        break


# ==========================================
# KENDİ ITERATOR'IMIZI OLUŞTURMA
# ==========================================

# Python'da kendi iterator sınıfımızı da oluşturabiliriz.
#
# Bunun için:
# __iter__()
# __next__()
#
# metotlarını kullanırız.


class Sayac:

    def __init__(self, maksimum):
        # Sayacın başlayacağı değer.
        self.sayi = 0

        # Sayacın ulaşabileceği maksimum değer.
        self.maksimum = maksimum

    def __iter__(self):
        # Iterator nesnesinin kendisini döndürür.
        return self

    def __next__(self):

        # Eğer sayı maksimum değere ulaştıysa
        # iterator sona erer.
        if self.sayi >= self.maksimum:
            raise StopIteration

        # Mevcut sayıyı kaydediyoruz.
        mevcut_sayi = self.sayi

        # Bir sonraki elemana geçiyoruz.
        self.sayi += 1

        # Mevcut değeri döndürüyoruz.
        return mevcut_sayi


# Iterator nesnemizi oluşturuyoruz.
sayac = Sayac(5)

# for döngüsü iterator'ımızı kullanır.
for sayi in sayac:
    print(sayi)


# ==========================================
# ÖZET
# ==========================================

# iter()  -> Bir nesneyi iterator'a dönüştürür.
#
# next()  -> Iterator'daki bir sonraki elemana ulaşır.
#
# __iter__() -> Iterator nesnesini döndürür.
#
# __next__() -> Bir sonraki değeri döndürür.
#
# StopIteration -> Iterator'ın sonuna gelindiğinde oluşur.
#
# for döngüsü -> Arka planda iterator mantığını kullanır.