while True:
    print("\n(1) Not ekleme\n")
    print("(2) Notları görüntüleme\n")
    print("(3) Çıkış\n")
    print("(4) Dosyanın İçeriğini Sıfırla (Dikkat! Tüm notlar silinir)\n")
    islem = input("Yapmak istediğiniz işlemi seçin: ")

    dosya_ismi = "defter_1.txt"

    if islem == "1":
        with open(f"{dosya_ismi}", "a") as dosya1:
            yazi = input("Dosya içine yazmak istediğiniz metni giriniz: ")
            dosya1.write(yazi + "\n")

    elif islem == "2":
        try:
            with open(f"{dosya_ismi}", "r") as dosya2:
                icerik = dosya2.read()
                if icerik.strip(): # Dosya boş mu kontrol et
                    print("\n--- Notlar ---")
                    print(icerik)
                    print("--------------")
                else:
                    print("Henüz hiç not eklenmemiş.")
                
        except FileNotFoundError:
            print(f"Hata! {dosya_ismi} isimli bir dosya bulunamadı.")
        except Exception as e:
            print(f"Notlar okunurken bir hata oluştu: {e}")

    elif islem == "3":
        print("Uygulamadan çıkılıyor...")
        break

    elif islem == "4":
        with open(f"{dosya_ismi}", "w") as dosya3:
            print("\nDikkat! Dosyanın içindeki tüm notlar silindi.")
            yazi = input("Dosya içine yazmak istediğiniz metni giriniz: ")
            dosya3.write(yazi)
            print("Dosya başarıyla güncellendi.")

    else:
        print("Geçersiz seçenek! Lütfen 1 - 2 - 3 - 4 seçeneklerinden birini seçiniz.s")
        
print("Program sona erdi.")