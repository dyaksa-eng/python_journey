inventory = {
    "kopi": {"stok": 10, "harga": 5000},
    "roti": {"stok": 5, "harga": 8000},
    "susu": {"stok": 8, "harga": 7000},
}

kategori = ["minuman", "makanan"]

inventory = {}

def tambah_barang():
    print("\n--- Tambah Barang Baru ---")
    nama = input("Nama Barang: ").lower()
    
    # Cek duplikat dulu
    if nama in inventory:
        print("Barang udah ada, mending update stok aja!")
        return
    
    # Input data pake try-except biar gak error kalo user asal masukin huruf di angka
    try:
        stok = int(input("Jumlah Stok: "))
        harga = int(input("Harga Barang: "))
        
        inventory[nama] = {"stok": stok, "harga": harga}
        print(f"{nama} berhasil ditambahkan!")
    except ValueError:
        print("Gagal! Stok dan Harga harus angka.")

# Menu utama biar bisa input terus-terusan
while True:
    print("\n1. Tambah Barang | 2. Lihat Inventory | 3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        tambah_barang()
    elif pilihan == '2':
        print("\nInventory saat ini:", inventory)
    elif pilihan == '3':
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan gak ada, coba lagi!")


def update_stok(nama_barang, jumlah):
    if nama_barang in inventory:
        inventory[nama_barang]["stok"] += jumlah
        print(f"Update: {nama_barang} sekarang {inventory[nama_barang]['stok']} item.")
    else:
        print(f"{nama_barang} tidak ditemukan dalam inventory.")


def cek_harga(nama_barang):
    item = inventory.get(nama_barang)
    if item:
        print(f"Harga {nama_barang}: Rp{item['harga']}")
    else:
        print(f"{nama_barang} tidak ditemukan dalam inventory.")


