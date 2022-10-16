# Реализуйте алгоритм перемешивания списка.

ran = range(1, 8)
numbers = list(ran)
print("Текущий массив", numbers)
k = -1
for i in range(len(numbers) // 2):
    numbers[k], numbers[i] = numbers[i], numbers[k]
    k -= 2
print("Перемешанный массив", numbers )