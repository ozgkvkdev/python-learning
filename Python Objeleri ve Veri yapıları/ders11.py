website = "https://www.python.org/tr"
course = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama"

# ------------------------------------------------------------
# PYTHON STRING METOTLARI ALIŞTIRMALARI
# Bu dosya, Python'da string (karakter dizisi) metotlarını
# öğrenmek amacıyla hazırlanmıştır.
# ------------------------------------------------------------

# 1. "HELLO WORLD" ifadesini tamamen küçük harfe çevirin.
# lower() metodu tüm karakterleri küçük harfe dönüştürür.

result = "HELLO WORLD".lower()
print("1. Soru:", result)

print("-" * 60)

# 2. "www.python.org" ifadesinden sadece "python" kısmını alın.
# String dilimleme (Slice) kullanılmıştır.

result = "www.python.org"[4:10]
print("2. Soru:", result)

print("-" * 60)

# 3. course değişkenindeki tüm harfleri küçük harfe çevirin.
# lower() metodu büyük harfleri küçük harfe dönüştürür.

result = course.lower()
print("3. Soru:", result)

print("-" * 60)

# 4. website değişkeninde kaç tane "e" harfi olduğunu bulun.
# count() metodu belirtilen karakterin kaç kez geçtiğini sayar.

result = website.count("e")
print("4. Soru:", result)

print("-" * 60)

# 5. website değişkeni "https" ile başlayıp "tr" ile bitiyor mu?
# startswith() ve endswith() metotları True veya False döndürür.

print("5. Soru (Başlangıç):", website.startswith("https"))
print("5. Soru (Bitiş):", website.endswith("tr"))

print("-" * 60)

# 6. website değişkeninde ".org" ifadesi var mı?
# find() metodu aranan ifadeyi bulursa başlangıç indexini,
# bulamazsa -1 değerini döndürür.

result = website.find(".org")
print("6. Soru:", result)

print("-" * 60)

# 7. course değişkenindeki tüm karakterler alfabetik mi?
# isalpha() metodu yalnızca harflerden oluşan ifadelerde True döndürür.
# course değişkeninde boşluk ve ":" karakteri bulunduğu için sonuç False olur.

result = course.isalpha()
print("7. Soru:", result)

print("-" * 60)

# 8. "contents" ifadesini 50 karakter genişliğinde ortalayın.
# Boş kalan alanları "*" karakteri ile doldurun.

result = "contents".center(50, "*")
print("8. Soru:", result)

print("-" * 60)

# 9. course değişkenindeki tüm boşluk karakterlerini "-" ile değiştirin.
# replace() metodu belirtilen ifadeyi başka bir ifade ile değiştirir.

result = course.replace(" ", "-")
print("9. Soru:", result)

print("-" * 60)

# 10. "hello world" ifadesindeki "world" kelimesini "there" ile değiştirin.

result = "hello world".replace("world", "there")
print("10. Soru:", result)