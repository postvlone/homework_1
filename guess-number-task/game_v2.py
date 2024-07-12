"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Инициализируем счетчик попыток
    # Инициализируем верхнюю и нижнюю границы поиска
    low = 1
    high = 100
    
    # Начинаем цикл, который будет продолжаться до тех пор, пока нижняя граница не станет больше верхней
    while low <= high:
        count += 1
        predict = (low + high) // 2 # Предполагаемое число - середина текущего интервала
        if predict == number:
            return count
        elif predict < number:
            low = predict + 1  # Если предположение меньше загаданного числа, сдвигаем нижнюю границу
        else:
            high = predict - 1 # И наоборот

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)