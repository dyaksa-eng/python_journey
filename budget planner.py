import json
import os


def main():
    file_data = "budget.json"
    if os.path.exists(file_data):
        with open(file_data, "r") as f:
            data = json.load(f)
    else:
        data = []

    while True:
        print("\n---Budget Planer---")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Total dan Daftar Pengeluaran")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            item = input("nama barang: ")
            harga = int(input("harga: "))
            data.append({"item": item, "harga": harga})

            with open(file_data, "w") as f:
                json.dump(data, f, indent=4)
            print("data tersimpan!")

        elif pilihan == "2":
            total = sum(d["harga"] for d in data)
            print(f"total pengeluaran: {total}")

        elif pilihan == "3":
            print("selesai")
            break


main()
