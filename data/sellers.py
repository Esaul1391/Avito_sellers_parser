import requests
from bs4 import BeautifulSoup

# sellers.py
from bs4 import BeautifulSoup


def check_new_seller(sellers_link):
    path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\1.html'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            print("HTML file read successfully.")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return

    soup = BeautifulSoup(html_content, 'lxml')
    sellers_link_tag = soup.find_all('a', {'data-marker': 'favorite-seller-head'})

    if not sellers_link_tag:
        print("No seller links found.")
    else:
        print(f"Found {len(sellers_link_tag)} seller links.")

    for tag in sellers_link_tag:
        seller = tag.get('href')
        if seller:
            print(f"Processing seller link: {seller}")
            key = seller[6:38]
            link = f"https://www.avito.ru{seller}"
            if key and key not in sellers_link:
                sellers_link[key] = link
                print(f"Added seller: {key} -> {link}")

    return sellers_link  # Возвращаем словарь для проверки

# def check_new_seller(sellers_link):
#     path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\1.html'
#     with open(path, 'r', encoding='utf-8') as file:
#         html_content = file.read()
#     soup = BeautifulSoup(html_content, 'lxml')
#
#     # Пример: извлекаем заголовок страницы
#     sellers_link_tag = soup.find_all('a', {'data-marker': 'favorite-seller-head'})
#
#     for tag in sellers_link_tag:
#
#         seller = tag.get('href')
#         key = seller[6:38]
#         link = f"https://www.avito.ru{seller}"
#         if key and key not in sellers_link:
#             sellers_link[key] = link
#             print(key)
#             print(link)
#     return sellers_link

#
# from bs4 import BeautifulSoup
# from data.date_sellers import load_sellers, save_sellers
#
#
# def check_new_seller(file_path, html_path):
#     sellers_link = load_sellers(file_path)  # Загружаем существующий словарь
#
#     try:
#         with open(html_path, 'r', encoding='utf-8') as file:
#             html_content = file.read()
#             print("HTML file read successfully.")
#     except FileNotFoundError:
#         print(f"File not found: {html_path}")
#         return
#
#     soup = BeautifulSoup(html_content, 'lxml')
#     sellers_link_tag = soup.find_all('a', {'data-marker': 'favorite-seller-head'})
#
#     if not sellers_link_tag:
#         print("No seller links found.")
#     else:
#         print(f"Found {len(sellers_link_tag)} seller links.")
#
#     for tag in sellers_link_tag:
#         seller = tag.get('href')
#         if seller:
#             print(f"Processing seller link: {seller}")
#             key = seller.split('/')[2]  # Извлекаем ключ из ссылки
#             link = f"https://www.avito.ru{seller}"
#             if key and key not in sellers_link:
#                 sellers_link[key] = link
#                 print(f"Added seller: {key} -> {link}")
#
#     save_sellers(sellers_link, file_path)  # Сохраняем обновленный словарь
#
#
# def update_sellers():
#     sellers_file_path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\sellers_link.json'
#     html_file_path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\1.html'
#     check_new_seller(sellers_file_path, html_file_path)