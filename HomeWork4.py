#1. 
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# def Pi(number: float='')-> int:
#     s = str(number)
#     d=abs(s.find('.') - (len(s)) +1)
#     from math import pi
#     p=round(pi,d)
#     print(f' Число Пи с заданной точностью {d} равно {round(pi, d)}')

# N=input('Введите число: ')
# Pi(N)

# 2.
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = int(input("адайте натуральное число: "))

# n= int(input("Введите список чисел, разделенных пробелом: "))
# i = 2
# my_list = []
# while i * i <= n:
#     while n % i == 0:
#         my_list.append(i)
#         n = n / i
#     i = i + 1
# if n > 1:
#     my_list.append(n)
# print(my_list)

#3. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# entered_list = input("Введите список чисел, разделенных пробелом: ").split()
# myset = set(entered_list)
# print(myset)

# from random import random
# data=[]
# for j in range(10):
#     data.append(int(random()*10))
# print(data)
# my_list=[]
# for i in data:
#     print(data.count(i))
#     if data.count(i)==1:
#         my_list.append(i)
# print(my_list)

# def unique_list(data:list=[])-> int:
#     my_list=[]
#     for i in data:
#         if data.count(i)==1:
#             my_list.append(i)
#     return my_list

# data = input("Введите список чисел, разделенных пробелом: ").split()
# print(unique_list(data))

#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.



#5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()

# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')

