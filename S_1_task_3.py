
"""Проверить год - високосный или нет"""

IGNORE = 1582
year = int(input("Введите год после 1582: "))
if year < IGNORE:
    print("Слишком ранний год")
else:
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print("Високосный год")
    else:
        print("Обычный год")
        


