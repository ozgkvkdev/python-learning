# ============================================================
# Ders 18 - Dictionary Uygulaması
#
# Kullanıcıdan öğrenci bilgileri alınır.
# Bilgiler dictionary içerisinde saklanır.
# Daha sonra öğrenci numarası girilerek bilgiler görüntülenir.
# ============================================================


students = {}

for i in range(2):
    number = input("Öğrenci Numarası : ")

    students[number] = {
        "Ad": input("Öğrenci Adı : "),
        "Soyad": input("Öğrenci Soyadı : "),
        "Telefon": input("Telefon : ")
    }

print("\nKayıt Tamamlandı")
print("-" * 40)

search = input("Bilgilerini görmek istediğiniz öğrenci numarası : ")

print("\nÖğrenci Bilgileri")
print("-" * 40)

print("Numara :", search)
print("Ad :", students[search]["Ad"])
print("Soyad :", students[search]["Soyad"])
print("Telefon :", students[search]["Telefon"])