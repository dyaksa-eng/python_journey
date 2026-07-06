import string
import random


def main():
    panjang = int(input("panjang password: "))
    karakter = string.ascii_letters + string.digits
    password = "".join([random.choice(karakter) for i in range(panjang)])
    print(f"generated password: {password}")


main()
