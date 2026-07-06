import random


def main():
    angka_rahasia = random.randint(1, 100)
    print("tebak angka 1-100")

    jumlah_tebakan = 0

    while True:
        tebakan = int(input("tebakan:"))
        jumlah_tebakan += 1

        if tebakan < angka_rahasia:
            print("angka nya kekecilan woi")
        elif tebakan > angka_rahasia:
            print("angka nya kegedean, gimana sih")
        else:
            print("AJEGILE TEBAKAN BENER")
            break


main()
