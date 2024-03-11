from requests import get
import json

url = "https://opentdb.com/api.php"

with open("categories_data.json", "r") as file:
    categories_data = json.load(file)

for category, data in categories_data.items():
    for number in [10, 20, 30, 40, 50]:
        if data['number_of_questions'] in [0, number - 10]:
            n = number
            params = {
                "amount": n,
                "category": data['id'],
                "type": "boolean"
            }
            response = get(url, params=params).json()
            while response['response_code'] != 0 and n >= number - 10:
                n -= 1
                params = {
                    "amount": n,
                    "category": data['id'],
                    "type": "boolean"
                }
                response = get(url, params=params).json()
            data['number_of_questions'] = n

with open("categories_data.json", "w") as file:
    json.dump(categories_data, file, indent=4)