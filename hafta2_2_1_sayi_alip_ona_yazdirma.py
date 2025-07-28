sayi = int(input("Kaça kadar yazdırmak istiyorsanız o sayıyı giriniz: "))

print(f"--- {sayi} sayısına kadar yazdırılacak. ---")

toplama = 0

for i in range(sayi+1):
    print(i)
    toplama += i

print(f"--- Tüm sayıların toplamı: {toplama} ---") 










