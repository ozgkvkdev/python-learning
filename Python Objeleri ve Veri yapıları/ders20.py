# ============================================================
# Ders 20 - Value Type ve Reference Type
#
# Bu derste:
# - Value Type (Değer Tipleri)
# - Reference Type (Referans Tipleri)
# ============================================================


# ==========================
# Value Type (Değer Tipleri)
# ==========================

x = 10
y = 20

x = y
y = 30

print(x)
print(y)

# Çıktı
# 20
# 30

# Açıklama:
# Değer tiplerinde değişkenler birbirinden bağımsızdır.
# Birinin değişmesi diğerini etkilemez.


print("-" * 40)


# =============================
# Reference Type (Referans Tipleri)
# =============================

listA = ["BMW", "Mercedes"]
listB = ["BMW", "Mercedes"]

listA = listB
listB.append("Toyota")

print(listA)
print(listB)

# Çıktı
# ['BMW', 'Mercedes', 'Toyota']
# ['BMW', 'Mercedes', 'Toyota']

# Açıklama:
# listA ve listB aynı listeyi göstermektedir.
# listB üzerinde yapılan değişiklik listA'yı da etkiler.


print("-" * 40)


# =============================
# Kopyalama İşlemi
# =============================

list1 = ["Python", "Java"]
list2 = list1.copy()

list2.append("C#")

print(list1)
print(list2)

# Çıktı
# ['Python', 'Java']
# ['Python', 'Java', 'C#']

# Açıklama:
# copy() metodu ile bağımsız bir kopya oluşturulur.
# Böylece yapılan değişiklikler diğer listeyi etkilemez.