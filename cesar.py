def encrypt(k, m):  # Шифровка кодом Цезаря
    encst = ''
    for sym in m:
        encst += chr(ord(sym)+k)
    return encst

def decrypt(k, c):  # Дешифровка кода Цезаря с ключом
    decst = ''
    for sym in c:
        decst += chr(ord(sym)-k)
    return decst

def decrypt_without_key(line):  # Дешифровка кода Цезаря без ключа
    sym_set = list(set(line))
    sym_dct = {}
    for sym in sym_set:
        l = []
        for el in line:
            if sym == el:
                l.append(el)
        sym_dct.update({sym: len(l)})

    max_el = ord(list(dict(reversed(sorted(sym_dct.items(), key=lambda item: item[1]))))[0])

    space_num = ord(' ')

    k = abs(space_num - max_el)

    return decrypt(k, line)

def vernam(key, line):  # Шифровка кодом Вернама работает в две стороны
    if len(key) != 8:
        print('Ключ меньше 8')
        quit()

    code_list = []
    for sym in line:

        bin_sym = bin(ord(sym))[2:]
        if len(bin_sym) != 8:
            bin_sym = '0' + bin_sym
            while len(bin_sym) != 8:
                bin_sym = '0' + bin_sym
        print(bin_sym)
        encrypt_sym = ''

        for i in range(len(key)):
            if bin_sym[i] == key[i]:
                encrypt_sym += '0'
            else:
                encrypt_sym += '1'
        print(encrypt_sym)

        code_list.append('0b'+encrypt_sym)
    sym_encrypt_list = list(map(lambda x: chr(int(x, base=2)), code_list))  # Символьная шифровка
    print(code_list)  # Двоичная шифровка
    return f'{line} --> {"".join(sym_encrypt_list)}'

print(vernam('00001111', ';e32'))
print(vernam('00001111', '4'))