import json

numbers = [2, 3, 4, 5, 65, 7]

filename = 'number.json'
with open(filename) as f_obj:
    json.dump(numbers, f_obj)
