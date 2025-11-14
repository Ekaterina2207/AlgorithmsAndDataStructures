#Задача: отсортировать список чисел по сумме их цифр.
#Пример: [123, 45, 6, 789] → [6, 123, 45, 789] (суммы: 6, 6, 9, 24)

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
lst = [123, 45, 6, 789]
lst_changed = []
for x in lst:
    total = 0
    while x > 0:
        total += x%10
        x = x // 10
    lst_changed.append(total)
print(quick_sort(lst_changed))


