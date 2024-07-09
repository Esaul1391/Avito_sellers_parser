from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import csv
from collections import Counter
import os





def scroll_to_element(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()