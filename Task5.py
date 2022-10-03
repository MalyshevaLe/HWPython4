# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

# записываем в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

# создаем случайное числа от 0 до 100
def rnd():
    return random.randint(0,101)

# создаем коэффициенты многочлена
def create_poly(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
# создаем многочлен в виде строки 
def create_str(spl):
    lst= spl[::-1]
    comp = ''
    if len(lst) < 1:
        comp = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                comp += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    comp += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                comp += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    comp += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                comp += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                comp += ' = 0'
    return comp

# получение степени многочлена
def sq_poly(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# находим коэффицент члена многочлена
def k_poly(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# производим разбор многочлена и получение его коэффициентов
def calc_poly(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_poly(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_poly(st[ii]) != -1 and sq_poly(st[ii]) == i:
            lst.append(k_poly(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    


# создаем два файла

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_poly(k1)
koef2 = create_poly(k2)
write_file("text1.txt", create_str(koef1))
write_file("text2.txt", create_str(koef2))

# находим сумму многочлена

with open('text1.txt', 'r') as data:
    st1 = data.readlines()
with open('text2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_poly(st1)
lst2 = calc_poly(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("text3_res.txt", create_str(lst_new))
with open('text3_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов {st3}")