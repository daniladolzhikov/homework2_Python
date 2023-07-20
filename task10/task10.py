# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть

import random

n = int(input('Введите кол-во момент: '))
count_tails = 0
count_eagle = 0

for n in range(n):
    coins = random.choice(['tails', 'eagle'])
    if coins == 'tails':
        count_tails += 1
    elif coins == 'eagle':
        count_eagle +=1
print('Решка:', count_tails)
print('Орел:', count_eagle)

if count_tails < count_eagle:
    print ('Минимальное кол-во переворотов: ', count_tails)
else:
    print ('Минимальное кол-во переворотов: ', count_eagle)

