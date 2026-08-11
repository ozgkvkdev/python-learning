# # dosya okuma işlemleri için read() fonksiyonu kullanılır. 

# file = open("ornek.txt","r", encoding="utf-8")   # dosya okundu

# # for döngüsü ile dosya içeriğini satır satır ekrana yazdırmak için dosya nesnesi üzerinde iterasyon yapılabilir.
# for i in file:
#     print(i,end="") # dosya içeriğini ekrana yazdır end parametresi ile satır sonuna ekleme yapılmaz
# file.close() # dosya kapatıldı  

# content = file.read() # dosya içeriğini tek seferde okur ve bir string olarak döndürür.
# print(content) # dosya içeriğini ekrana yazdır


# from click import File


# content = File.readline() # type: ignore # dosya içeriğini satır satır okur ve bir liste olarak döndürür.
# print(content) # dosya içeriğini ekrana yazdır


# liste = file.readlines() # dosya içeriğini satır satır okur ve bir liste olarak döndürür.
# print(liste) # dosya içeriğini ekrana yazdır

