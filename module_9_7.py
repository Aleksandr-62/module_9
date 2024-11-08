#     Напишите 2 функции:

#  Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет
#  простым числом и "Составное" в противном случае.
def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)
        is_prime = True
        for i in range(2, sum_):
            if sum_ % i == 0:
                is_prime = False
        if is_prime == True:
            return (f'Простое\n{sum_}')
        else:
            return (f'Составное\n{sum_}')
    return wrapper


@is_prime
# Функция, которая складывает 3 числа (sum_three)
def sum_three(*args):
    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)
