# Задача 1. Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

num = float(input('Введите число: '))
d =  int(input('Задайте точность числа: '))
print(round(num, d))
