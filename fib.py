# Возвращает первые х четных элемента последовательности Фибаначчи

def fib(x):
    fib_list = []

    # формируем последовательность до последнего четного элемента, который нам нужен
    for i in range(x * 3 - 1):
        if i == 0:
            fib_list.append(i)
        elif i == 1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            res = list(filter(lambda x: x % 2 == 0, fib_list))
    return res
