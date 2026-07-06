inventory = {"kopi": {"stok": 10, "harga": 5000}}

def tambah_barang():
    nama = input("Nama Barang: ").lower()
    if nama in inventory:
        print("Barang udah ada, mending update stok aja!")
        return
    try:
        stok = int(input("Jumlah Stok: "))
        harga = int(input("Harga Barang: "))
        inventory[nama] = {"stok": stok, "harga": harga}
        print(f"{nama} berhasil ditambahkan!")
    except ValueError:
        print("Gagal! Stok dan Harga harus angka.")

def update_stok():
    nama = input("Nama barang yang mau diupdate: ").lower()
    if nama in inventory:
        jumlah = int(input("Tambah berapa stok? (bisa pake minus buat ngurangin): "))
        inventory[nama]["stok"] += jumlah
        print(f"Update: {nama} sekarang jadi {inventory[nama]['stok']} item.")
    else:
        print("Barang gak ditemukan!")

while True:
    print("\n1. Tambah | 2. Lihat | 3. Update Stok | 4. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1': tambah_barang()
    elif pilihan == '2': print(inventory)
    elif pilihan == '3': update_stok()
    elif pilihan == '4': break
    else: print("Pilihan gak ada!")
