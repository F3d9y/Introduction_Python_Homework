#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

N = int(input("Введите число N: "))

listInt = []
i = -N
while i<=N:
    listInt.append(i)
    i += 1

print(listInt)