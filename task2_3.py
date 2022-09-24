# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
k = int(input("Введите k: "))
lest = [round((1 + 1/k)**k, 5) for k in range(1, k+1)]
print(lest)
print(round(sum(lest),5))