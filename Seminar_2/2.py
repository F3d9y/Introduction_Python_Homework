#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
a = int(input("Введите число N: "))

def array_digits_mltiplier (n):
    listA = []
    buf = 1
    for i in range (1,n+1):
        listA.append(i*buf)
        buf*=i
    return listA

print ("Набор результатов произведений чисел от 1 до N:", (array_digits_mltiplier(a)))