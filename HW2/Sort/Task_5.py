#Сортировка с сохранением исходных индексов
#Задача: отсортировать список чисел, но сохранить исходные индексы элементов.
#Пример: [5, 2, 9, 1] → [(3, 1), (1, 2), (0, 5), (2, 9)]

def index_sort(numbers):
    indexed_numbers = list(enumerate(numbers))
    sorted_numbers = sorted(indexed_numbers, key=lambda x: x[1])

    return sorted_numbers

numbers = [5, 2, 9, 1]
print(index_sort(numbers))
