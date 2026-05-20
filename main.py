#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Omnikit Security Toolkit - Entry Point
Ana giriş noktası: Kullanıcının hangi dizinde olduğundan bağımsız çalışır
"""

import os
import sys
from pathlib import Path

def main():
    """
    Omnikit'in ana giriş noktası
    - Proje kök dizinini belirler
    - src/ klasörünü Python yoluna ekler
    - Ana aracı başlatır
    """
    # Bu dosyanın bulunduğu dizin = Proje kök dizini
    BASE_DIR = Path(__file__).resolve().parent
    
    # Çalışma dizinini proje kök dizinine ayarla
    os.chdir(BASE_DIR)
    
    # src/ klasörünü Python yoluna ekle
    src_path = BASE_DIR / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    # Artık src/ içindeki modülleri import edebiliriz
    try:
        # omnikittoolsv15.py dosyasını import et ve çalıştır
        import omnikittoolsv15
        
    except ImportError as e:
        print(f"\n\033[91m[HATA] Omnikit modülü yüklenemedi: {e}\033[0m")
        print(f"\033[93m[BİLGİ] src/ klasörünün varlığını kontrol edin.\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\n\033[91m[HATA] Beklenmeyen bir hata oluştu: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
