import json


def load_sellers():
    try:
        with open(r'C:\Users\13\Desktop\Avito_sellers_parser\data\sellers_link.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_sellers(sellers_link):
    with open(r'C:\Users\13\Desktop\Avito_sellers_parser\data\sellers_link.json', 'w', encoding='utf-8') as file:
        json.dump(sellers_link, file, ensure_ascii=False, indent=4)
