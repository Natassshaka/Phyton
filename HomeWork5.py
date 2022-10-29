#1.  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# def game(all):
#     from random import randint
#     # all=int(2021)
#     player_1=randint(1, 2)
#     count=1
#     while all>0:
#         x1=int(input("Укажите кол-во, не превышающее 28: "))
#         all-=x1
#         count+=1
#         # print(all)
#     # print(count)
#     return count

# def result_player(count):
#     from random import randint
#     player_1=randint(1, 2)
#     # print(player_1)
#     if player_1%2==count%2:
#         return 1
#     else:
#         return 2


# print(f'Игрок № {result_player(game(2021))}')

#--a) Добавим бота:
# def game(all):
#     # print(f"Очередность игрока {player_number}")
#     from random import randint
#     player_number=randint(1, 2)
#     print(f'Очередность игрока: {player_number}')
#     count=1
#     while all>0:
#         for i in range(1,3):
#             if all>0:
#                 if i==player_number:
#                     print(f'---Игрок №{i}')
#                     x=int(input("Укажите кол-во, не превышающее 28: "))
#                     all-=x
#                     print(f'Остаток: {all}') 
#                 else:
#                     print(f'---Игрок №{i}')
#                     from random import randint
#                     x=randint(1, 28)
#                     print(f'Бот указал: {x}')
#                     all-=x
#                     print(f'Остаток: {all}')                
#         count+=1
#     print(f'Счетчик:{count}')
#     # if count%2==0:
#     #     print(f'Выйграл игрок 2')
#     # else:
#     #     print(f'Выйграл игрок 1')
#     if count%player_number!=0:
#         print(f'Выйграл игрок')
#     else:
#         print(f'!!! Выйграл Бот')
# game(2021)


#  ---b) Подумайте как наделить бота ""интеллектом""


  

#3. Создайте программу для игры в ""Крестики-нолики"".
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# def printMatrix ( matrix ): 
#    for i in range ( len(matrix) ): 
#       for j in range ( len(matrix[i]) ): 
#           print ( "{:4d}".format(matrix[i][j]), end = "" ) 
#       print ()
# printMatrix(matrix)

# import numpy as np
# matrix = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(matrix)
# import numpy as np
# data = np.(10, size=(3,3))
# print(data)




example_array = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(example_array)):
    print(example_array[i])
print()


# print(example_array[0])
# print(example_array[1])
# print(example_array[2])

# print(example_array[1],[2])
# my_list=int(input("Укажите номер строки и столбца через пробел: "))
# x=example_array.index(2)
# print(x)
my_list = input("Укажите номер строки и столбца через пробел: ").split()
x1=int(my_list[0])-1
x2=int(my_list[1])-1
example_array[x1][x2] = х
for i in range(len(example_array)):
    print(example_array[i])



#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     deres = ''
#     for i in range(1,len(txt),2):
#         deres = deres + txt[i]*int(txt[i-1])
#     return deres

# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")