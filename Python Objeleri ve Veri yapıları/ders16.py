# ============================================================
# Ders 16 - Tuple (Demet)
#
# Bu derste:
# - Tuple oluşturma
# - Tuple elemanlarına erişme
# - count() metodu
# - index() metodu
# - Tuple ile List arasındaki fark
# ============================================================


# Tuple oluşturma
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Farklı veri tipleri
person = ("Özgür", "Kavak", 22, "Yazılım Geliştirici")
print(person)

# Elemanlara erişme
print(person[0])
print(person[-1])

# Tuple uzunluğu
print(len(person))

# count() metodu
numbers = (10, 20, 30, 10, 40, 10)
print(numbers.count(10))

# index() metodu
print(numbers.index(30))

# Tuple değiştirilemez
colors = ("Kırmızı", "Mavi", "Yeşil")
print(colors)

# Liste ile Tuple farkı
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)

print(type(list_example))
print(type(tuple_example))