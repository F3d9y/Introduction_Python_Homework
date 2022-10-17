#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

a = int(input("Введите число n: "))

def array_digits_mltiplier (n):
    listA = []
    for i in range (1,n+1):
        listA.append((1+1/i)**i)
    return listA

print ("Последовательность (1+1/n)^n: ", (array_digits_mltiplier(a)))
print ("Сумма чисел последовательности: ", (sum(array_digits_mltiplier(a))))