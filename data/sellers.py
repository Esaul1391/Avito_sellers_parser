from bs4 import BeautifulSoup

from data.date_sellers import load_sellers, save_sellers


def update_sellers():
    sellers_link = load_sellers()  # Загружаем существующий словарь
    updated_sellers_link = check_new_seller(sellers_link)
    if updated_sellers_link:
        save_sellers(updated_sellers_link)  # Сохраняем обновленный словарь
    else:
        print("Продавцов не нашлось.")


def check_new_seller(sellers_link):
    path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\1.html'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            print("HTML файл найден")
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return

    soup = BeautifulSoup(html_content, 'lxml')
    sellers_link_tag = soup.find_all('a', {'data-marker': 'favorite-seller-head'})

    if not sellers_link_tag:
        print("Не найдены ссылки")
    else:
        print(f"Найдено {len(sellers_link_tag)} ссылок.")

    for tag in sellers_link_tag:
        seller = tag.get('href')
        if seller:
            key = seller[6:38]
            link = f"http://www.avito.ru{seller}"
            if key and key not in sellers_link:
                sellers_link[key] = link
                print(f"Добавил продавца: {key} -> {link}")

    return sellers_link  # Возвращаем словарь для проверки
