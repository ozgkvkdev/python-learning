# fonksiyona parametre olarak göndereceğiz.

def siparis_hesapla(urun_adi, fiyat, adet):
    toplam = fiyat * adet

    print(f"Ürün: {urun_adi}")
    print(f"Birim fiyat: {fiyat} TL")
    print(f"Adet: {adet}")
    print(f"Toplam tutar: {toplam} TL")


siparis_hesapla("Kahve", 150, 3)