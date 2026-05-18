# 🛡️ Omnikit Security Toolkit

<div align="center">

![Omnikit Logo](omnikit.png)

**Kapsamlı Siber Güvenlik Araç Seti**

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Jizek/Omnikit-Security-Toolkit?style=social)](https://github.com/Jizek/Omnikit-Security-Toolkit/stargazers)

[English](#english) | [Türkçe](#turkish)

</div>

---

<a name="turkish"></a>
## 🇹🇷 Türkçe

### ⚠️ Yasal Uyarı ve Sorumluluk Reddi

> Bu araç yalnızca **eğitim**, **öğretim** ve **siber güvenlik bilincini artırma** amaçlarıyla geliştirilmiştir.

**ÖNEMLİ:** Bu araçla gerçekleştireceğiniz tüm işlemlerin **sorumluluğu tamamen size aittir**. Geliştirici ve GitHub platformu hiçbir hukuki veya etik yükümlülük kabul etmez.

### 📖 Hakkında

**Omnikit**, siber güvenlik profesyonelleri, penetrasyon testçileri ve güvenlik araştırmacıları için geliştirilmiş kapsamlı bir araç setidir. 50'den fazla güvenlik aracını tek bir platformda birleştirerek, güvenlik testlerini daha verimli hale getirir.

### ✨ Özellikler

- 🔍 **Ağ Tarama**: Port tarama, servis tespiti, güvenlik duvarı analizi
- 🌐 **Web Güvenliği**: SQL injection, XSS, admin panel bulma, directory fuzzing
- 🔐 **Şifreleme**: MD5, SHA, Base64, steganografi, özel şifreleme algoritmaları
- 🔓 **Kaba Kuvvet**: SSH, FTP, HTTP, mail servisleri için brute force
- 📱 **Sosyal Mühendislik**: Phishing araçları, SMS bombing, kullanıcı bilgi toplama
- 🦠 **Payload Oluşturma**: Msfvenom otomasyonu, trojan oluşturma
- 🔬 **Forensics**: Dosya analizi, EXIF işlemleri, hash analizi
- 🎭 **Anonimlik**: MAC adresi değiştirme, VPN kontrolü
- 🤖 **Otomasyon**: Instagram bot, spam bot, auto clicker

### 🛠️ Kurulum

#### Linux / Termux

```bash
# Depoyu klonlayın
git clone https://github.com/Jizek/Omnikit-Security-Toolkit.git

# Dizine girin
cd Omnikit-Security-Toolkit

# Gerekli izinleri verin
chmod +x main.py

# Kurulum scriptini çalıştırın (opsiyonel)
python3 metfora.py

# Aracı başlatın
python3 main.py
```

#### Windows

```cmd
# Depoyu klonlayın
git clone https://github.com/Jizek/Omnikit-Security-Toolkit.git

# Dizine girin
cd Omnikit-Security-Toolkit

# Aracı başlatın
python main.py
```

#### Docker

```bash
# Docker image'ı çekin
docker pull jizek/omnikit:latest

# Container'ı çalıştırın
docker run -it jizek/omnikit:latest
```

### 📋 Gereksinimler

- Python 3.6 veya üzeri
- Linux işletim sistemi (önerilen)
- Root/Administrator yetkileri (bazı araçlar için)

**Termux Kullanıcıları İçin:**
```bash
apt update
apt install python3 git
```

### 🎯 Kullanım

1. Programı başlatın: `python3 main.py`
2. Ana menüden istediğiniz aracı seçin (1-54)
3. Araç için gerekli parametreleri girin
4. Sonuçları görüntüleyin

### 🔧 Araç Kategorileri

<details>
<summary><b>🌐 Ağ Araçları (Network Tools)</b></summary>

- Port Tarama (NMAP Otomasyonu)
- Güvenlik Duvarı Tespiti (wafw00f)
- VPN Kontrolü (ike-scan)
- WiFi Port Tarayıcı
- DNS Yönlendirici
- Anormal DNS Tespit
- Traceroute
- Network Reaper (Paket Dinleyici)

</details>

<details>
<summary><b>🔓 Kaba Kuvvet Araçları (Brute Force)</b></summary>

- FTP/SSH/Telnet/HTTP Brute Force
- SMB/RDP/VNC Brute Force
- SSH Brute Force v2
- Mail Brute Force (Gmail/Hotmail)
- Zip Şifre Kırıcı

</details>

<details>
<summary><b>🌍 Web Güvenlik Araçları</b></summary>

- WordPress Tarama (wpscan)
- SQL Injection (sqlmap)
- Admin Panel Bulucu
- Directory Fuzzer
- Subdomain Listeleyici
- Web Scraper
- Site Fuzzing
- SSL Analizi
- Whois Sorgulama

</details>

<details>
<summary><b>🔐 Şifreleme & Kriptografi</b></summary>

- Hash Şifreleme (MD5, SHA, Blake2b)
- Hash Kırma (Reverse Hash)
- Base64 Encode/Decode
- Steganografi (Resim İçine Veri Gizleme)
- StnCrypt (Özel Şifreleme)
- Gelişmiş Şifreleme 1 & 2

</details>

<details>
<summary><b>🔬 Forensics & Analiz</b></summary>

- Dosya Analizi
- EXIF İşlemleri
- PDF Bilgi Toplama
- Email Header Analyzer
- Hash Analizi
- Strings (Binary Analiz)
- Dosya Hash Bulma

</details>

<details>
<summary><b>🎭 Sosyal Mühendislik</b></summary>

- Phishing Araçları (3 Farklı)
- SMS Bombing
- Anonim SMS
- Instagram Bot
- Spam Bot
- Kullanıcı Adı ile Hesap Bulma

</details>

<details>
<summary><b>🦠 Payload & Exploit</b></summary>

- Trojan Oluşturma (Msfvenom)
- Virüs Oluşturma (4 Tip)
- Raspberry Pi Pico Hack
- Omnikit Twin (ESP32/ESP8266)
- Uzantı Sahteleyici

</details>

<details>
<summary><b>🛠️ Yardımcı Araçlar</b></summary>

- Wordlist Oluşturucu (2 Tip)
- Şifre Oluşturucu
- MAC Adresi Değiştirme
- Oto Tıklayıcı
- Python Derleme
- Index Oluşturucu
- FotoDit (Fotoğraf Düzenleme)

</details>

### 📚 Dokümantasyon

Detaylı kullanım kılavuzu ve araç açıklamaları için [Wiki](https://github.com/Jizek/Omnikit-Security-Toolkit/wiki) sayfasını ziyaret edin.

### 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

### 🐛 Hata Bildirimi

Bir hata bulduysanız, lütfen [Issues](https://github.com/Jizek/Omnikit-Security-Toolkit/issues) sayfasından bildirin.

### 📬 İletişim

- **Geliştirici:** jizek
- **Telegram:** [@FurkanDe](https://t.me/FurkanDe)
- **Telegram Kanalı:** [t.me/omnikit](https://t.me/omnikit)
- **Discord:** `jizek`
- **Discord Sunucusu:** [discord.com/invite/DTN5RSvYvw](https://discord.com/invite/DTN5RSvYvw)
- **Instagram:** [@omnikit](https://instagram.com/omnikit)

### 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

### ⭐ Yıldız Verin!

Bu projeyi beğendiyseniz, lütfen ⭐ vererek destek olun!

---

<a name="english"></a>
## 🇬🇧 English

### ⚠️ Legal Disclaimer

> This tool is developed solely for **educational**, **instructional**, and **cybersecurity awareness** purposes.

**IMPORTANT:** You are entirely responsible for all actions performed with this tool. The developer and GitHub platform accept no legal or ethical liability.

### 📖 About

**Omnikit** is a comprehensive toolkit designed for cybersecurity professionals, penetration testers, and security researchers. It combines over 50 security tools into a single platform, making security testing more efficient.

### ✨ Features

- 🔍 **Network Scanning**: Port scanning, service detection, firewall analysis
- 🌐 **Web Security**: SQL injection, XSS, admin panel finder, directory fuzzing
- 🔐 **Encryption**: MD5, SHA, Base64, steganography, custom encryption algorithms
- 🔓 **Brute Force**: SSH, FTP, HTTP, mail services brute forcing
- 📱 **Social Engineering**: Phishing tools, SMS bombing, user information gathering
- 🦠 **Payload Generation**: Msfvenom automation, trojan creation
- 🔬 **Forensics**: File analysis, EXIF operations, hash analysis
- 🎭 **Anonymity**: MAC address changing, VPN checking
- 🤖 **Automation**: Instagram bot, spam bot, auto clicker

### 🛠️ Installation

#### Linux / Termux

```bash
# Clone the repository
git clone https://github.com/Jizek/Omnikit-Security-Toolkit.git

# Navigate to directory
cd Omnikit-Security-Toolkit

# Grant permissions
chmod +x main.py

# Run setup script (optional)
python3 metfora.py

# Start the tool
python3 main.py
```

#### Windows

```cmd
# Clone the repository
git clone https://github.com/Jizek/Omnikit-Security-Toolkit.git

# Navigate to directory
cd Omnikit-Security-Toolkit

# Start the tool
python main.py
```

### 📋 Requirements

- Python 3.6 or higher
- Linux operating system (recommended)
- Root/Administrator privileges (for some tools)

### 🎯 Usage

1. Start the program: `python3 main.py`
2. Select desired tool from main menu (1-54)
3. Enter required parameters
4. View results

### 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

### ⭐ Star Us!

If you like this project, please give it a ⭐ to show your support!

---

<div align="center">

**Made with ❤️ by [jizek](https://github.com/Jizek)**

</div>
