#gfhdthev
#объединение 3 программ


#импортируе необходимые модули
import notation
import pascal
import euclid


#главная функция
def main():
    print('E - Вычисление НОДа\nN - Перевод числа в другую систему счисления\nP - Ввывод строчек треугоника Паскаля')
    user_input = str(input('Введите букву: '))

    if user_input.lower() == 'e':
        euclid.main()
        main()
    elif user_input.lower() == 'n':
        notation.main()
        main()
    elif user_input.lower() == 'p':
        pascal.main()
        main()
    else:
        return 1


#проверяем на прямой запуск
if __name__ == '__main__':
    main()