import csv

fieldname=['title', 'author', 'year']

books = [
    {'title': 'Война и мир', 'author': 'Толстой', 'year': 1869},
    {'title': '1984', 'author': 'Оруэлл', 'year': 1949}
]

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(books)


