"""
Напишите реализацию функции factorize, которая принимает список чисел и возвращает список
чисел, на которые числа из входного списка делятся без остатка.
Реализуйте синхронную версию и измерьте время выполнения.
Потом улучшите производительность вашей функции, реализовав использование нескольких ядер процессора для
параллельных вычислений, и замерьте время выполнения опять.
"""

from multiprocessing import Process, RLock as PrLock
from time import time


def factorize(*number):
    list_number = [*number]
    result = {}

    for i in list_number:
        result_list = []
        for el in range(1, i + 1):
            if i % el == 0:
                result_list.append(el)
        result.update({i: result_list})

    return result


def factorize_parallel(number, lock):
    result_list = []
    result = {}

    for el in range(1, number + 1):
        if number % el == 0:
            result_list.append(el)
    result.update({number: el})

    return result


if __name__ == '__main__':

    timer_s = time()
    factorize(128, 255, 99999, 10651060)
    print(f"Time for sync process: {round(time() - timer_s, 4)}")

    pr_lock = PrLock()
    processes = [
        Process(target=factorize_parallel, args=(128, pr_lock)),
        Process(target=factorize_parallel, args=(255, pr_lock)),
        Process(target=factorize_parallel, args=(99999, pr_lock)),
        Process(target=factorize_parallel, args=(10651060, pr_lock)),
    ]

    timer_p = time()
    [pr.start() for pr in processes]
    [pr.join() for pr in processes]
    [pr.close() for pr in processes]
    print(f"Time for parallel process: {round(time() - timer_p, 4)}")


