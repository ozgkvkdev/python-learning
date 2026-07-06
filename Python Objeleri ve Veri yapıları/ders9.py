"""
==================================================
        PYTHON STRING (KARAKTER DİZİLERİ)
==================================================

Bu dosyada;

✔ len()
✔ String Indexing
✔ String Slicing
✔ Negatif Index
✔ Adım Değeri (Step)
✔ replace()
✔ String Çarpma
✔ String Formatlama

konuları örneklerle anlatılmıştır.
"""

# ==================================================
# Değişken Tanımlama
# ==================================================

website = "https://www.coursera.org/learn/python-programming-tr"
course = "Python Programlama Temelleri"

# ==================================================
# 1) course değişkenindeki karakter sayısını bulun.
# ==================================================

result = len(course)

print("1. Karakter Sayısı:", result)

# len() fonksiyonu karakterlerin tamamını sayar.
# Boşluklar da karakter olarak kabul edilir.

print("-" * 50)


# ==================================================
# 2) website içindeki "www" ifadesini alın.
# ==================================================

result = website[8:11]

print("2. www ifadesi:", result)

# Index numaraları:
#
# https://www...
#        8 9 10
#
# 8 dahil
# 11 dahil değildir.

print("-" * 50)


# ==================================================
# 3) website içindeki "tr" ifadesini alın.
# ==================================================

result = website[-2:]

print("3. Son iki karakter:", result)

# Negatif index sondan başlar.
#
# -1 -> son karakter
# -2 -> sondan ikinci karakter

print("-" * 50)


# ==================================================
# 4) course değişkeninin
#    ilk 15 ve son 15 karakterini alın.
# ==================================================

first_part = course[:15]
last_part = course[-15:]

print("4. İlk 15 karakter :", first_part)
print("4. Son 15 karakter :", last_part)

# [:15]
# Baştan başlar.

# [-15:]
# Sondan 15 karakter alır.

print("-" * 50)


# ==================================================
# 5) course ifadesini tersten yazdırın.
# ==================================================

result = course[::-1]

print("5. Tersten Yazılışı:", result)

# [başlangıç:bitiş:adım]
#
# Adım = -1
# sondan başa doğru ilerler.

print("-" * 50)


# ==================================================
# 6) String Formatlama
# ==================================================

name = "Özgür"
surname = "Kavak"
age = 22
job = "Yazılım Geliştirici"

# Yöntem 1 (String Birleştirme)

result = "Benim adım " + name + " " + surname + \
         ". Yaşım " + str(age) + " ve mesleğim " + job + "."

print(result)

print()

# Yöntem 2 (.format())

result = "Benim adım {} {}. Yaşım {} ve mesleğim {}.".format(
    name,
    surname,
    age,
    job
)

print(result)

print()

# Yöntem 3 (f-string)  ✅ En çok kullanılan yöntem

result = f"Benim adım {name} {surname}. Yaşım {age} ve mesleğim {job}."

print(result)

print("-" * 50)


# ==================================================
# 7) replace()
# ==================================================

text = "hello world"

result = text.replace("w", "W")

print("7. replace() sonucu:", result)

# replace(eski, yeni)

print("-" * 50)


# ==================================================
# 8) String Çarpma
# ==================================================

result = course * 3

print(result)

# Stringleri sayıyla çarparsan
# aynı ifade belirtilen sayı kadar tekrar edilir.

print("-" * 50)