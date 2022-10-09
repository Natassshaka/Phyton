# Урок 3. Данные, функции и модули в Python

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = input("Задайте список из нескольких чисел: ").split()
# s_sum=0
# for i in range(1,len(my_list),2):
#     s_sum+=int(my_list[i])
# print(s_sum)

# def uneven_sum(my_list: list=[])-> int:
#     s_sum=0
#     for i in range(1,len(my_list),2):
#         s_sum+=int(my_list[i])
#     return(s_sum)

# my_list = input("Задайте список из нескольких чисел: ").split()
# print(uneven_sum(my_list))

# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_list = input("Задайте список из нескольких чисел: ").split()
# s_sum=0
# x=len(my_list)%2
# if x == 0:
#     for i in range(len(my_list)//2):
#         s_sum=int(my_list[i])*int(my_list[-(i+1)])
#         print(s_sum, end=' ')
# else:
#     for i in range(len(my_list)//2+1):
#         s_sum=int(my_list[i])*int(my_list[-(i+1)])
#         print(s_sum, end=' ')


#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# def delta_extrem(my_list: lst=[])-> float:
#     my_min=1
#     my_max=0
#     for i in lst:
#         x=float(i)%1
#         print(x)
#         if x<=my_min:
#             my_min=x
#         if x>=my_max:
#             my_max=x
#     print(my_max-my_min)

# lst = input("Введите числа через пробел:\n").split()
# delta_extrem(lst)
#  ---Вариант 2
# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# #  map  используется для применения фнкции к каждому элементу списка
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# 4. 
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# def decimalTo1Binary(n):
 
#     if (n > 1):
#         #делим число без остатка
#         decimalTo1Binary(n//2)
#     print(n%2, end='')

# n = int(input("Введите число: "))     
# decimalTo1Binary(n)    
 
# Вариат2 

# def decimal_to_binary(number: int=" ") -> int:
#     while number > 0:
#         print(number%2, end='')
#         number = number // 2
 
# number = int(input('Введите число:'))
# decimal_to_binary(number)

# 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# my_list= [1,1]
# for i in range(2, 10):
#     my_list.append(my_list[-1] + my_list[-2])
# print(my_list)

# new_list=my_list[:]
# for i in range(1,len(new_list),2):
#     new_list[i]=-new_list[i]
# print(new_list[::-1]+[0]+my_list)



    