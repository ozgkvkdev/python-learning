def harf_notu_hesapla(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    elif ortalama >= 50:
        return "FD"
    else:
        return "FF"


def ortalamaları_oku():
    try:
        with open("sınav_notları.txt", "r", encoding="utf-8") as file:
            print("\n--- ÖĞRENCİ NOTLARI VE ORTALAMALARI ---")
            for satir in file:
                satir = satir.strip()
                if not satir:  # Boş satırları atla
                    continue
                
                # "İsim Soyisim:not1,not2,not3" formatını parçalıyoruz
                parcalari = satir.split(":")
                ogrenci_adi = parcalari[0]
                notlar_str = parcalari[1].split(",")
                
                # int yerine float() kullanılarak '100.0' gibi değerlerin çökmesi engellendi
                not1 = float(notlar_str[0])
                not2 = float(notlar_str[1])
                not3 = float(notlar_str[2])
                
                # Ortalama hesaplama
                ortalama = (not1 + not2 + not3) / 3
                harf = harf_notu_hesapla(ortalama)
                
                print(f"{ogrenci_adi} -> Ortalama: {ortalama:.2f} | Harf Notu: {harf}")
            print("---------------------------------------")
    except FileNotFoundError:
        print("\nHenüz kaydedilmiş bir not bulunamadı. Lütfen önce not giriniz.")


def not_gir():
    ad = input("öğrenci adı: ")
    soy_ad = input("öğrenci soyadı: ")
    not1 = float(input("not 1: "))  # Gelecekte de noktalı not girilebilmesi için float yapıldı
    not2 = float(input("not 2: "))
    not3 = float(input("not 3: "))

    with open("sınav_notları.txt", "a", encoding="utf-8") as file:
        file.write(f"{ad} {soy_ad}:{not1},{not2},{not3}\n")
    print(f"{ad} {soy_ad} başarıyla eklendi.")


def notları_kayıt_et():
    try:
        with open("sınav_notları.txt", "r", encoding="utf-8") as file_in, \
             open("ortalamalar.txt", "w", encoding="utf-8") as file_out:
            
            for satir in file_in:
                satir = satir.strip()
                if not satir:
                    continue
                parcalari = satir.split(":")
                ogrenci_adi = parcalari[0]
                notlar_str = parcalari[1].split(",")
                
                # Burada da dönüşümler float() olarak güncellendi
                not1 = float(notlar_str[0])
                not2 = float(notlar_str[1])
                not3 = float(notlar_str[2])
                
                ortalama = (not1 + not2 + not3) / 3
                harf = harf_notu_hesapla(ortalama)
                
                file_out.write(f"{ogrenci_adi} -> Ortalama: {ortalama:.2f} | Harf Notu: {harf}\n")
        print("\nOrtalamalar başarıyla 'ortalamalar.txt' dosyasına kaydedildi!")
    except FileNotFoundError:
        print("\nKaynak dosya (sınav_notları.txt) bulunamadı. Önce not girmelisiniz.")


# ANA PROGRAM DÖNGÜSÜ
while True:
    islem = input("\n1-Notları oku ve hesapla \n2-Not gir \n3-Ortalamaları dosyaya kaydet \n4-Çıkış\nSeçiminiz: ")
    if islem == "1":
        ortalamaları_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notları_kayıt_et()
    elif islem == "4":  
        print("Programdan çıkış yapılıyor...")
        break
    else:
        print("Yanlış bir işlem seçtiniz.")