def process_seller(driver):
    try:
        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
        driver.find_element(By.CSS_SELECTOR, '[data-marker="seller-link/link"]').click()
        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка

        rating = driver.find_element(By.CSS_SELECTOR, '[data-marker="profile/summary"]').text
        print(rating)
        driver.find_element(By.CSS_SELECTOR, '[data-marker="profile/summary"]').click()
        time.sleep(random.uniform(min_delay, max_delay))  # Случайная задержка
        rating_list = []
        # Скролл к кнопке "Показать еще отзывы"
        while True:
            try:
                # Скролл к кнопке "Показать еще отзывы" и кликнуть на нее
                more_reviews_button = driver.find_element(By.CSS_SELECTOR, '[data-marker="rating-list/moreReviewsButton"]')

                scroll_to_element(driver, more_reviews_button)
                more_reviews_button.click()
                time.sleep(random.uniform(min_delay, max_delay))
            except Exception as e:
                break  # Выход из цикла при отсутствии кнопки "Показать еще отзывы"
                # Поиск элементов с классом "desktop-35wlrd"
            desktop_elements = driver.find_elements(By.CLASS_NAME, 'desktop-35wlrd')

            # Преобразуем элементы в их текстовое представление перед подсчетом
            element_texts = [rating_list.append(element.text) for element in desktop_elements]
        element_counts = Counter(rating_list)

        # Находим три самых повторяющихся элемента
        top_elements = element_counts.most_common(3)
        print(top_elements)
        return top_elements
    except:
        print("Нет оценок")
        return "Не кликается"
