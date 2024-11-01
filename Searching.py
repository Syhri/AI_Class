# Fungsi untuk mencari indeks bilangan genap dalam list
def find_even_indices(x, y1):
    # Memeriksa apakah y1 adalah bilangan genap
    if y1 % 2 != 0:
        raise ValueError("Input y1 is not an even number. Please provide an even number.")
    
    # Mencari semua indeks di mana nilai dalam x sama dengan y1
    indices = [i for i, value in enumerate(x) if value == y1]
    
    # Jika y1 tidak ditemukan dalam x, tampilkan pesan error
    if not indices:
        raise ValueError(f"Bilangan {y1} tidak ditemukan dalam list.")
    
    return indices

# Array contoh dengan 20 data acak
x = [2, 7, 8, 9, 1, 1, 4, 4, 4, 9, 5, 7, 8, 6, 1, 4, 7, 8, 3, 2]

# Meminta pengguna memasukkan nilai y1
y1 = int(input("Masukkan bilangan genap yang ingin dicari: "))

# Menjalankan fungsi dengan input dari pengguna
try:
    indices = find_even_indices(x, y1)
    print(f"Bilangan {y1} ada di indeks {indices}")
except ValueError as e:
    print(e)
