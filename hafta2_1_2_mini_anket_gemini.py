anket_katilimcilari = []

while True:
    name = input("İsminizi giriniz: ")

    gender = input("Cinsiyetinizi giriniz (Erkek/Kadın): ")
    if gender.lower() not in ["erkek", "kadın"]:
        print("Hata: Geçersiz cinsiyet girişi. Lütfen cinsiyetinizi doğru giriniz.\n")
        continue

    try:
        age = int(input("Yaşınızı giriniz: "))
    except ValueError:
        print("Hata: Geçersiz yaş girişi. Lütfen bir sayı giriniz.\n")
        continue

    city = input("Yaşadığınız şehir adını giriniz: ")

    katilimci = {
        "isim": name,
        "cinsiyet": gender,
        "yas": age,
        "sehir": city
    }
    anket_katilimcilari.append(katilimci)

    devam = input("\nBaşka bir katılımcı eklemek ister misiniz? (Evet/Hayır): ").lower()
    if devam == "hayır":
        print("\nAnket tamamlandı.")
        break

print("\nAnket Katılımcı Bilgileri:")
for katilimci in anket_katilimcilari:
    for key, value in katilimci.items():
        print(f"{key.capitalize()}: {value}")
    print("---")