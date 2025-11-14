#Сортировка чисел по убыванию
#Задача: отсортировать список чисел в порядке убывания, не используя встроенные методы сортировки.
#Пример: [5, 2, 9, 1, 5] → [9, 5, 5, 2, 1]

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
numbers = [5,2,9,1,5,6]
print(quick_sort(numbers))