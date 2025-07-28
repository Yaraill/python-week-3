kelime_sayilari = {}

metin = input("Lütfen bir metin giriniz: ")

for kelime in metin.split():
    kelime = kelime.lower().strip(",.!?;:")
    if kelime in kelime_sayilari:
        kelime_sayilari[kelime] += 1
    else:
        kelime_sayilari[kelime] = 1

print("\nKelime Sayıları:")
for kelime, sayi in kelime_sayilari.items():
    print(f"{kelime}: {sayi} kez")
print("\nToplam Kelime Sayısı:", sum(kelime_sayilari.values()))
print("Farklı Kelime Sayısı:", len(kelime_sayilari))
