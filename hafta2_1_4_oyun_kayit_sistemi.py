metin = input("Dosyaya yazdırılcak metni giriniz: ")

import datetime
simdi = datetime.datetime.now()

zaman_damgasi = simdi.strftime("%Y%m%d_%H%M%S")



dosya_adi = f"w2_1.4_Oyun_{zaman_damgasi}.txt"
with open(dosya_adi, "w") as dosya:
    dosya.write(metin)

print(f"Dosyaya yazma tamamlandı. Dosya {dosya_adi} adlı dosyaya yazıldı.")
