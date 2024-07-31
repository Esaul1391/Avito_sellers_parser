from collections import Counter
from bs4 import BeautifulSoup


def find_best_rating():
    path = r'C:\Users\13\Desktop\Avito_sellers_parser\data\raiting_selltrs.html'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            print("HTML файл найден")
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return

    soup = BeautifulSoup(html_content, 'lxml')
    sellers_link_tag = soup.find_all('span', class_='styles-module-size_m-n6S6Y')
    sale_text = [tag.text for tag in sellers_link_tag]
    top_dict = Counter(sale_text)
    return top_dict


print(find_best_rating())