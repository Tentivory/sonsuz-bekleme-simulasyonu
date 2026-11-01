#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Simülasyonu v1.0
Dünyanın en gerçekçi bekleme deneyimi.
Otobüs gelmez. Çay demlenmez. Umut tükenir. Ama kod çalışır.
"""

import time
import random
import sys

def sonsuz_bekleme():
    print("\n🚌 SONSUz BEKLEME SİMÜLASYONU BAŞLATILDI 🚌")
    print("Lütfen sabırlı olun. (Ama olmayın, çünkü sonsuza kadar sürecek.)\n")
    
    bekleme_mesajlari = [
        "Otobüs yaklaşıyor... (yalan)",
        "Çay demleniyor... (asla bitmeyecek)",
        "Sıra size geliyor... (gelmiyor)",
        "Yükleme %99... (sonsuza kadar %99)",
        "Motivasyonunuzu yüklüyoruz... (hata: bulunamadı)",
        "Sistem güncelleniyor... (2026'da hâlâ)",
        "Lütfen bekleyin, bu sefer gerçekten gelecek... (yok)"
    ]
    
    sayac = 0
    while True:
        mesaj = random.choice(bekleme_mesajlari)
        print(f"[{sayac}] {mesaj}")
        # Gizli not: bazen sistemin kendisi de bekler
        time.sleep(random.uniform(2, 5))
        sayac += 1
        if sayac > 1000000:
            print("Hata: Bekleme sınırı aşıldı. Ama yine de devam ediyorum.")
            # Gizli not (base64, decode etmeyin diye yazdım ki edesiniz): Ymlyw7xrcmFzaSBoZXIgemFtYW4ga2F6YW5pciwga2ltc2UgYmVrbGVy
            sayac = 0

if __name__ == "__main__":
    try:
        sonsuz_bekleme()
    except KeyboardInterrupt:
        print("\n\nBeklemeyi durdurdunuz. Tebrikler, çoğu insan bunu başaramaz.")
        print("Ama unutmayın: Gerçek hayatta CTRL+C yok.")
        sys.exit(0)
