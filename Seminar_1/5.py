#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input("Введите день недели "))
match a:
    case 1:
        print("Понедельник")
    case 2:
        print("Вторник")
    case 3:
        print("Среда")
    case 4:
        print("Четверг")
    case 5:
        print("Пятница")
    case 6:
        print("Суббота")
    case 7:
        print("Воскресенье")
    case _:
        print("Не является днем недели")
