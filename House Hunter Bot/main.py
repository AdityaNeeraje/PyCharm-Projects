import requests
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import json
from urllib3.exceptions import *
from os import environ
import lxml

number_of_results = 90
max_number_of_attempts = 20
sleep_time = 5
property_list = []
list_of_titles = []
list_of_ids = []
list_of_prices = []
list_of_urls = []


def is_city(string):
    url = f'https://api.api-ninjas.com/v1/city?name={string}'
    response = requests.get(url, headers={'X-Api-Key': environ.get("API_KEY")})
    if response.status_code == requests.codes.ok:
        return True
    else:
        return False


url = "https://www.magicbricks.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
search_city = input("Please enter the name of the city you wish to hunt for houses in:\n").strip()

while not is_city(search_city):
    search_city = input("Please type in the name of a valid City, Locality or Project:\n").strip()

try:
    driver = webdriver.Chrome()
    driver.get(url)
    for attempt in range(max_number_of_attempts):
        try:
            driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "mb-search__tag-close"))
            break
        except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
            sleep(sleep_time)
            if attempt == max_number_of_attempts - 1:
                print("Sorry. Unable to load page correctly. Please try again later.")

    continue_searching = True
    while continue_searching:
        search_bar = driver.find_element(By.ID, "keyword")
        for search_attempt in range(max_number_of_attempts):
            try:
                search_bar.send_keys(search_city)
                sleep(2)
                if len(driver.find_elements(By.CSS_SELECTOR, "div.mb-search__auto-suggest__item")) == 0:
                    search_bar.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
                    search_city = input("Please type in the name of a valid City, Locality or Project:\n").strip()
                else:
                    try:
                        driver.find_element(By.CSS_SELECTOR, "div.mb-search__auto-suggest__item").click()
                        driver.find_element(By.CSS_SELECTOR, "div.mb-search__btn").click()
                    except (ElementClickInterceptedException, StaleElementReferenceException):
                        driver.execute_script("arguments[0].click();",
                                              driver.find_element(By.CSS_SELECTOR, "div.mb-search__auto-suggest__item"))
                        driver.execute_script("arguments[0].click();",
                                              driver.find_element(By.CSS_SELECTOR, "mb-search__btn"))
                    continue_searching = False
                break
            except NoSuchElementException:
                sleep(sleep_time)

    for attempt in range(max_number_of_attempts):
        try:
            number_of_listings = int(
                driver.find_element(By.CSS_SELECTOR, "div.mb-srp__title--text1").text.split()[0].replace(",", ""))
            break
        except (StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException) as error:
            sleep(sleep_time)
            if attempt == max_number_of_attempts - 1:
                print(f"Unable to count the number of listed properties. Here is the error: {error}")
                number_of_listings = 0

    if number_of_results > number_of_listings:
        number_of_results = number_of_listings
    while len(property_list) < number_of_results:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        property_list.extend(
            item for item in soup.select(selector="div.mb-srp__list") if list_of_ids.count(item.attrs['id']) == 0)
        list_of_titles.extend([item.select_one(selector="h2.mb-srp__card--title").text for item in property_list if
                               list_of_ids.count(item.attrs['id']) == 0])
        list_of_prices.extend(
            [item.select_one(selector="div.mb-srp__card__price--amount").text for item in property_list if
             item.select_one(selector="div.mb-srp__card__price--amount") is not None and list_of_ids.count(
                 item.attrs['id']) == 0])
        list_of_urls.extend([json.loads(item.select_one(selector="script").string)['url'] for item in property_list if
                             item.select_one(selector="script") is not None and list_of_ids.count(
                                 item.attrs['id']) == 0])
        list_of_ids.extend([item.attrs['id'] for item in property_list if
                            hasattr(item, 'id') and list_of_ids.count(item.attrs['id']) == 0])
        if list_of_ids:
            driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, list_of_ids[-1]))
        sleep(2)
    driver.quit()
except (ConnectionError, ConnectionRefusedError, KeyboardInterrupt, MaxRetryError, ProtocolError, NoSuchWindowException,
        InvalidSessionIdException):
    pass

form_url = "https://forms.gle/H1YFBJvfV17zfVUM6"

try:
    if property_list:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(form_url)
        for n in range(len(property_list)):
            for input_attempt in range(max_number_of_attempts):
                try:
                    input_boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
                    input_boxes[0].send_keys(list_of_titles[n])
                    input_boxes[1].send_keys(list_of_prices[n])
                    input_boxes[2].send_keys(list_of_urls[n])
                    break
                except (NoSuchElementException, ElementNotInteractableException):
                    sleep(sleep_time)
                    if input_attempt == max_number_of_attempts - 1:
                        print(f"Unable to submit the details of the porperty listed at {list_of_urls[n]} to the form.")
            for submit_attempt in range(max_number_of_attempts):
                try:
                    driver.find_element(By.CSS_SELECTOR, "div[role='button']").click()
                    break
                except (ElementClickInterceptedException, StaleElementReferenceException):
                    driver.execute_script("arguments[0].click();",
                                          driver.find_element(By.CSS_SELECTOR, "div[role='button']"))
                    break
                except NoSuchElementException as error:
                    sleep(sleep_time)
                    print(error)
            for return_to_form_attempt in range(max_number_of_attempts):
                try:
                    driver.find_element(By.LINK_TEXT, "Submit another response").click()
                    break
                except (StaleElementReferenceException, ElementClickInterceptedException):
                    driver.execute_script("arguments[0].click();",
                                          driver.find_element(By.LINK_TEXT, "Submit another response"))
                    break
                except NoSuchElementException:
                    sleep(sleep_time)
                    if return_to_form_attempt == max_number_of_attempts - 1:
                        print(f"Unable to submit the details of the property listed at {list_of_urls[n]} to the form.")

        sleep(30)
        driver.quit()
except (ConnectionError, ConnectionRefusedError, KeyboardInterrupt, MaxRetryError, ProtocolError, NoSuchWindowException,
        InvalidSessionIdException):
    pass