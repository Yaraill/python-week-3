import pygame # Pygame kütüphanesini içeri aktarıyoruz

# Pygame'i başlat
pygame.init()

# Ekran ayarları
GENISLIK, YUKSEKLIK = 720, 720
EKRAN = pygame.display.set_mode((GENISLIK, YUKSEKLIK)) # Oyun penceresini oluşturuyoruz
pygame.display.set_caption("Basit Pygame Fonksiyon Örneği") # Pencere başlığını ayarlıyoruz

# Renkler (RGB kodları)
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)

# --- Oyuncu çizme fonksiyonumuz ---
def oyuncu_ciz(ekran_yuzeyi, oyuncu_resmi, x_konumu, y_konumu):
    """
    Belirtilen oyuncu resmini ekranın belirtilen konumuna çizer.

    Args:
        ekran_yuzeyi (pygame.Surface): Çizimin yapılacağı Pygame ekran yüzeyi.
        oyuncu_resmi (pygame.Surface): Çizilecek oyuncunun resmi (Pygame yüzeyi).
        x_konumu (int): Oyuncu resminin sol üst köşesinin x koordinatı.
        y_konumu (int): Oyuncu resminin sol üst köşesinin y koordinatı.
    """
    ekran_yuzeyi.blit(oyuncu_resmi, (x_konumu, y_konumu)) # Resmi ekrana kopyala

# --- Ana Oyun Döngüsü ---
def ana_oyun():
    # Oyuncu resmini yükle (örnek olarak basit bir kare oluşturacağız)
    # Normalde buraya 'pygame.image.load("oyuncu.png").convert_alpha()' gibi bir şey yazarsın
    oyuncu_resmi = pygame.Surface((80, 50)) # 50x50 boyutunda bir yüzey oluştur
    oyuncu_resmi.fill(KIRMIZI) # Bu yüzeyi kırmızı renkle doldur, oyuncumuz kırmızı bir kare olacak

    oyuncu_x = 360 # Oyuncunun başlangıç X konumu
    oyuncu_y = 360 # Oyuncunun başlangıç Y konumu

    kosuyor = True # Oyun döngüsünü kontrol eden değişken
    while kosuyor:
        for event in pygame.event.get(): # Olayları kontrol et
            if event.type == pygame.QUIT: # Eğer kapatma düğmesine basıldıysa
                kosuyor = False # Döngüyü sonlandır

        # Ekranı temizle (her karede baştan çizmek için)
        EKRAN.fill(SIYAH) # Arka planı siyaha boya

        # --- Fonksiyonumuzu çağırıyoruz ---
        oyuncu_ciz(EKRAN, oyuncu_resmi, oyuncu_x, oyuncu_y) # Oyuncuyu ekrana çiz

        # Ekranı güncelle
        pygame.display.flip() # Tüm çizimleri göster

    pygame.quit() # Pygame'i kapat

# Oyunu başlat
if __name__ == "__main__":
    ana_oyun()