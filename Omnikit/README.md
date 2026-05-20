<div align="center">

# 🛡️ OMNIKIT Security Toolkit

<img src="assets/omnikit.png" alt="Omnikit Logo" width="200"/>

### *The Ultimate Cybersecurity Arsenal*

[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge)](https://github.com/jizek/omnikit)
[![Stars](https://img.shields.io/github/stars/jizek/omnikit?style=for-the-badge&color=yellow)](https://github.com/jizek/omnikit/stargazers)

**[🇬🇧 English](#english)** | **[🇹🇷 Türkçe](#turkish)**

---

</div>

## 🌟 Highlights

```ascii
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██████╗ ███╗   ███╗███╗   ██╗██╗██╗  ██╗██╗████████╗ ║
║  ██╔═══██╗████╗ ████║████╗  ██║██║██║ ██╔╝██║╚══██╔══╝ ║
║  ██║   ██║██╔████╔██║██╔██╗ ██║██║█████╔╝ ██║   ██║    ║
║  ██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔═██╗ ██║   ██║    ║
║  ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██║  ██╗██║   ██║    ║
║   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ║
║                                                          ║
║              Security Toolkit v15                        ║
║              54+ Professional Tools                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

<div align="center">

### 🎯 **54+ Tools** | 🎨 **8 ASCII Designs** | 🌍 **Multi-Language** | 💻 **Cross-Platform**

</div>

---

<a name="turkish"></a>

## 🇹🇷 Türkçe

### 📖 Nedir?

**Omnikit**, siber güvenlik profesyonelleri, penetrasyon testçileri ve güvenlik araştırmacıları için geliştirilmiş **kapsamlı** ve **güçlü** bir araç setidir. 54'ten fazla güvenlik aracını tek bir platformda birleştirerek, güvenlik testlerini **hızlı**, **verimli** ve **profesyonel** hale getirir.

### ⚠️ Yasal Uyarı

> **ÖNEMLİ:** Bu araç yalnızca **eğitim**, **öğretim** ve **yasal penetrasyon testleri** için geliştirilmiştir. Bu araçla gerçekleştireceğiniz tüm işlemlerin **sorumluluğu tamamen size aittir**. Geliştirici hiçbir hukuki veya etik yükümlülük kabul etmez.

### ✨ Özellikler

<table>
<tr>
<td width="50%">

#### 🔍 Ağ Güvenliği
- Port Tarama & Servis Tespiti
- Güvenlik Duvarı Analizi
- VPN & Proxy Kontrolü
- DNS Analizi & Yönlendirme
- WiFi Güvenlik Testleri
- Paket Dinleme & Analiz

</td>
<td width="50%">

#### 🌐 Web Güvenliği
- SQL Injection Testleri
- XSS Zafiyet Tarama
- Admin Panel Bulma
- WordPress Güvenlik Analizi
- Directory Fuzzing
- SSL/TLS Analizi

</td>
</tr>
<tr>
<td width="50%">

#### 🔐 Kriptografi
- Hash Şifreleme (MD5, SHA, Blake2b)
- Şifre Kırma & Analiz
- Base64 Encode/Decode
- Steganografi
- Özel Şifreleme Algoritmaları
- Dosya Hash Analizi

</td>
<td width="50%">

#### 🔓 Brute Force
- SSH/FTP/Telnet Brute Force
- HTTP/HTTPS Brute Force
- SMB/RDP/VNC Brute Force
- Mail Servisleri Brute Force
- Zip Şifre Kırma
- Wordlist Oluşturma

</td>
</tr>
<tr>
<td width="50%">

#### 🦠 Payload Oluşturma
- Msfvenom Otomasyonu
- Trojan Oluşturma
- Reverse Shell Payloads
- Android Payloads
- Raspberry Pi Pico Payloads
- ESP32/ESP8266 Payloads

</td>
<td width="50%">

#### 🔬 Forensics & Analiz
- Dosya Analizi
- EXIF İşlemleri
- PDF Bilgi Toplama
- Email Header Analizi
- Binary Analiz (Strings)
- Timestamp Manipülasyonu

</td>
</tr>
</table>

### � Hızlı Başlangıç

#### 📥 Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/jizek/omnikit.git

# Dizine girin
cd omnikit

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Programı başlatın
python src/main.py
```

#### 🐳 Docker ile Kullanım

```bash
# Docker image'ı çekin
docker pull jizek/omnikit:latest

# Container'ı çalıştırın
docker run -it jizek/omnikit:latest
```

### 📋 Gereksinimler

- **Python:** 3.6 veya üzeri
- **İşletim Sistemi:** Linux (önerilen), Windows, macOS
- **Yetki:** Bazı araçlar için root/administrator

### 🎯 Kullanım

1. **Başlatma:** `python src/main.py`
2. **Araç Seçimi:** Ana menüden istediğiniz aracı seçin (1-54)
3. **Parametre Girişi:** Gerekli bilgileri girin
4. **Sonuç:** Analiz sonuçlarını görüntüleyin

### � Proje Yapısı

```
omnikit/
├── 📂 src/                    # Ana kaynak kodlar
│   ├── main.py               # Başlatıcı
│   ├── omnikittoolsv15.py    # Ana program
│   └── acilis.py             # Banner & Logo
│
├── 📂 tools/                  # Araç modülleri
│   ├── kits/                 # 35+ yardımcı araç
│   ├── blue-cough/           # DDoS araçları
│   ├── crawler-x11/          # Web crawler
│   ├── imitator-x11/         # AI imitator
│   ├── oltalama/             # Phishing araçları
│   ├── password-kits/        # Şifre araçları
│   ├── pico-payloads/        # RPi Pico payloads
│   ├── omnikit-twin/         # ESP32/ESP8266
│   └── vrs/                  # Payload generator
│
├── 📂 assets/                 # Görseller & medya
│   └── omnikit.png           # Logo
│
├── 📂 docs/                   # Dokümantasyon
│   ├── SECURITY.md           # Güvenlik politikası
│   └── LOGO_INFO.md          # Logo bilgileri
│
├── � .github/                # GitHub yapılandırması
│   └── workflows/            # CI/CD
│
├── 📄 README.md               # Bu dosya
├── 📄 LICENSE                 # MIT Lisansı
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📄 Dockerfile              # Docker yapılandırması
└── 📄 surum.txt               # Versiyon bilgisi
```

### 🛠️ Araç Kategorileri

<details>
<summary><b>� Ağ Araçları (10 Araç)</b></summary>

1. **Exploit Arama** - searchsploit otomasyonu
2. **Güvenlik Duvarı Tespiti** - wafw00f
3. **Kaba Kuvvet** - Multi-protocol brute force
4. **NMAP Port Tarama** - Gelişmiş port tarama
5. **Rootkit Tarama** - chkrootkit
6. **Trojan Oluşturma** - msfvenom otomasyonu
7. **Zaafiyet Analizi** - nikto
8. **Zaafiyet Analizi v2** - lynis
9. **Wordlist Oluşturucu** - crunch
10. **VPN Kontrolü** - ike-scan

</details>

<details>
<summary><b>� Sistem Araçları (4 Araç)</b></summary>

11. **MAC Adresi Değiştirme** - macchanger
12. **WordPress Tarama** - wpscan
13. **Python Derleme** - py_compile
14. **SQL Injection** - sqlmap

</details>

<details>
<summary><b>🎭 Yeraltı Araçları (40+ Araç)</b></summary>

- Etkinleştirme Kodu Oluşturucuları
- Şifre Oluşturucular (3 tip)
- Kullanıcı Adı ile Hesap Bulma
- TC Kimlik Son 2 Hane Bulma
- Anonim SMS
- Telefon Numarasından Şehir Bulma
- Panelsiz Mail
- Admin Panel Tarama
- Spambot
- IP Bilgi Toplama
- UltraBot
- Oto Tıklayıcı
- SMS Bomb
- Zip Şifre Kırıcı
- Wordlist Oluşturucu
- Oltalama Araçları
- Instagram Bot
- Web Scraping Araçları
- Dosya Analiz Araçları
- StnCrypt Şifreleme
- Admin Panel Bulucu (Dinamik)
- Link Kısaltma Servisleri
- Whois Sorgulama
- SSL Analizi
- Rastgele İnsan Verisi Üretme
- DNS Bilgi Toplama
- ISBN Bilgi Toplama
- Mail Geçerlilik Kontrolü
- IP Zafiyet Analizi
- SSH Brute Force
- WiFi Port Tarayıcı
- Anormal DNS Tespit
- DNS Yönlendirici
- WiFi Dinleyicileri (2 tip)

</details>

### 🎨 Özellikler

- ✨ **8 Farklı ASCII Art** - Her çalıştırmada farklı tasarım
- 🌍 **Çoklu Dil Desteği** - Türkçe & İngilizce
- 💻 **Cross-Platform** - Windows, Linux, macOS
- 🎯 **Kullanıcı Dostu** - Kolay menü navigasyonu
- � **Ana Menüye Dön** - Her araçta geri dönüş
- 🎨 **Renkli Arayüz** - Terminal renklendirmesi
- 📦 **Otomatik Kurulum** - Eksik paketleri otomatik yükler

### 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

### 🐛 Hata Bildirimi

Bir hata bulduysanız, lütfen [Issues](https://github.com/jizek/omnikit/issues) sayfasından bildirin.

### � İletişim

<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-@FurkanDe-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/FurkanDe)
[![Discord](https://img.shields.io/badge/Discord-jizek-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/DTN5RSvYvw)
[![Instagram](https://img.shields.io/badge/Instagram-@omnikit-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/omnikit)

**Telegram Kanalı:** [t.me/omnikit](https://t.me/omnikit)

</div>

### 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

### ⭐ Yıldız Verin!

Bu projeyi beğendiyseniz, lütfen ⭐ vererek destek olun!

---

<a name="english"></a>

## 🇬🇧 English

### 📖 What is Omnikit?

**Omnikit** is a **comprehensive** and **powerful** toolkit designed for cybersecurity professionals, penetration testers, and security researchers. It combines **54+ security tools** into a single platform, making security testing **fast**, **efficient**, and **professional**.

### ⚠️ Legal Disclaimer

> **IMPORTANT:** This tool is developed solely for **educational**, **instructional**, and **legal penetration testing** purposes. You are entirely responsible for all actions performed with this tool. The developer accepts no legal or ethical liability.

### ✨ Features

- 🔍 **Network Security** - Port scanning, firewall analysis, VPN checking
- 🌐 **Web Security** - SQL injection, XSS, admin panel finder
- 🔐 **Cryptography** - Hash encryption, password cracking, steganography
- 🔓 **Brute Force** - Multi-protocol brute forcing tools
- 🦠 **Payload Generation** - Msfvenom automation, trojan creation
- 🔬 **Forensics** - File analysis, EXIF operations, hash analysis
- 🎭 **Social Engineering** - Phishing tools, SMS bombing
- 🤖 **Automation** - Instagram bot, spam bot, auto clicker

### � Quick Start

```bash
# Clone the repository
git clone https://github.com/jizek/omnikit.git

# Navigate to directory
cd omnikit

# Install requirements
pip install -r requirements.txt

# Run the tool
python src/main.py
```

### 📋 Requirements

- **Python:** 3.6 or higher
- **OS:** Linux (recommended), Windows, macOS
- **Privileges:** Root/Administrator for some tools

### 🎯 Usage

1. **Start:** `python src/main.py`
2. **Select Tool:** Choose from main menu (1-54)
3. **Enter Parameters:** Provide required information
4. **View Results:** Analyze the output

### 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Create Pull Request

### 📄 License

This project is licensed under the [MIT License](LICENSE).

### ⭐ Star Us!

If you like this project, please give it a ⭐ to show your support!

---

<div align="center">

### 🌟 Made with ❤️ by [jizek](https://github.com/jizek)

[![GitHub followers](https://img.shields.io/github/followers/jizek?style=social)](https://github.com/jizek)
[![GitHub stars](https://img.shields.io/github/stars/jizek/omnikit?style=social)](https://github.com/jizek/omnikit/stargazers)

**[⬆ Back to Top](#-omnikit-security-toolkit)**

</div>
