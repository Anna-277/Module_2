first = int(input("Введите число "))
second = int(input("Введите число "))
third = int(input("Введите число "))

# Если все числа равны между собой, то вывести 3.
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2.
# Если равных чисел среди 3-х вообще нет, то вывести 0.
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)


