nilai_siswa = [89, 90, 76, 40, 80, 59, 80]


def cek_kelulusan(daftar_nilai):

    print("---Cek Kelulusan Siswa---")

    for nilai in daftar_nilai:
        if nilai >= 70:
            print(f"Nilai {nilai} : Lulus")
        else:
            print(f"Nilai {nilai} : Tidak Lulus")
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    tertinggi = max(daftar_nilai)
    terendah = min(daftar_nilai)

    print("\n---Statistik Nilai---")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")
    print(f"Nilai Tertinggi: {tertinggi}")
    print(f"Nilai Terendah: {terendah}")

    while True:
        tanya = input("\nmau input nilai baru? (y/n): ")

        if tanya.lower() == "y":
            while True:
                nilai_baru = float(input("Masukkan nilai baru: "))
                if 0 <= nilai_baru <= 100:
                    break
                else:
                    print("Nilai tidak valid, silakan masukkan nilai antara 0 dan 100.")
            daftar_nilai.append(nilai_baru)
            print("nilai berhasil ditambahkan!")
            cek_kelulusan(daftar_nilai)
            break
        elif tanya.lower() == "n":
            print("terima kasih")
            break
        else:
            print("input tidak valid, silakan masukkan 'y' atau 'n'.")

print("-" * 30)


cek_kelulusan(nilai_siswa)
