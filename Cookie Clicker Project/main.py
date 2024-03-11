from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import *
from time import sleep
import threading
from urllib3.exceptions import *
import lxml

cookies_per_second_dictionary = {"Cursor": 0.1, "Grandma": 1, "Farm": 8, "Mine": 47, "Factory": 260}


def convert_to_integer(number_string):
    values_dict = {"million": 6, "billion": 9, "trillion": 12, "quadrillion": 15, "quintillion": 18, "sextillion": 21,
                   "septillion": 24, "octillion": 27}
    for word, number_of_digits in values_dict.items():
        number_string.replace(f" {word}", "0" * number_of_digits)
    return float(number_string.replace(",", ""))


def event_one():
    global big_cookie, game_over
    while not game_over:
        try:
            big_cookie = driver.find_element(By.ID, "bigCookie")
            try:
                big_cookie.click()
            except (ElementClickInterceptedException, StaleElementReferenceException):
                driver.execute_script("arguments[0].click()", driver.find_element(By.ID, "bigCookie"))
            except NoSuchElementException:
                pass
        except (NoSuchWindowException, InvalidSessionIdException, AttributeError, KeyboardInterrupt, MaxRetryError, ProtocolError, ConnectionError, ConnectTimeoutError):
            pass


def event_two():
    global game_over
    try:
        while not game_over:
            try:
                sleep(5)
                upgrades_available = driver.find_elements(By.CSS_SELECTOR, "div.crate.upgrade.enabled")
                while len(upgrades_available) != 0:
                    try:
                        driver.execute_script("arguments[0].click()", driver.find_elements(By.CSS_SELECTOR, "div.crate.upgrade.enabled")[-1])
                    except IndexError as error:
                        pass
                    upgrades_available = driver.find_elements(By.CSS_SELECTOR, "div.crate.upgrade.enabled")

                items_available = driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")
                if len(items_available) != 0:
                    try:
                        prices = [convert_to_integer(item.find_element(By.CSS_SELECTOR, "span.price").text) for item in items_available]
                    except StaleElementReferenceException:
                        prices = [convert_to_integer(element.text) for element in driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled span.price")]
                    try:
                        names = [item.find_element(By.CSS_SELECTOR, "div.title.productName").text for item in items_available]
                    except StaleElementReferenceException:
                        names = [item.text for item in driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled div.title.productName")]
                    CpS_per_dollar = [cookies_per_second_dictionary.get(names[n])/prices[n] for n in range(len(items_available))]
                    number_of_cookies = convert_to_integer(driver.find_element(By.ID, "cookies").text.split()[0])
                    item_to_buy_index = CpS_per_dollar.index(max(CpS_per_dollar))
                    soup = BeautifulSoup(driver.page_source, 'lxml')
                    cookies_per_second_initially = convert_to_integer(soup.select_one(selector="#cookiesPerSecond").text.split(": ")[1])
                    for n in range(int(number_of_cookies//prices[item_to_buy_index])):
                        try:
                            driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")[item_to_buy_index].click()
                        except (ElementClickInterceptedException, StaleElementReferenceException):
                            try:
                                element = driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")[item_to_buy_index]
                                driver.execute_script("arguments[0].scrollIntoView();", element)
                                driver.execute_script("arguments[0].click();", element)
                            except:
                                pass
                        except IndexError:
                            pass
                        if n == 0:
                            soup = BeautifulSoup(driver.page_source, 'lxml')
                            cookies_per_second_finally = convert_to_integer(soup.select_one(selector="#cookiesPerSecond").text.split(": ")[1])
                            marginal_change = round(cookies_per_second_finally - cookies_per_second_initially, 2)
                            if marginal_change != 0 and abs(marginal_change - cookies_per_second_dictionary[names[item_to_buy_index]]) >= 0.099:
                                cookies_per_second_dictionary[names[item_to_buy_index]] = round(marginal_change, 1)
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException) as error:
                pass
    except (NoSuchWindowException, InvalidSessionIdException, AttributeError, KeyboardInterrupt, MaxRetryError, ProtocolError, ConnectionError, ConnectTimeoutError):
        pass


def event_three():
    global game_over
    try:
        sleep(100)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        cookies_per_second = convert_to_integer(soup.select_one(selector="#cookiesPerSecond").text.split(": ")[1])
        print(cookies_per_second)
        game_over = True
        driver.quit()
    except (NoSuchWindowException, InvalidSessionIdException, AttributeError, KeyboardInterrupt, MaxRetryError, ProtocolError, ConnectionError, ConnectTimeoutError):
        pass


url = "https://orteil.dashnet.org/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

max_number_of_attempts = 20
sleep_time = 5
game_over = False

for attempt in range(max_number_of_attempts):
    try:
        select_language = driver.find_element(By.ID, "langSelect-EN")
        select_language.click()
        break
    except NoSuchElementException as error:
        sleep(sleep_time)
        if attempt == max_number_of_attempts - 1:
            print(f"Sorry. Unable to select the required language. Here is the error:\n{error}")
    except (ElementClickInterceptedException, StaleElementReferenceException):
        driver.execute_script("arguments[0].click()", driver.find_element(By.ID, "langSelect-EN"))
        break

for attempt in range(max_number_of_attempts):
    try:
        big_cookie = driver.find_element(By.ID, "bigCookie")
        break
    except NoSuchElementException:
        sleep(sleep_time)

thread1 = threading.Thread(target=event_one)
thread2 = threading.Thread(target=event_two)
thread3 = threading.Thread(target=event_three)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

driver.quit()