# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır. open() fonksiyonu ile dosya açarken, dosya modunu belirlemek gerekir. Dosya modları şunlardır:
# 'w' : yazma modu (varsa dosya içeriğini siler, yoksa yeni dosya oluşturur)
# 'a' : ekleme modu (varsa dosya içeriğini silmeden ekleme yapar, yoksa yeni dosya oluşturur)
# 'x' : oluşturma modu (varsa hata verir, yoksa yeni dosya oluşturur)
# 'r' : okuma modu (varsayılan)


#=========================================#

# file = open("ornek.txt","w") # dosya açıldı
# file.close() # dosya kapatıldı

# file = open("C:\\Users\\User\\Desktop\\ornek.txt","w") # dosya açıldı
# file.close() # dosya kapatıldı

#=========================================#

# file = open("ornek2.txt","w") # dosya açıldı
# file.write("Python ile dosya yönetimi öğreniyorum.\n") # dosyaya yaz
# file.close() # dosya kapatıldı

#=========================================#

# file = open("ornek3.txt","w", encoding="utf-8") # dosya açıldı türkçe karakterler için encoding parametresi eklendi
# file.write("Python ile dosya yönetimi öğreniyorum.\n") # dosyaya yaz
# file.close() # dosya kapatıldı


#=========================================#

# file = open("ornek4.txt","a", encoding="utf-8")   # dosya eklendi 
# file.write("Python ile dosya yönetimi öğreniyorum.\n") # dosyaya yaz
# file.close() # dosya kapatıldı


#=========================================#

# file = open("ornek5.txt","x", encoding="utf-8")   # dosya oluşturuldu
# file.close() # dosya kapatıldı
# # x modu ile dosya oluşturulurken, eğer dosya zaten varsa hata verir.


#=========================================#

file = open("ornek6.txt","r", encoding="utf-8")   # dosya okundu
print(file.read()) # dosya içeriğini ekrana yazdır
file.close() # dosya kapatıldı

# r modu ile dosya okuma işlemi yapılırken, eğer dosya yoksa hata verir.    
