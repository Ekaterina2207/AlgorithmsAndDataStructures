#Сортировка по частоте встречаемости
#Задача: отсортировать список слов по частоте их встречаемости в тексте.
#Пример: ["apple", "banana", "apple", "cherry", "banana"] → ["apple", "banana", "cherry"]

import pandas as pd

def sort_words(items):
    series = pd.Series(items)
    value_counts = series.value_counts()
    result = []
    for value, count in value_counts.items():
        result.extend([value] * count)
    return result

def delete_duplicates(items):
    if len(items) <= 1:
        return items
    if items[0] == items[1]:
        return delete_duplicates(items[1:])
    else:
        return [items[0]] + delete_duplicates(items[1:])
words = ["apple", "banana", "apple", "cherry", "banana"]
print(delete_duplicates(sort_words(words)))