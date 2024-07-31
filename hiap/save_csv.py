import csv
import os
import random
import time
from collections import Counter

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium_stealth import stealth


def save_to_csv(data):
    file_exists = os.path.isfile('3d.csv')

    # Открываем CSV файл для записи (если он не существует, он будет создан)
    with open('3d.csv', mode='a', newline='', encoding='utf-8') as file:
        # Создаем объект writer для записи данных в файл
        writer = csv.writer(file)

        if not file_exists:
            # Записываем заголовки только если файл не существует
            writer.writerow(['Name', 'ID', 'Data_time', 'View', 'Имя магазина', 'reiting'])

        # Записываем данные в файл
        for item in data:
            writer.writerow(item)