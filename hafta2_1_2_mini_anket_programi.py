anket_katilimcilari = []

while True:
    name = input("İsminizi giriniz: ")
    gender = input("Cinsiyetinizi giriniz (Erkek/Kadın): ")
    age = int(input("Yaşınızı giriniz: "))
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
        print("Anket tamamlandı.")
        break

print("\nAnket Katılımcı Bilgileri:")
for katilimci in anket_katilimcilari:
    for key, value in katilimci.items():
        print(f"{key.capitalize()}: {value}")
    print("---")