#gfhdthev
#Поиск НОДа двух чисел


#функция для поиска НОДа двух чисел, с помощью алгоритма Евклида
def gcd(a, b):
    if a == 0 or b == 0: 
        return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)

#функция main
def main():
    #просим пользователя ввести 2 числа
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    print(gcd(first, second))


#проверяем на прямой запуск
if __name__ == '__main__':
    main()