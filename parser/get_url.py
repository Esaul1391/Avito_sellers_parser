import time

import undetected_chromedriver as uc


def get_url(url):
    driver = uc.Chrome( )
    driver.get(url)
    time.sleep(22)
    print(driver.title)
    # driver.save_screenshot('nowsecure.png')


def main():
    url = 'http://www.avito.ru/moskva/predlozheniya_uslug/oborudovanie_proizvodstvo/proizvodstvo_obrabotka-ASgBAgICAkSYC7SfAaALiKAB?cd=1&p=1&q=3d+печать'
    get_url(url)



if __name__ == "__main__":
    main()