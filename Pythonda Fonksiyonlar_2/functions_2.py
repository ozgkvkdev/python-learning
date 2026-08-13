#   FONKSİYONDA FONKSİYON DÖNDERME KULLANIMI

def islem_olustur(islem):

    def toplama(a, b):
        return a + b

    def cikarma(a, b):
        return a - b

    def carpma(a, b):
        return a * b

    def bolme(a, b):
        if b == 0:
            return "Sıfıra bölme yapılamaz."
        return a / b

    if islem == "toplama":
        return toplama

    elif islem == "cikarma":
        return cikarma

    elif islem == "carpma":
        return carpma

    elif islem == "bolme":
        return bolme

    return None


toplama_islemi = islem_olustur("toplama")
cikarma_islemi = islem_olustur("cikarma")
carpma_islemi = islem_olustur("carpma")
bolme_islemi = islem_olustur("bolme")


print("Toplama:", toplama_islemi(10, 5)) # type: ignore
print("Çıkarma:", cikarma_islemi(10, 5)) # type: ignore
print("Çarpma:", carpma_islemi(10, 5)) # type: ignore
print("Bölme:", bolme_islemi(10, 5)) # type: ignore