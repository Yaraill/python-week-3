hesap_bilgileri =  [
    {
    "ad": "Ahmet Polat",
    "hesapNo": "123",
    "password": "123456",
    "bakiye": 6738.55,
    "username": "polatahmet",
    "ekHesap": 2500.0,
    },
    {
    "ad": "Ali Veli",
    "hesapNo": "123456",
    "password": "123987",
    "bakiye": 5437.98,
    "username": "veliali",
    "ekHesap": 5500.0,
    }
]

def menu(hesap):
    while True:
        print("\n")

        print(f"Merhaba, {hesap['ad']}")

        print("1-Bakiye Sorgulama")
        print("2-Para Çekme")
        print("3-Para Yatırma")
        print("4-Çıkış")

        islem = input("Yapmak istediğin işlemi seçiniz: ")

        if islem == "1":
            bakiyeSorgula(hesap)

        elif islem == "2":
            paraCekme(hesap)

        elif islem == "3":
            paraYatirma(hesap)

        elif islem == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçerli bir şey girin.")

def bakiyeSorgula(hesap):
    print(f"bakiye: {hesap['bakiye']}")
    print(f"ek bakiye: {hesap['ekHesap']}")

def paraCekme(hesap):
    miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanımIzni = input("Ek hesap kullanılsın mı? (e/h): ")

            if ekHesapKullanımIzni == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("Paranızı alabilirsiniz")

            else:
                print("Üzgünüz bakiyeniz yetersiz.")

        else:
            print("Üzgünüz bakiyeniz yetersiz.")

def paraYatirma(hesap):
    miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
    hesap["bakiye"] += miktar
    print(f"{miktar} TL hesabınıza yatırıldı.")

def login():
    username = input("username: ")
    password = input("password: ")

    isLoggedIn = False

    for hesap in hesap_bilgileri:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break
    
    if not isLoggedIn:
        print("username yada parola yanlış!")

login()
