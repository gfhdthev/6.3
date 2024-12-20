#gfhdthev
#Переввод какого-либо числа в какую-либо систему счисления


#словарь для черевода остатков деления в буквы
nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

#функция для печевода чисел в другую систему счисления
def convert_to_base(number, dev):
    if dev > number:
        return str(nums[number % dev]) if number % dev > 9 else str(number % dev)
    return convert_to_base(number // dev, dev) + (str(nums[number % dev]) if number % dev > 9 else str(number % dev))

#функция main
def main():
    #просим пользователя ввести данные
    first = int(input('Введите число: '))
    second = int(input('Введите в какую систему его перевести: '))
    print(convert_to_base(first, second))


#проверяем на прямой запуск
if __name__ == '__main__':
    main()