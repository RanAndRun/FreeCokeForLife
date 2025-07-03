from selenium import webdriver
from time import sleep
import threading




def send_request(phone_number):
    path = 'D:\Ran\Programing\FreeColaForLife\chromeDriver\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)

    url = "https://cocacola.co.il/refund/app/0.5/"

    driver.get(url)
    sleep(5)
    user = driver.find_element_by_xpath("//input[@type='text' and @name='phone_number']")
    user.send_keys(phone_number)

    clicker = driver.find_element_by_xpath("//div[@class='btn' and contains(text(),'שליחה ואימות')]")
    clicker.click()


with open("fixed_phone_numbers.txt", 'r') as file:
    numbers = file.readlines()

# Create threads for each phone number
threads = []
for number in numbers:
    # Remove newline characters and create a thread for each number
    thread = threading.Thread(target=send_request, args=(number.strip(),))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()
    sleep(2)

# Wait for all threads to finish
for thread in threads:
    thread.join()
