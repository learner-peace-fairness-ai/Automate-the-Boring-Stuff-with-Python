import json

JSON_DATA = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

json_data_as_python_value = json.loads(JSON_DATA)
print(json_data_as_python_value)
