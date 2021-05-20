import datetime

print("""Написать декоратор для подсчета времени выполнения функции""")


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print('Получена функция {} в качестве аргумента'.format(func))
        beg = datetime.datetime.now().timestamp()
        return_val = func(*args, **kwargs)
        end = datetime.datetime.now().timestamp()
        print('Время выполнения {} секунд'.format(end - beg))
        return return_val
    return wrapper


@decorator_func
def iteration(m):
    for x in range(m):
        x += x
    print('Итераций {}'.format(m))

iteration(1000000)
