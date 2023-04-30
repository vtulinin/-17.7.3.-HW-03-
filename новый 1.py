Задание 17.7.3.
#  Метод № 1.
money = int(input("Пожалуйста,введите сумму, которую планируете положить под проценты:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int((per_cent['ТКБ']) * (money/100))
SKB = int((per_cent['СКБ']) * (money/100))
VTB = int((per_cent['ВТБ']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))
deposit = [TKB, SKB, VTB, SBER]
print("Накопленные средства за год вклада в каждом из банков =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))

# метод № 2.
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую Вы планируете положить под проценты:"))
A = per_cent.get('ТКБ')
Bank1 = int(A*(money/100))
B = per_cent.get('СКБ')
Bank2 = int(B*(money/100))
C= per_cent.get('ВТБ')
Bank3 = int(C*(money/100))
D = per_cent.get('СБЕР')
Bank4 = int(D*(money/100))
deposit = [Bank1,Bank2,Bank3,Bank4]
print("Накопленные средства за год вклада в каждом из банков =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))

