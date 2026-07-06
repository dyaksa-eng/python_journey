import os

data_nilai_siswa = "nilai_siswa.txt"
if not os.path.exists(data_nilai_siswa):
    print("file tidak ditemukan, membuat file baru...")
    with open(data_nilai_siswa, "w") as f:
        f.write("Daftar Nilai Siswa\n")
        f.write("-------------------\n")
        f.write("NAMA----NILAI----STATUS\n")

else:
    print("file ditemukan, menambahkan data...")


while True:
    nilai_siswa = int(input("MASUKAN NILAI SISWA: "))
    nama_siswa = input("MASUKAN NAMA SISWA: ")
    nilai_kkm = 75

    if nilai_siswa >= 0:
        with open(data_nilai_siswa, "a") as f:
            status = "lulus" if nilai_siswa >= 75 else "tidak lulus"
            f.write(f"{nama_siswa}, {nilai_siswa}, {status}\n")

    if nilai_siswa >= nilai_kkm:
        print(f" {nama_siswa} lulus, dengan nilai {nilai_siswa}")
    else:
        print(f" {nama_siswa} tidak lulus, dengan nilai {nilai_siswa}")

    lagi = input("apakah ingin menilai siswa lagi? (y/n): ")
    if lagi.lower() != "y":
        print("terima kasih")
        break
