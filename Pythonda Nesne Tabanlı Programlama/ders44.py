# ==================
#PYTHON NESNE TABANLI PROGRAMLAMA (OOP)
#===================
# DERS 1 :

# class "sınıf"   oluşturma


class Araba:       # araba adında bir sınıf oluşturduk   "ilk harfi büyük olması daha iyi olur"

    # Constructor Metodu

    def __init__(self,marka,model,yil):    
      self.marka=marka
      self.model=model 
      self.yil=yil

    def bilgileri_goster(self):

        print("==ARAÇ BİLGİLERİ==")
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Yıl: {self.yil}")

# nesneleri oluşturma

araba1=Araba("Bmw","M4","2017")
araba2=Araba("Şahin","Q5","1999")
araba3=Araba("Auodi","xxx","2026")

# metod çağırma

araba1.bilgileri_goster()
araba2.bilgileri_goster()
araba3.bilgileri_goster()
