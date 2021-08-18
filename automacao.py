from selenium import webdriver

import pyperclip
import time


def start_browser(browser):

    time.sleep(4)

    browser.find_element_by_xpath('//*[@id="click-to-copy"]').click()
    time.sleep(2)

    t = pyperclip.paste()
    file = open('email.txt', 'a')
    time.sleep(1)
    file.write(str(t) + '\n')
    file.close()
    pyperclip.copy('')
    print(t)

    browser.find_element_by_xpath('//*[@id="click-to-delete"]').click()
    time.sleep(2)
    browser.refresh()

    # browser.quit()


browser = webdriver.Chrome()
browser.get('https://temp-mail.org/pt/')
while True:
    start_browser(browser)
