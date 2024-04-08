""" 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

number_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)

for _ in range(10):
    user_guess = int(input("Угадайте число от 0 до 1000: "))
    if user_guess < number_to_guess:
        print("Больше")
    elif user_guess > number_to_guess:
        print("Меньше")
    else:
        print("Вы угадали число!")
        break
else:
    print(f"Попытки закончились. Загаданное число было {number_to_guess}")
