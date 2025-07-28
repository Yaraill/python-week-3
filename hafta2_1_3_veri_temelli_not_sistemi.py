sinif = [
    {"Ad": "Ali", "Notlar": [35, 18, 68]},
    {"Ad": "Ayşe", "Notlar": [90, 85, 95]},
    {"Ad": "Yasir", "Notlar": [75, 80, 70]},
    {"Ad": "Akif", "Notlar": [90, 100, 90]},
    {"Ad": "Zeynep", "Notlar": [25, 45, 55]}
]

for ogrenci in sinif:
    notlar = ogrenci["Notlar"]
    ortalama = sum(notlar) / len(notlar)
    print(f"{ogrenci["Ad"]} öğrencisinin not ortalaması: {ortalama:.2f}")

for ogrenci in sinif:
    notlar = ogrenci["Notlar"]
    ortalama = sum(notlar) / len(notlar)
    if ortalama >= 50:
        print(f"{ogrenci["Ad"]} dersi geçti.")
    else:
        print(f"{ogrenci["Ad"]} dersten kaldı.")

tum_notlar = []
for ogrenci in sinif:
    tum_notlar.extend(ogrenci["Notlar"])
sinif_ortalamasi = sum(tum_notlar) / len(tum_notlar)
print(f"Sınıfın genel not ortalaması: {sinif_ortalamasi:.2f}")