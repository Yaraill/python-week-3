bilgiler = {
    "Ali": "123456",
    "Ayşe": "123987",
    "Yasir": "147896",
    "Akif": "111222",
}

max_deneme = 3
deneme_sayisi = 0

while deneme_sayisi < max_deneme:
    giris = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    if giris in bilgiler and bilgiler[giris] == sifre: 
        print("Giriş başarılı!")
        break 
    else:
        deneme_sayisi += 1 

        if deneme_sayisi == max_deneme:
            print("Çok fazla yanlış deneme yaptınız. Hesabınız kilitlendi!")
        else:
            print(f"Giriş başarısız! Kalan deneme hakkınız: {max_deneme - deneme_sayisi}")


