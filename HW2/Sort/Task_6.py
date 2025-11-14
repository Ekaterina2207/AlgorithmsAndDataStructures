#Сортировка с удалением дубликатов
#Задача: отсортировать список чисел, удалив дубликаты.
#Пример: [5, 2, 9, 1, 5, 2] → [1, 2, 5, 9]

def delete_duplicates(items):
    if len(items) <= 1:
        return items
    if items[0] == items[1]:
        return delete_duplicates(items[1:])
    else:
        return [items[0]] + delete_duplicates(items[1:])
numbers = [5, 2, 9, 1, 5, 2]
sorted_numbers = sorted(numbers)
print(delete_duplicates(sorted_numbers))