# 🚀 GitHub'a Yükleme Rehberi

## ✅ Proje Hazır!

Omnikit projesi GitHub'a yüklenmeye tamamen hazır. Aşağıdaki adımları takip edin.

## 📋 Ön Kontrol

Proje yapısı:
```
omnikit/
├── 📂 .github/workflows/      # CI/CD otomasyonu
├── 📂 src/                    # Ana kaynak kodlar
├── 📂 tools/                  # Araç modülleri (10 klasör)
├── 📂 assets/                 # Logo ve görseller
├── 📂 docs/                   # Dokümantasyon
├── 📄 README.md               # Göz alıcı README
├── 📄 CONTRIBUTING.md         # Katkı rehberi
├── 📄 LICENSE                 # MIT Lisansı
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📄 .gitignore              # Git yapılandırması
└── 📄 surum.txt               # Versiyon: 15
```

## 🔧 Adım 1: Git Başlatma

```bash
cd c:\Users\12jiz\Desktop\Omnikit\Omnikit

# Git'i başlat
git init

# Tüm dosyaları ekle
git add .

# İlk commit
git commit -m "🎉 Initial commit: Omnikit Security Toolkit v15

✨ Features:
- 54+ professional security tools
- 8 diverse ASCII art designs  
- Windows & Linux compatibility
- TR/EN language support
- Underground tools menu (40+ tools)
- Professional folder structure
- CI/CD with GitHub Actions

🔧 Main Categories:
- Network scanning & analysis
- Web security testing
- Brute force tools
- Encryption & cryptography
- Forensics & analysis
- Social engineering
- Payload generation

📝 Documentation:
- Complete README with badges
- Contributing guidelines
- MIT License
- Security policy
- Docker support

🎨 UI/UX:
- 8 random ASCII art designs
- Colorful terminal interface
- User-friendly menu navigation
- Return to menu functionality"
```

## 🌐 Adım 2: GitHub Repository Oluşturma

### Web Üzerinden:

1. GitHub'a giriş yapın: https://github.com
2. Sağ üst köşeden **"+"** → **"New repository"** tıklayın
3. Repository bilgilerini doldurun:
   - **Repository name:** `omnikit` veya `Omnikit-Security-Toolkit`
   - **Description:** `🛡️ The Ultimate Cybersecurity Arsenal - 54+ Professional Security Tools`
   - **Visibility:** Public
   - **❌ Initialize this repository with:** Hiçbirini seçmeyin (boş bırakın)
4. **"Create repository"** butonuna tıklayın

### Komut Satırından (Alternatif):

```bash
# GitHub CLI kullanarak
gh repo create omnikit --public --description "🛡️ The Ultimate Cybersecurity Arsenal"
```

## 🔗 Adım 3: Remote Repository Bağlama

```bash
# GitHub repository URL'inizi buraya yazın
git remote add origin https://github.com/KULLANICI_ADI/omnikit.git

# Veya SSH kullanıyorsanız:
git remote add origin git@github.com:KULLANICI_ADI/omnikit.git

# Remote'u kontrol edin
git remote -v
```

## 📤 Adım 4: Push

```bash
# Ana branch'i main olarak ayarla
git branch -M main

# GitHub'a push et
git push -u origin main
```

## 🎨 Adım 5: Repository Ayarları

### Topics Ekleyin:

Repository sayfasında **"About"** bölümünden **"⚙️ Settings"** → **"Topics"** ekleyin:

```
security, penetration-testing, hacking-tool, python, cybersecurity,
security-tools, ethical-hacking, kali-linux, infosec, security-scanner,
vulnerability-scanner, network-security, web-security, brute-force,
payload-generator, forensics, cryptography, social-engineering
```

### Description Güncelleyin:

```
🛡️ The Ultimate Cybersecurity Arsenal - 54+ Professional Security Tools | Network Security | Web Security | Brute Force | Cryptography | Forensics | Payload Generation
```

### Website Ekleyin:

```
https://t.me/omnikit
```

## 📋 Adım 6: Release Oluşturma

1. Repository sayfasında **"Releases"** → **"Create a new release"** tıklayın
2. Release bilgilerini doldurun:
   - **Tag version:** `v15.0`
   - **Release title:** `🎉 Omnikit v15 - The Ultimate Security Toolkit`
   - **Description:**

```markdown
## 🎉 Omnikit Security Toolkit v15

### ✨ What's New

- 🎨 **8 Diverse ASCII Art Designs** - Beautiful terminal interface
- 💻 **Windows Compatibility** - Full cross-platform support
- 📁 **Professional Structure** - Clean and organized codebase
- 🤖 **CI/CD Integration** - GitHub Actions automation
- 📚 **Complete Documentation** - README, Contributing guide, Security policy

### 🛠️ Features

- **54+ Security Tools** in one platform
- **Network Security** - Port scanning, firewall analysis, VPN checking
- **Web Security** - SQL injection, XSS, admin panel finder
- **Brute Force** - Multi-protocol brute forcing
- **Cryptography** - Hash encryption, password cracking
- **Forensics** - File analysis, EXIF operations
- **Payload Generation** - Msfvenom automation
- **Social Engineering** - Phishing tools, SMS bombing

### 📦 Installation

```bash
git clone https://github.com/KULLANICI_ADI/omnikit.git
cd omnikit
pip install -r requirements.txt
python src/main.py
```

### 🌍 Language Support

- 🇹🇷 Turkish
- 🇬🇧 English

### 📝 Full Changelog

- Added 8 random ASCII art designs
- Fixed broken ASCII art in underground menu
- Added Windows compatibility (cls command)
- Reorganized project structure
- Added CI/CD with GitHub Actions
- Updated documentation
- Improved user interface
- Added return to menu functionality

### ⚠️ Legal Disclaimer

This tool is for educational and legal penetration testing purposes only.
```

3. **"Publish release"** butonuna tıklayın

## 🏷️ Adım 7: README Badges Güncelleme

README.md dosyasındaki badge linklerini güncelleyin:

```markdown
[![Stars](https://img.shields.io/github/stars/KULLANICI_ADI/omnikit?style=for-the-badge&color=yellow)](https://github.com/KULLANICI_ADI/omnikit/stargazers)
```

## 📊 Adım 8: GitHub Actions Kontrolü

1. Repository'de **"Actions"** sekmesine gidin
2. İlk workflow çalışmasını kontrol edin
3. Yeşil ✅ işareti görmelisiniz

## 🎉 Tamamlandı!

Projeniz artık GitHub'da yayında! 

### Sonraki Adımlar:

- ⭐ Kendi repository'nize star verin
- 👀 Watch ekleyin
- 📢 Sosyal medyada paylaşın
- 🤝 Katkıda bulunmayı bekleyin

### Önemli Linkler:

- **Repository:** https://github.com/KULLANICI_ADI/omnikit
- **Issues:** https://github.com/KULLANICI_ADI/omnikit/issues
- **Pull Requests:** https://github.com/KULLANICI_ADI/omnikit/pulls
- **Releases:** https://github.com/KULLANICI_ADI/omnikit/releases

## 🔄 Güncelleme Yapmak İçin

```bash
# Değişiklikleri ekle
git add .

# Commit
git commit -m "feat: yeni özellik eklendi"

# Push
git push origin main
```

## 🐛 Sorun Giderme

### Problem: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/KULLANICI_ADI/omnikit.git
```

### Problem: "failed to push"
```bash
git pull origin main --rebase
git push origin main
```

### Problem: "permission denied"
```bash
# SSH key'inizi kontrol edin veya HTTPS kullanın
git remote set-url origin https://github.com/KULLANICI_ADI/omnikit.git
```

---

**🌟 Başarılar! Projeniz artık dünya çapında erişilebilir! 🌟**
