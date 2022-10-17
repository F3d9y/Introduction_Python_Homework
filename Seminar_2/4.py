#Реализуйте алгоритм перемешивания списка.
import random

list = [1,2,3,4,5,6,7,8,9,10]

list_shuf = []

for i in range(0, len(list)):
    j = random.randrange(0, len(list))
    list_shuf.append(list[j])
    list.remove(list[j])

print(list_shuf)