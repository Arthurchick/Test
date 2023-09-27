from selenium import webdriver
import time

url = "https://vk.com/"
browser = webdriver.Chrome(executable_path="C:\\Users\\vika_\\PycharmProjects\\pythonProject\\selenium\\chromedriver\\chromedriver.exe")

try:
    browser.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()