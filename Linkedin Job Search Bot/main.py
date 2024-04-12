import urllib3.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from bs4 import BeautifulSoup
from time import sleep
import lxml
#
# Set the Number of results required. To keep the time taken for execution low, I would recommend less than 30.
number_of_results = 25
url = "https://www.linkedin.com/login"

max_number_of_attempts = 20
sleep_time = 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

email_address = "meerakaluvar@gmail.com"
password = "Ad@11042005"

try:
    for attempt in range(max_number_of_attempts):
        try:
            driver.find_element(By.LINK_TEXT, "Sign in").click()
            break
        except (ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException) as error:
            sleep(sleep_time)
            if attempt == max_number_of_attempts - 1:
                print("Sorry. Unable to sign in. Here is the error:", error)
        except (KeyboardInterrupt, NoSuchWindowException, InvalidSessionIdException, ConnectionError, ConnectionRefusedError):
            break

    for attempt in range(max_number_of_attempts):
        try:
            driver.find_element(By.ID, "username").send_keys(email_address)
            driver.find_element(By.ID, "password").send_keys(password)
            try:
                driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign in']").click()
            except (ElementClickInterceptedException, StaleElementReferenceException):
                driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign in']"))
            break
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException) as error:
            sleep(sleep_time)
            if attempt == max_number_of_attempts - 1:
                print("Unable to log in. Here is the error:", error)
        except (KeyboardInterrupt, NoSuchWindowException, InvalidSessionIdException, ConnectionError, ConnectionRefusedError):
            break

    # for attempt in range(max_number_of_attempts):
    #     try:
    #         try:
    #             driver.find_element(By.CSS_SELECTOR, "button.search-global-typeahead__collapsed-search-button").click()
    #         except (StaleElementReferenceException, ElementClickInterceptedException):
    #             driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "button.search-global-typeahead__collapsed-search-button"))
    #         for search_attempt in range(max_number_of_attempts):
    #             try:
    #                 search_bar = driver.find_element(By.CSS_SELECTOR, "input.search-global-typeahead__input")
    #                 search_bar.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    #                 search_bar.send_keys("Python Developer")
    #                 search_bar.send_keys(Keys.ENTER)
    #                 break
    #             except (NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException) as error:
    #                 sleep(sleep_time)
    #                 if search_attempt == max_number_of_attempts - 1:
    #                     print("Unable to search for jobs. Here is the error:", error)
    #         break
    #     except (NoSuchElementException, ElementNotInteractableException) as error:
    #         sleep(sleep_time)
    #         print("Unable to search for jobs. Here is the error:", error)

    for attempt in range(max_number_of_attempts):
        try:
            driver.find_element(By.CSS_SELECTOR, "li-icon[type='chevron-down'] svg").click()
            break
        except (ElementClickInterceptedException, ElementNotInteractableException):
            driver.execute_script("arguments[0].click();", driver.find_elements(By.CSS_SELECTOR, "button.msg-overlay-bubble-header__control.msg-overlay-bubble-header__control--new-convo-btn.artdeco-button--circle.ember-view")[1])
            break
        except NoSuchElementException as error:
            sleep(sleep_time)
            print(error)

    # for attempt in range(max_number_of_attempts):
    #     try:
    #         driver.find_element(By.CSS_SELECTOR, "ul.search-reusables__filter-list li button").click()
    #         break
    #     except (ElementClickInterceptedException, ElementNotInteractableException):
    #         driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "ul.search-reusables__filter-list li button"))
    #     except NoSuchElementException:

    for attempt in range(max_number_of_attempts):
        try:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            number_of_listings = int(soup.select_one(selector="div.jobs-search-results-list__subtitle span").text.split()[0].replace(",", ""))
            if number_of_listings < number_of_results:
                number_of_results = number_of_listings
            break
        except (AttributeError, NoSuchElementException) as error:
            sleep(sleep_time)
            if attempt == max_number_of_attempts - 1:
                print("Unable to find the number of listings. Here is the error:", error)
    job_ids = []
    page_number = 1

    while len(job_ids) < number_of_results:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        listed_jobs = [job for job in soup.select(selector="div[data-view-name='job-card']") if job.attrs["data-job-id"] not in job_ids]
        job_ids.extend([item.attrs["data-job-id"] for item in listed_jobs if item.attrs["data-job-id"] not in job_ids])
        print(len(job_ids), job_ids)
        for job in listed_jobs:
            data_job_id = job.attrs["data-job-id"]
            for attempt in range(max_number_of_attempts):
                try:
                    try:
                        driver.find_element(By.CSS_SELECTOR, f"div[data-job-id='{data_job_id}']").click()
                    except (StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException):
                        driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, f"div[data-job-id='{data_job_id}']"))
                    save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button")
                    if save_button.find_element(By.CSS_SELECTOR, "span").text == "Save":
                        try:
                            save_button.click()
                        except (StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException):
                            driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button"))
                    try:
                        follow_button = driver.find_element(By.CSS_SELECTOR, "button.follow.artdeco-button.artdeco-button--secondary")
                        driver.execute_script("arguments[0].scrollIntoView();", follow_button)
                        if follow_button.find_element(By.CSS_SELECTOR, "span").text == "Follow":
                            try:
                                follow_button.click()
                            except (StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException):
                                driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, "button.follow.artdeco-button.artdeco-button--secondary"))
                    except NoSuchElementException:
                        pass
                    break
                except (NoSuchElementException) as error:
                    sleep(sleep_time)
                    if attempt == max_number_of_attempts - 1:
                        print(error)
                except (NoSuchWindowException, InvalidSessionIdException, KeyboardInterrupt, ConnectionError, ConnectionRefusedError):
                    break
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CSS_SELECTOR, f"div[data-job-id='{job_ids[-1]}']"))
        sleep(sleep_time)
        if not listed_jobs:
                page_number += 1
                try:
                    driver.find_element(By.CSS_SELECTOR, f"button[aria-label='Page {page_number}']").click()
                except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
                    driver.execute_script("arguments[0].click();",driver.find_element(By.CSS_SELECTOR, f"button[aria-label='Page {page_number}']"))

    sleep(30)
    driver.quit()
except (KeyboardInterrupt, ConnectionError, ConnectionRefusedError, NoSuchWindowException, InvalidSessionIdException, urllib3.exceptions.MaxRetryError, urllib3.exceptions.ConnectTimeoutError, urllib3.exceptions.ProtocolError):
    pass