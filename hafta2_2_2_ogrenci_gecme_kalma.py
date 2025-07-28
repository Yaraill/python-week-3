ogrenciler = {
    "Akif": 80,
    "Yasir": 70,
    "Ali": 30,
}

toplam_not = 0

print("--- Öğrenci Not Durumları ---")

for ogrenci_adi, note in ogrenciler.items():
    toplam_not += note

    if note >= 50:
        print(f"{ogrenci_adi} {note} notu ile geçti!")

    else:
        print(f"{ogrenci_adi} {note} notu ile kaldı!")

ortalama = toplam_not / len(ogrenciler)

print("\n--- Genel Not Ortalaması ---")
print(f"Genel Not Ortalaması: {ortalama:.2f}")
