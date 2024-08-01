import json
from collections import Counter
from bs4 import BeautifulSoup

def load_sellers(filepath):
    """Load sellers data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            sellers = json.load(file)
        return sellers
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON из файла: {filepath}")
        return {}

def save_sellers(sellers, filepath):
    """Save sellers data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(sellers, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка записи файла: {e}")

def find_best_rating():
    path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\raiting_selltrs.html'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            print("HTML файл найден")
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return {}

    soup = BeautifulSoup(html_content, 'lxml')
    sellers_link_tag = soup.find_all('span', class_='styles-module-size_m-n6S6Y')
    sale_text = [tag.text for tag in sellers_link_tag]
    top_dict = Counter(sale_text)
    print(top_dict)
    return top_dict


def update_top_sales_for_user(sellers_file_path, best_sales):
    sellers = load_sellers(sellers_file_path)
    print()
    print(sellers)
    seller_name = input("Введите имя пользователя, которому нужно добавить данные рейтинга: ")

    if seller_name not in sellers:
        print(f"Пользователь с именем {seller_name} не найден.")
        return
    print(sellers[seller_name])

    # Добавляем все товары из best_sales в top_sales выбранного продавца
    sellers[seller_name]["top_sales"] = list(best_sales.most_common(7))

    print(f"Обновлены топ продажи для {seller_name}: {sellers[seller_name]['top_sales']}")

    save_sellers(sellers, sellers_file_path)

# Загрузка и обновление информации о продажах
best_sales = find_best_rating()
sellers_file_path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\sellers_link.json'
update_top_sales_for_user(sellers_file_path, best_sales)





# from collections import Counter
# from bs4 import BeautifulSoup
#
#
# def find_best_rating():
#     path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\raiting_selltrs.html'
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             html_content = file.read()
#             print("HTML файл найден")
#     except FileNotFoundError:
#         print(f"Файл не найден: {path}")
#         return
#
#     soup = BeautifulSoup(html_content, 'lxml')
#     sellers_link_tag = soup.find_all('span', class_='styles-module-size_m-n6S6Y')
#     sale_text = [tag.text for tag in sellers_link_tag]
#     top_dict = Counter(sale_text)
#     return top_dict
#
#
# print(find_best_rating())