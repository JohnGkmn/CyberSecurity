#!/usr/bin/python3
# -*- coding: utf-8 -*-*
# Author Gökmen DEMİR
# Vade hesaplama CLI versiyon
# dosyayı buraya kopya /usr/local/bin/
# Terminale Gcalc.py -v vadeTürü ile hesaplama yapabilirsin.
import argparse
#import os
#os.system("Gcalc.py")

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--vade", required=True, help=("Vade türü: Gün(g) / Ay(a) / Yıl(y)"))
args = vars(ap.parse_args())
#print("Girilen Tür  {}.".format(args["vade"]))

kazanc = 0.0
toplam = 0.0
toplamKar = 0.0
anaPara = input("Ana Para: ")
#vade = input("Faiz Getirisi {Günlük(g) / Aylık(a) / Yıllık(y) } : ")

if args["vade"] == "g":
    faizOrani = input("Günlük Faiz Oranı: %")
    gunSayisi = input("Faiz Gün Sayısı: ")
    toplam = (float(anaPara) / 100) * (float(faizOrani) / 365) * float(gunSayisi)
    kazanc = toplam - (toplam * 0.15)
    toplamKar = float(anaPara) + kazanc
    print("-----o-----\n")
    print("Ana Para: " + str(anaPara))
    print("Brüt Kazanç:" + str(toplam))
    print("Kazanç: " + str(kazanc))
    print("Toplam: " + str(toplamKar))

elif args["vade"] == "a":
    faizOrani = input("Aylık Faiz Oranı: %")
    aySayisi = input("Faiz Ay Sayısı: ")
    toplam = (float(anaPara) / 100) * (float(faizOrani) / 12) * float(aySayisi)
    kazanc = toplam - (toplam * 0.15)
    toplamKar = float(anaPara) + kazanc
    print("-----o-----\n")
    print("Ana Para: " + str(anaPara))
    print("Brüt Kazanç:" + str(toplam))
    print("Kazanç: " + str(kazanc))
    print("Toplam: " + str(toplamKar))

elif args["vade"] == "y":
    faizOrani = input("Yıllık Faiz Oranı: %")
    yilSayisi = input("Faiz Yıl Sayısı: ")
    toplam = (float(anaPara) / 100) * float(faizOrani) * float(yilSayisi)
    kazanc = toplam - (toplam * 0.15)
    toplamKar = float(anaPara) + kazanc
    print("-----o-----\n")
    print("Ana Para: " + str(anaPara))
    print("Brüt Kazanç:" + str(toplam))
    print("Kazanç: " + str(kazanc))
    print("Toplam: " + str(toplamKar))

else:
    print("Lütfen g / a / y seçimlerininden birini yapınız.")
