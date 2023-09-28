from selenium import webdriver
import time

url = "https://vk.com/"
browser = webdriver.Chrome()

try:
    browser.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()