# Tüm öğrenci verilerini saklayacağımız ana sözlük.
# Anahtar: Öğrenci adı (string)
# Değer: Notlarını içeren bir liste (liste)
ogrenciler = {}

# --- Fonksiyon Tanımlamaları ---

def ogrenci_ekle(isim):
    """Yeni bir öğrenciyi sisteme ekler."""
    if isim in ogrenciler:
        print(f"Hata: '{isim}' isimli bir öğrenci zaten mevcut.")
    else:
        ogrenciler[isim] = [] # Not listesi başlangıçta boş
        print(f"'{isim}' sisteme başarıyla eklendi.")

def not_ekle(isim, not_degeri):
    """Belirtilen öğrenciye not ekler."""
    if isim not in ogrenciler:
        print(f"Hata: '{isim}' isimli öğrenci bulunamadı.")
        return # Öğrenci yoksa fonksiyondan çık

    try:
        not_degeri = int(not_degeri) # Girilen değeri tam sayıya çevirmeye çalış
        if 0 <= not_degeri <= 100: # Notun 0-100 arasında olup olmadığını kontrol et
            ogrenciler[isim].append(not_degeri)
            print(f"'{isim}' adlı öğrenciye '{not_degeri}' notu eklendi.")
        else:
            print("Hata: Not değeri 0 ile 100 arasında olmalıdır.")
    except ValueError:
        print("Hata: Geçersiz not değeri. Lütfen bir sayı girin.")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

def ortalama_hesapla(isim):
    """Belirtilen öğrencinin not ortalamasını hesaplar."""
    if isim not in ogrenciler:
        # print(f"Hata: '{isim}' isimli öğrenci bulunamadı.") # Kullanıcı arayüzünde zaten mesaj verilebilir
        return 0 # Öğrenci yoksa ortalama 0 döndür

    notlar = ogrenciler[isim]
    if not notlar: # Not listesi boş mu kontrol et (eğer hiç notu yoksa)
        print(f"'{isim}' adlı öğrencinin henüz notu yok.")
        return 0
    
    toplam_not = sum(notlar) # Notların toplamını al
    ortalama = toplam_not / len(notlar) # Ortalama hesapla
    return ortalama

def ogrenci_durum_goster():
    """Tüm öğrencilerin durumlarını (notlar, ortalama, geçti/kaldı) gösterir."""
    if not ogrenciler: # Eğer hiç öğrenci yoksa
        print("Henüz kayıtlı öğrenci yok.")
        return

    print("\n--- Öğrenci Durumları ---")
    for isim, notlar in ogrenciler.items():
        print(f"Öğrenci Adı: {isim}")
        print(f"Notları: {notlar if notlar else 'Henüz not yok'}") # Not yoksa bilgilendir
        
        ortalama = ortalama_hesapla(isim) # Ortalama hesaplamak için fonksiyonu çağır
        print(f"Ortalama: {ortalama:.2f}") # Ortalamayı virgülden sonra 2 hane ile göster

        if ortalama >= 50:
            print("Durum: Geçti")
        else:
            print("Durum: Kaldı")
        print("--------------------")

# --- Ana Program Akışı (Menü Sistemi) ---

while True:
    print("\n--- Öğrenci Takip Sistemi Menüsü ---")
    print("(1) Öğrenci Ekle")
    print("(2) Not Ekle")
    print("(3) Durumları Görüntüle")
    print("(4) Çıkış")
    
    secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        ogrenci_adi = input("Eklenecek öğrencinin adını giriniz: ")
        ogrenci_ekle(ogrenci_adi)
    
    elif secim == "2":
        ogrenci_adi = input("Not eklenecek öğrencinin adını giriniz: ")
        not_deger = input(f"'{ogrenci_adi}' için eklenecek notu giriniz (0-100): ")
        not_ekle(ogrenci_adi, not_deger) # Not değeri string olarak alınıp fonksiyon içinde int'e çevriliyor
    
    elif secim == "3":
        ogrenci_durum_goster()
    
    elif secim == "4":
        print("Sistemden çıkılıyor...")
        break # Ana döngüden çık ve programı bitir
    
    else:
        print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")

print("Program sona erdi.")