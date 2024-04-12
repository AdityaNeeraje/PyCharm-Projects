from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import lxml
from time import sleep
from os import environ

url = "https://portal.iitb.ac.in/asc/Login"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

max_number_of_attempts = 20
sleep_time = 5

for attempt in range(max_number_of_attempts):
    try:
        user_id = driver.find_element(By.ID, "login_user")
        user_id.send_keys(environ.get("USERNAME"))
        user_id.send_keys(Keys.ENTER)
        password = driver.find_element(By.ID, "login_password")
        password.send_keys(environ.get("PASSWORD"))
        password.send_keys(Keys.ENTER)
        break
    except NoSuchElementException as error:
        sleep(sleep_time)
        if attempt == max_number_of_attempts - 1:
            print(f"Sorry. Unable to fill the login and password details. Here is the error:\n{error}")
    except (ElementClickInterceptedException, StaleElementReferenceException):
        driver.execute_script("arguments[0].value=arguments[1]", driver.find_element(By.ID, "login_user"), environ.get("USERNAME"))
        driver.execute_script("arguments[0].value=arguments[1]", driver.find_element(By.ID, "login_password"), environ.get("PASSWORD"))
        break
sleep(sleep_time)
# soup = BeautifulSoup(driver.page_source, 'lxml')
# print(soup.prettify())
# for attempt in range(max_number_of_attempts):
#     try:
#         captcha_box = driver.find_element(By.ID, "g-recaptcha-response")
#         captcha_box.click()
#         break
#     except NoSuchElementException as error:
#         sleep(sleep_time)
#         if attempt == max_number_of_attempts - 1:
#             print(f"Sorry. Unable to click the captcha. Here is the error:\n{error}")
#     except (ElementClickInterceptedException, StaleElementReferenceException):
#         driver.execute_script("arguments[0].click()", driver.find_element(By.ID, "g-recaptcha-response"))
#         break
sleep(sleep_time)
for attempt in range(max_number_of_attempts):
    try:
        login = driver.find_element(By.ID, "l").find_element(By.CSS_SELECTOR, "button")
        login.click()
        break
    except NoSuchElementException as error:
        sleep(sleep_time)
        if attempt == max_number_of_attempts - 1:
            print(f"Sorry. Unable to click the captcha. Here is the error:\n{error}")
    except (ElementClickInterceptedException, StaleElementReferenceException):
        driver.execute_script("arguments[0].click()", driver.find_element(By.ID, "l").find_element(By.CSS_SELECTOR, "button"))
        break
sleep(sleep_time)
for attempt in range(max_number_of_attempts):
    try:
        driver.find_element(By.LINK_TEXT, "Performance Summary").click()
        break
    except NoSuchElementException as error:
        sleep(sleep_time)
        if attempt == max_number_of_attempts - 1:
            print(f"Sorry. Unable to go to performance summary. Here is the error {error}")
    except (ElementClickInterceptedException, StaleElementReferenceException):
        driver.execute_script("arguments[0].click()", driver.find_element(By.LINK_TEXT, "Performance Summary"))
        break
sleep(sleep_time)
course_names = []
course_grades = []
for attempt in range(max_number_of_attempts):
    try:
        rows = driver.find_elements(By.CSS_SELECTOR, "tr")
        for index in range(len(rows)):
            try:
                word = rows[index].find_element(By.CSS_SELECTOR, "td").text
            except NoSuchElementException:
                word = rows[index].find_element(By.CSS_SELECTOR, "th").text
            if word == "Course Code":
                rows = rows[index+1:]
                break
        for row in rows:
            try:
                data = row.find_elements(By.CSS_SELECTOR, "td")
                course_names.append(data[1].text)
                course_grades.append(data[4].text)
                # print(f"Course Name: {data[1].text}\t\tGrade: {data[4].text}")
            except (IndexError, NoSuchElementException):
                break
        break
    except NoSuchElementException as error:
        sleep(sleep_time)
        if attempt == max_number_of_attempts - 1:
            print(f"Sorry. Unable to go to performance summary. Here is the error {error}")

from tkinter import Tk
root = Tk()
root.title("Grades")
root.mainloop()