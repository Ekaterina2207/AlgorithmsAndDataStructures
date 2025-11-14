#Задача: отсортировать список строк по их длине в порядке возрастания.
#Пример: ["apple", "banana", "kiwi", "pear"] → ["kiwi", "pear", "apple", "banana"]

lst = ["apple", "banana", "kiwi", "pear"]
lst.sort(key=len)
print(lst)