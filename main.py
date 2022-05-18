import random
sayacmilan1=0
sayacmilan2=0
sayacfenerbahçe1=0
sayacfenerbahçe2=0
sayacunited1=0
sayacunited2=0
sayaclyon1=0
sayaclyon2=0

#1. HAFTA
i=0
while i<100:
    Fenerbahçe_puan = 0
    Milan_puan = 0
    Lyon_puan = 0
    United_puan = 0
    # Fenerbahçe Milan Maçı ---Fenerbahçe Ev sahibi
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.3:
        Fenerbahçe_puan = Fenerbahçe_puan + 3
    elif rassal_deger > 0.8:
        Milan_puan = Milan_puan + 3
    else:
        Fenerbahçe_puan = Fenerbahçe_puan + 1
        Milan_puan = Milan_puan + 1

    # lYON-United Maçı----Lyon Ev sahibi
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.6:
        Lyon_puan = Lyon_puan + 3
    elif rassal_deger > 0.9:
        United_puan = United_puan + 3
    else:
        Lyon_puan = Lyon_puan + 1
        United_puan = United_puan + 1

    # 2.HAFTA
    # United-Fenerbahçe
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.6:
        United_puan = United_puan + 3
    elif rassal_deger > 0.9:
        Fenerbahçe_puan = Fenerbahçe_puan + 3
    else:
        United_puan = United_puan + 1
        Fenerbahçe_puan = Fenerbahçe_puan + 1

    # Lyon-Milan
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.4:
        Lyon_puan = Lyon_puan + 3
    elif rassal_deger > 0.7:
        Milan_puan = Milan_puan + 3
    else:
        Lyon_puan = Lyon_puan + 1
        United_puan = United_puan + 1

    # 3.Hafta
    # Milan-United
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.5:
        Milan_puan = Milan_puan + 3
    elif rassal_deger > 0.9:
        United_puan = United_puan + 3
    else:
        Milan_puan = Milan_puan + 1
        United_puan = United_puan + 1

    # Lyon-Fenerbahçe

    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.5:
        Lyon_puan = Lyon_puan + 3
    elif rassal_deger > 0.9:
        Fenerbahçe_puan = Fenerbahçe_puan + 3
    else:
        Lyon_puan = Lyon_puan + 1
        Fenerbahçe_puan = Fenerbahçe_puan + 1

    # 4.hafta
    # Fenerbahçe-United
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.5:
        Fenerbahçe_puan = Fenerbahçe_puan + 3
    elif rassal_deger > 0.8:
        Fenerbahçe_puan = Fenerbahçe_puan + 0
        United_puan = United_puan + 3
    else:
        Fenerbahçe_puan = Fenerbahçe_puan + 1
        United_puan = United_puan + 1

    # Milan-Lyon
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)
    if rassal_deger < 0.6:
        Milan_puan = Milan_puan + 3
    elif rassal_deger > 0.8:
        Lyon_puan = Lyon_puan + 3
    else:
        Milan_puan = Milan_puan + 1
        Lyon_puan = Lyon_puan + 1

    # 5.HAFTA
    # Milan-Fenerbahçe
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)
    if rassal_deger < 0.7:
        Milan_puan = Milan_puan + 3
    elif rassal_deger > 0.9:
        Fenerbahçe_puan = Fenerbahçe_puan + 3
    else:
        Milan_puan = Milan_puan + 1
        Fenerbahçe_puan = Fenerbahçe_puan + 1

    # United-Lyon
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)
    if rassal_deger < 0.3:
        United_puan = United_puan + 3
    elif rassal_deger > 0.8:
        Lyon_puan = Lyon_puan + 3
    else:
        United_puan = United_puan + 1
        Lyon_puan = Lyon_puan + 1

    # 6.HAFTA
    # Fenerbahçe-Lyon
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)

    if rassal_deger < 0.4:
        Fenerbahçe_puan = Fenerbahçe_puan + 3
    elif rassal_deger > 0.7:
        Lyon_puan = Lyon_puan + 3
    else:
        Fenerbahçe_puan = Fenerbahçe_puan + 1
        Lyon_puan = Lyon_puan + 1

    # United-Milan
    rassal_deger = random.uniform(0, 1)
    print(rassal_deger)
    if rassal_deger < 0.4:
        United_puan = United_puan + 3
    elif rassal_deger > 0.8:
        Milan_puan = Milan_puan + 3
    else:
        United_puan = United_puan + 1
        Milan_puan = Milan_puan + 1

    Milan_birincilik = 0
    Milan_ikincilik = 0
    Fenerbahçe_birincilik = 0
    Fenerbahçe_ikincilik = 0
    United_birincilik = 0
    United_ikincilik = 0
    Lyon_birincilik = 0
    Lyon_ikincilik = 0

    # Milan_puan=6
    # Fenerbahçe_puan=8
    # Lyon_puan=7
    # United_puan=8

    print("Milan Puan: ", Milan_puan)
    print("Fenerbahçe Puan: ", Fenerbahçe_puan)
    print("Lyon Puan:", Lyon_puan)
    print("United Puan: ", United_puan)
    print("-----------------")

    if Milan_puan > Fenerbahçe_puan and Milan_puan > Lyon_puan and Milan_puan > United_puan:
        Milan_birincilik = Milan_birincilik + 1
        if Fenerbahçe_puan > Lyon_puan and Fenerbahçe_puan > United_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if United_puan > Lyon_puan and United_puan > Fenerbahçe_puan:
            United_ikincilik = United_ikincilik + 1
        if Fenerbahçe_puan == Lyon_puan and Fenerbahçe_puan > United_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Lyon_puan == United_puan and Lyon_puan > Fenerbahçe_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if Lyon_puan > Fenerbahçe_puan and Lyon_puan > United_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if Fenerbahçe_puan == United_puan and Fenerbahçe_puan > Lyon_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Fenerbahçe_puan == United_puan == Lyon_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
    elif Lyon_puan == United_puan and Lyon_puan > Milan_puan and Lyon_puan > Fenerbahçe_puan:  # Lyon united eşitse 1 ve 2
        Lyon_birincilik = Lyon_birincilik + 1
        United_ikincilik = United_ikincilik + 1
    elif Fenerbahçe_puan == Lyon_puan and Fenerbahçe_puan > Milan_puan and Fenerbahçe_puan > United_puan:  # Lyon Fener eşit 1 ve 2 yse
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Lyon_ikincilik = Lyon_ikincilik + 1
    elif Milan_puan == Fenerbahçe_puan and Milan_puan > Lyon_puan and Milan_puan > United_puan:  # Milanla Fenerin puanı eşit olursa ilk 2 sıra olarak.
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Milan_ikincilik = Milan_ikincilik + 1
    elif Milan_puan > Fenerbahçe_puan and Milan_puan == Lyon_puan and Milan_puan > United_puan:  # Milanla Lyon eşit puan ise ilk 2 sıra olarak
        Lyon_birincilik = Lyon_birincilik + 1
        Milan_ikincilik = Milan_ikincilik + 1
    elif Milan_puan > Fenerbahçe_puan and Milan_puan > Lyon_puan and Milan_puan == United_puan: #Milanla United eşit puan ise ilk 2 sıra olarak
        Milan_birincilik = Milan_birincilik + 1
        United_ikincilik = United_ikincilik + 1
    elif Milan_puan < Fenerbahçe_puan and Milan_puan == Lyon_puan and Milan_puan == United_puan: #SON 3 ÜN PUANLARI EŞİT OLURSA
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Lyon_ikincilik = Lyon_ikincilik + 1
    elif Fenerbahçe_puan == United_puan and Fenerbahçe_puan > Lyon_puan and Fenerbahçe_puan > Milan_puan:#Fener-United Eşit ilk 2 sıra
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        United_ikincilik = United_ikincilik + 1
    elif Milan_puan == Fenerbahçe_puan and Milan_puan == Lyon_puan and Milan_puan == United_puan:  # Herkesin Puanları Eşit olursa
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Lyon_ikincilik = Lyon_ikincilik + 1
    elif Milan_puan == Fenerbahçe_puan == United_puan and Milan_puan > Lyon_puan:  # 3ünün puanları eşit olursa İLK 3
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Milan_ikincilik = Milan_ikincilik + 1
    elif Milan_puan == Fenerbahçe_puan == Lyon_puan and Milan_puan > United_puan:  # 3ünün puanları eşit olursa İLK 3
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Lyon_ikincilik = Lyon_ikincilik + 1
    elif Milan_puan == United_puan == Lyon_puan and Milan_puan > Fenerbahçe_puan:  # 3ünün puanları eşit olursa İLK 3
        Lyon_birincilik = Lyon_birincilik + 1
        Milan_ikincilik = Milan_ikincilik + 1
    elif United_puan == Lyon_puan == Fenerbahçe_puan and United_puan > Milan_puan:  # 3ünün puanları eşit olursa İLK 3
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        Lyon_ikincilik = Lyon_ikincilik + 1

    elif Lyon_puan > Milan_puan and Lyon_puan > Fenerbahçe_puan and Lyon_puan > United_puan:  # Lyon Hepsinden büykken
        Lyon_birincilik = Lyon_birincilik + 1
        if Fenerbahçe_puan > Milan_puan and Fenerbahçe_puan > United_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Milan_puan > Fenerbahçe_puan and Milan_puan > United_puan:
            Milan_ikincilik = Milan_ikincilik + 1
        if United_puan > Milan_puan and United_puan > Fenerbahçe_puan:
            United_ikincilik = United_ikincilik + 1
        if Milan_puan == Fenerbahçe_puan and Milan_puan > United_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Milan_puan == United_puan and Milan_puan > Fenerbahçe_puan:
            Milan_ikincilik = Milan_ikincilik + 1
        if Fenerbahçe_puan == United_puan and Fenerbahçe_puan > Milan_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Fenerbahçe_puan == Milan_puan == United_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
    elif United_puan > Milan_puan and United_puan > Fenerbahçe_puan and United_puan > Lyon_puan:  # United Hepsinden Büyükken
        United_birincilik = United_birincilik + 1
        if Lyon_puan > Fenerbahçe_puan and Lyon_puan > Milan_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if Fenerbahçe_puan > Lyon_puan and Fenerbahçe_puan > Milan_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Milan_puan > Fenerbahçe_puan and Milan_puan > Lyon_puan:
            Milan_ikincilik = Milan_ikincilik + 1
        if Fenerbahçe_puan == Lyon_puan and Fenerbahçe_puan > Milan_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Fenerbahçe_puan == Milan_puan and Fenerbahçe_puan > Lyon_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1
        if Lyon_puan == Milan_puan and Lyon_puan > Fenerbahçe_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if Fenerbahçe_puan == Milan_puan == Lyon_puan:
            Fenerbahçe_ikincilik = Fenerbahçe_ikincilik + 1

    elif Fenerbahçe_puan > Milan_puan and Fenerbahçe_puan > United_puan and Fenerbahçe_puan > Lyon_puan:  # Fener hepsinden Büyükken
        Fenerbahçe_birincilik = Fenerbahçe_birincilik + 1
        if Milan_puan == United_puan and Milan_puan > Lyon_puan:
            Milan_ikincilik = Milan_ikincilik + 1
        if Milan_puan == Lyon_puan and Milan_puan > United_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if United_puan == Lyon_puan and United_puan > Milan_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if Milan_puan > United_puan and Milan_puan > Lyon_puan:
            Milan_ikincilik = Milan_ikincilik + 1
        if Lyon_puan > United_puan and Lyon_puan > Milan_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1
        if United_puan > Lyon_puan and United_puan > Milan_puan:
            United_ikincilik = United_ikincilik + 1
        if Milan_puan == Lyon_puan == United_puan:
            Lyon_ikincilik = Lyon_ikincilik + 1

    Milan_birincilik_toplam = Milan_birincilik
    Milan_ikincilik_toplam = Milan_ikincilik
    Fenerbahçe_birincilik_toplam = Fenerbahçe_birincilik
    Fenerbahçe_ikincilik_toplam = Fenerbahçe_ikincilik
    United_birincilik_toplamı = United_birincilik
    United_ikincilik_toplamı = United_ikincilik
    Lyon_birincilik_toplamı = Lyon_birincilik
    Lyon_ikincilik_toplamı = Lyon_ikincilik

    if Milan_birincilik==1:
       sayacmilan1=sayacmilan1+1
    if Milan_ikincilik==1:
        sayacmilan2=sayacmilan2+1
    if Fenerbahçe_birincilik==1:
        sayacfenerbahçe1=sayacfenerbahçe1+1
    if Fenerbahçe_ikincilik==1:
        sayacfenerbahçe2=sayacfenerbahçe2+1
    if United_birincilik==1:
        sayacunited1=sayacunited1+1
    if United_ikincilik==1:
        sayacunited2=sayacunited2+1
    if Lyon_birincilik==1:
        sayaclyon1=sayaclyon1+1
    if Lyon_ikincilik==1:
        sayaclyon2=sayaclyon2+1


    i=i+1



print("Milan 1. olma sayısı:",sayacmilan1)
print("Milan 2. olma sayısı:",sayacmilan2)
print("Fener 1. olma sayısı:",sayacfenerbahçe1)
print("Fener 2. olma sayısı:",sayacfenerbahçe2)
print("United 1. olma sayısı:",sayacunited1)
print("United 2. olma sayısı:",sayacunited2)
print("Lyon 1. olma sayısı:",sayaclyon1)
print("Lyon 2. olma sayısı:",sayaclyon2)
print("----------------------")


print("TOPLAM 1.'lik sayısı: ",sayacmilan1+sayaclyon1+sayacunited1+sayacfenerbahçe1)
print("TOPLAM 2.'lik sayısı: ",sayaclyon2+sayacunited2+sayacfenerbahçe2+sayacmilan2)
toplam_birincilikler=sayacmilan1+sayaclyon1+sayacunited1+sayacfenerbahçe1
toplam_ikincilikler=sayaclyon2+sayacunited2+sayacfenerbahçe2+sayacmilan2
print("TOPLAM 1 VEYA 2.'cilik sayısı: ",toplam_birincilikler+toplam_ikincilikler)

print("-----------------------")
Milan_tur_gecme=(sayacmilan1+sayacmilan2)/i
Fenerbahçe_tur_gecme=(sayacfenerbahçe1+sayacfenerbahçe2)/i
United_tur_gecme=(sayacunited1+sayacunited2)/i
Lyon_tur_gecme=(sayaclyon1+sayaclyon2)/i
print("Milan Tur geçme olasılığı:",Milan_tur_gecme)
print("FenerBahçe Turu geçme olasığı:",Fenerbahçe_tur_gecme)
print("United Turu geçme Olasılığı",United_tur_gecme)
print("Lyon Turu geçme Olasılığı",Lyon_tur_gecme)
print("-----------------")
print("ORAN TOPLAM=",Milan_tur_gecme+Fenerbahçe_tur_gecme+United_tur_gecme+Lyon_tur_gecme)