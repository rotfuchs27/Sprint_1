def digit_root(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

print('Цифровой корень числа 4851: ', digit_root(4851))  
print('Цифровой корень числа 97569: ', digit_root(97569))  
print('Цифровой корень числа 889987: ', digit_root(889987))  