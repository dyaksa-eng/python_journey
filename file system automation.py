import os

folder_nama = "data_laporan"

if not os.path.exists(folder_nama):
    os.mkdir(folder_nama)
    print(f"Folder '{folder_nama}' berhasil dibuat!")
else:
    print("Folder udah ada, lewatin aja.")

with open("data_laporan/hasil.txt", "a") as file_saya:
    file_saya.write("\nini baris baru hasil mode append")
