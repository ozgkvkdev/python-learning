# ============================================================
# Ders 17 - Dictionary (Sözlük)
#
# Bu derste:
# - Dictionary oluşturma
# - Veri ekleme
# - Veri güncelleme
# - Veri silme
# - keys(), values(), items()
# ============================================================


student = {
    "name": "Özgür",
    "surname": "Kavak",
    "age": 22,
    "city": "Adana"
}

print(student)

# Veri okuma
print(student["name"])
print(student["surname"])

# Veri ekleme
student["job"] = "Yazılım Geliştirici"

# Veri güncelleme
student["age"] = 23

# Veri silme
student.pop("city")

print(student)

# Anahtarlar
print(student.keys())

# Değerler
print(student.values())

# Anahtar - Değer
print(student.items())