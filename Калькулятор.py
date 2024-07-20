print("Калькулятор")
while True:
    print("Выбереде режим:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Выйти")
    x=int(input())
    if x==1:
        print("Режим: Сложение")
        print("Введите числа через пробел")
        a=int(input())
        b=int(input())
        c=a+b
        print("Ответ: ", c)
    elif x==2:
        print("Режим: Вычитание")
        print("Введите числа через пробел")
        a=int(input())
        b=int(input())
        c=a-b
        print("Ответ: ", c)
    elif x==3:
        print("Режим: Умножения")
        print("Введите числа через пробел")
        a=int(input())
        b=int(input())
        c=a*b
        print("Ответ: ", c)
    elif x==4:
        print("Режим: Деление")
        print("Введите числа через пробел")
        a=int(input())
        b=int(input())
        c=a/b
        print("Ответ: ", c)
    elif x==5:
        print("Приложение закрыто.")
        break