from bs4 import BeautifulSoup
import logging
from parser_reiting.date_sellers import load_sellers, save_sellers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Продовцы которых я не буду проверять
seller_name_no_search = ['Техношоп']


def update_sellers():
    sellers_link = load_sellers()  # Загружаем существующий словарь
    updated_sellers_link = check_new_seller(sellers_link)  # Проверяю наличие продавцов и обновляю словарь

    if updated_sellers_link:
        save_sellers(updated_sellers_link)  # Сохраняем обновленный словарь
    else:
        logger.warning('Продавцов не нашлось!')


def check_new_seller(sellers_link: dict) -> dict:
    """
        Проверяет новый HTML файл на наличие новых продавцов и добавляет их в словарь.
        """
    path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\1.html'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            logger.info("HTML файл найден")
    except FileNotFoundError:
        logger.warning(f"Файл не найден: {path}")
        return

    soup = BeautifulSoup(html_content, 'lxml')
    sellers_link_tag = soup.find_all('a', {'data-marker': 'favorite-seller-head'})

    if not sellers_link_tag:
        logger.warning("Не найдены ссылки")
    else:
        logger.info(f"Найдено {len(sellers_link_tag)} ссылок.")

    for tag in sellers_link_tag:
        seller = tag.get('href')
        name = tag.find('span', {'data-marker': 'name'}).text
        # print(name)
        if seller and name not in seller_name_no_search:
            key = name
            link = f"http://www.avito.ru{seller}"
            if key and key not in sellers_link:
                sellers_link[key] = {'link': link, 'top sales': {}}
                logger.info(f"Добавил продавца: {key} -> {link}")

    return sellers_link
