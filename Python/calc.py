#   Author : Gökmen DEMİR
#
# Vadeli mevduat faiz hesaplama / basit bir deneme
# Önce yatıraacağınız para miktarını giriniz (ana para)
# Faiz türünü g , a , y  ' dan birini seçerek yazınız
# Faiz oranını % olarak giriniz.
# Ne kadar süreyle faiz göreceğini giriniz.
# -*- coding: utf-8 -*-*
kazanc = 0.0
toplam = 0.0
toplamKar = 0.0
anaPara = input("Ana Para: ")
vade = input("Faiz Getirisi {Günlük(g) / Aylık(a) / Yıllık(y) } : ")

print(type(vade))

if vade == "g":
    faizOrani = input("Günlük Faiz Oranı: %")
    gunSayisi = input("Faiz Gün Sayısı: ")
    toplam = (float(anaPara) / 100) * (float(faizOrani) / 365) * float(gunSayisi)
    kazanc = toplam - (toplam * 0.15)
    toplamKar = float(anaPara) + kazanc
    print("-----o-----\n")
    print("Ana Para: " + anaPara)
    print("Brüt Kazanç:" + str(toplam))
    print("Kazanç: " + str(kazanc))
    print("Toplam: " + str(toplamKar))

elif vade == "a":
    faizOrani = input("Aylık Faiz Oranı: %")
    aySayisi = input("Faiz Ay Sayısı: ")
    toplam = (float(anaPara) / 100) * (float(faizOrani) / 12) * float(aySayisi)
    kazanc = toplam - (toplam * 0.15)
    toplamKar = float(anaPara) + kazanc
    print("-----o-----\n")
    print("Ana Para: " + anaPara)
    print("Brüt Kazanç:" + str(toplam))
    print("Kazanç: " + str(kazanc))
    print("Toplam: " + str(toplamKar))

elif vade == "y":
    faizOrani = input("Yıllık Faiz Oranı: %")
    yilSayisi = input("Faiz Yıl Sayısı: ")
    toplam = (float(anaPara) / 100) * float(faizOrani) * float(yilSayisi)
    kazanc = toplam - (toplam * 0.15)
    toplamKar = float(anaPara) + kazanc
    print("-----o-----\n")
    print("Ana Para: " + anaPara)
    print("Brüt Kazanç:" + str(toplam))
    print("Kazanç: " + str(kazanc))
    print("Toplam: " + str(toplamKar))

else:
    print("Lütfen g / a / y seçimlerininden birini yapınız.")



# Yeni versiyon hedefleri:
# ->Bileşik faiz hesaplama özelliği
# ->Menü şeklinde ilk giriş ekranı
# ->Çıkış yapana kadar tekrar tekrar hesaplama