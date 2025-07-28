name = "Yasir"
password = "yasirnörün"

while True:
    username = input("username: ")
    sifre = input("password: ")
    if username == name and sifre == password:
        print("Giriş başarılı")
        break

    else:
        print("--- Giriş başarısız ---")
        continue
        
