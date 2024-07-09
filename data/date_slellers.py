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



#
# # date_sellers.py
# import json
#
# def load_sellers(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}
#
# def save_sellers(sellers_link, file_path):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         json.dump(sellers_link, file, ensure_ascii=False, indent=4)
