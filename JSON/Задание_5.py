def open_json(filename: str):
    if filename.split('.')[-1] != 'json':
        print("Некорректный формат файла")
        return None
    try:
        f = open(filename, 'rb')
        data = json.load(f)
        return data
    except IOError:
        print("Could not open/read file:", filename)
        return None
    except json.decoder.JSONDecodeError:
        print("Invalid JSON")
        return None

my_filename = input()
result = open_json(my_filename)
if result:
    print(result)