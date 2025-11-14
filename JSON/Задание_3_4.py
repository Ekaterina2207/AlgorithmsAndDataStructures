import json
def find_book(author: str, books: list):
    for book in books:
        if book['author'] == author:
            return book
    return None
with open('books.json', 'r') as file:
    data = json.load(file)
input_author = input('Введите автора: ') #здесь пишем автора
result = find_book(input_author, data)
if result:
    print(result)
else:
    print('Книга не найдена.')

