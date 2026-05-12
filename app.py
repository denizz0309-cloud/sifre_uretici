import random
import string

def sifre_uret(uzunluk=8):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(karakterler) for _ in range(uzunluk))

print("Şifre üretici")

uzunluk = int(input("Uzunluk gir: "))
print("Şifre:", sifre_uret(uzunluk))