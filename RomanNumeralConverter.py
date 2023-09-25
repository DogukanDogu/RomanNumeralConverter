def roman_to_decimal(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]

        if value < prev_value:
            decimal -= value
        else:
            decimal += value

        prev_value = value

    return decimal

def decimal_to_roman(decimal):
    if not (0 < decimal < 5000):
        return "Yanlış değer..."

    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    roman = ""
    for value in sorted(roman_numerals.keys(), reverse=True):
        while decimal >= value:
            roman += roman_numerals[value]
            decimal -= value

    return roman

while True:
    print("Seçenekler:")
    print("Roma rakamlarından tam sayıya çevirmek için 1 yazınız.")
    print("Tam sayıdan Roma rakamlarına çevirmek için 2 yazınız")
    print("Çıkış için 3 yazınız")

    choice = input("Lütfen seçim yapınız : (1 - 2 - 3) : ")

    if choice == '1':
        roman_numeral = input("Lütfen Roma rakamı giriniz: ").upper()
        decimal_value = roman_to_decimal(roman_numeral)
        print(f"Sayı karşılığı : {decimal_value}")
    elif choice == '2':
        decimal_value = int(input("(1-4999) arasında tam sayı giriniz: "))
        roman_numeral = decimal_to_roman(decimal_value)
        print(f"Roma rakamı karşılığı: {roman_numeral}")
    elif choice == '3':
        break
    else:
        print("Yanlış değer. Lütfen tekrar deneyiniz...")
