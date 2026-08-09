liste=["1","2","5a","10b","abc","10","50"]

# soru1 liste elemanları içindeki sayısal degerleri bulunuz

for x in liste:
    try:
        result=int (x)
        print(result)
    except ValueError:
      continue    




# soru 2 kullanıcı "q"  degerini girmedikçe aldıgınız her inputun sayı olup olmadığından emin olunuz.

while True:
   sayi=input("sayı:")
   if sayi == "q":
      break

   try:
      result = float(sayi)
      print(f"Girdiğiniz sayı: {result}")
   except ValueError:
      print("geçersiz sayı")
      continue  




# soru 3 girilen  paralo içinde türkçe karakter hatası veriniz.

turkce_karakterler = "çğıöşüÇĞİÖŞÜ"

parola = input("Parola giriniz: ")
for i in parola:
   if i in turkce_karakterler:
      raise TypeError("parola türke karakter içeremez")
   else:
      pass

print("parola geçerli")   



# soru 4 faktoriyel fonksiyonu oluşturup fonksiyona gelen deger hata mesajı veriniz.


def faktoriyel(n):
   n = int(n)
   if n < 0:
        raise ValueError("Negatif sayıların faktöriyeli alınamaz.")
   elif n == 0 or n == 1:
        return 1
   else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

   

