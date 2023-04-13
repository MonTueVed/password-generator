import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def generate_password(len, chars):
    password = ''
    for j in range (len):
        password += random.choice(chars)
    return password

def settings():
    print('сколько паролей нужно?')
    kol_par = int(input())
    print('длина пароля?')
    len_par = int(input())
    print('включать ли цифры? y-ДА, n-НЕТ')
    be_digits = input()
    print('включать ли прописные буквы? y-ДА, n-НЕТ')
    be_low = input()
    print('включать ли заглавные буквы? y-ДА, n-НЕТ')
    be_up = input()
    print('включать ли символы? y-ДА, n-НЕТ')
    be_punctuation = input()
    print('исключать неоднозначые символы: iIlL10oO')
    adekvat = input()
    return kol_par, len_par, be_digits, be_low, be_up, be_punctuation, adekvat

k, len, bd, bl, bu, bp, a = settings()

if a == 'y':
    digits = digits.replace('0', '1')
    digits = digits.replace('1', '')
    lowercase_letters = lowercase_letters.replace('i', 'l')
    lowercase_letters = lowercase_letters.replace('l', 'o')
    lowercase_letters = lowercase_letters.replace('o', '')
    uppercase_letters = uppercase_letters.replace('I', 'L')
    uppercase_letters = uppercase_letters.replace('L', 'O')
    uppercase_letters = uppercase_letters.replace('O', '')
if bd == 'y':
    chars += digits
if bl == 'y':
    chars += lowercase_letters
if bu == 'y':
    chars += uppercase_letters
if bp == 'y':
    chars += punctuation

for i in range(k):
    password = generate_password(len, chars)
    print('Ваш случайный пароль: ', password)

print('Press any key to close')
s = input()
