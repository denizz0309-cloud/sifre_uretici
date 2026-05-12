import random   # rastgele seçim için
import string   # harf, rakam, sembol listeleri için

def sifre_uret(uzunluk, buyuk_harf, rakam, sembol):
    
    # Başlangıçta sadece küçük harfler var
    karakter_havuzu = string.ascii_lowercase  # a-z

    # Kullanıcı istediyse büyük harf ekle
    if buyuk_harf:
        karakter_havuzu += string.ascii_uppercase  # A-Z

    # Kullanıcı istediyse rakam ekle
    if rakam:
        karakter_havuzu += string.digits  # 0-9

    # Kullanıcı istediyse sembol ekle
    if sembol:
        karakter_havuzu += string.punctuation  # !@#$% vs.

    # Havuzdan rastgele seçim yaparak şifreyi oluştur
    sifre = ""
    for i in range(uzunluk):
        sifre += random.choice(karakter_havuzu)

    return sifre


def main():
    print("=" * 40)
    print("       🔐 Şifre Üreteci")
    print("=" * 40)

    # Kullanıcıdan şifre uzunluğunu al
    while True:
        try:
            uzunluk = int(input("\nŞifre uzunluğu (6-32): "))
            if 6 <= uzunluk <= 32:
                break
            else:
                print("Lütfen 6 ile 32 arasında bir sayı gir.")
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

    # Büyük harf istiyor mu?
    # Evet için 'e', Hayır için 'h' yaz ve Enter'a bas
    buyuk_harf = input("Büyük harf olsun mu? (evet için 'e', hayır için 'h'): ").lower() == "e"

    # Rakam istiyor mu?
    # Evet için 'e', Hayır için 'h' yaz ve Enter'a bas
    rakam = input("Rakam olsun mu? (evet için 'e', hayır için 'h'): ").lower() == "e"

    # Sembol istiyor mu?
    # Evet için 'e', Hayır için 'h' yaz ve Enter'a bas
    sembol = input("Sembol olsun mu? (!@#$ gibi) (evet için 'e', hayır için 'h'): ").lower() == "e"

    # Kaç tane şifre üretilsin?
    while True:
        try:
            adet = int(input("Kaç şifre üreteyim? (1-10): "))
            if 1 <= adet <= 10:
                break
            else:
                print("Lütfen 1 ile 10 arasında bir sayı gir.")
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")

    # Şifreleri üret ve ekrana yaz
    print("\n" + "=" * 40)
    print("Üretilen Şifreler:")
    print("=" * 40)
    for i in range(adet):
        sifre = sifre_uret(uzunluk, buyuk_harf, rakam, sembol)
        print(f"{i + 1}. {sifre}")

    print("=" * 40)


main()
