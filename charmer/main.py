from selenium import webdriver
from time import sleep
import threading
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send_request(phone_number):
    path = 'D:\Ran\Programing\FreeColaForLife\chromeDriver\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    url = "https://cocacola.co.il/refund/app/0.5/"
    driver.get(url)

    try:
        input_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @name='phone_number']")))
        input_field.send_keys(phone_number)

        input_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//section[@class="page active" and @data-name="page_1.5"]')))

        print(f"{phone_number} is not valid")

    except NoSuchElementException or TimeoutException:
        with open("valid_phone_numbers.txt", "a") as file:
            file.write(phone_number + "\n")
        print(f"might be valid: {phone_number}")

    finally:
        driver.close()

with open("fixed_phone_numbers.txt", 'r') as file:
    numbers = file.readlines()

threads = []
for number in numbers:
    thread = threading.Thread(target=send_request, args=(number.strip(),))
    threads.append(thread)



# Start all threads
for thread in threads:
    thread.start()
    sleep(7)

for thread in threads:
    thread.join()
