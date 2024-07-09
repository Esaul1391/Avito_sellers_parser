from data.date_slellers import load_sellers, save_sellers
from data.sellers import check_new_seller

def main():
    sellers_link = load_sellers()  # Загружаем существующий словарь
    updated_sellers_link = check_new_seller(sellers_link)
    if updated_sellers_link:
        print("Updated sellers link dictionary:")
        print(updated_sellers_link)
        save_sellers(updated_sellers_link)  # Сохраняем обновленный словарь
    else:
        print("No sellers found or error occurred.")

if __name__ == "__main__":
    main()


# # main.py
# from data.sellers import update_sellers
#
# def main():
#     update_sellers()
#
# if __name__ == "__main__":
#     main()


# from parse_page import get_pages_html, parse_page
# from request_parametrs import get_target_url, request_param
#
#
# def main():
#     dict_param = request_param()
#     target_url = get_target_url(dict_param['target'], dict_param['min_price'], dict_param['max_price'])
#     print(target_url)
#
#     with get_pages_html(target_url) as driver:
#         parse_page(driver, dict_param['target'], dict_param['count_page'])
#
#
# if __name__ == "__main__":
#     main()

