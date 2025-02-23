import json

PYTHON_VALUE = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

json_data = json.dumps(PYTHON_VALUE)
print(json_data)
