#Создайте JSON-объект, представляющий каталог товаров с вложенной структурой
# (категория → подкатегория → товары). Реализуйте поиск товара по названию.
import json

def find_goods(data, goods_name, current_path=''):
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f'{current_path}.{key}' if current_path else key
            if value == goods_name:
                results.append(new_path)
                continue
            results.extend(find_goods(value, goods_name, new_path))
    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_path = f'{current_path}[{index}]'
            if value == goods_name:
                results.append(new_path)
                continue
            results.extend(find_goods(value, goods_name, new_path))
    else:
        if data == goods_name:
            results.append(current_path)
    return results

with open('goods.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

target = input('Введите название товара: ')
result = find_goods(data, target)

print(f'Найдено {len(result)} совпадений:')
print(result)