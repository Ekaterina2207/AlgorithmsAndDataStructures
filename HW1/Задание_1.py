#задание_1

import json
json_string = '{"name": "John", "age": "25", "score": ["5","3", "4"]}'
data = json.loads(json_string)
print(data)


