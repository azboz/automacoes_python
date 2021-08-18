from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

from colorama import init
from colorama import Fore

init()


def temp_mail(browser):

    original_id = browser.current_window_handle
    browser.get('https://temp-mail.org/pt/')
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="click-to-copy"]').click()
    time.sleep(2)

    email_copy_to_save = pyperclip.paste()
    file = open('email_egarwork.txt', 'a')
    time.sleep(1)
    file.write(str(email_copy_to_save) + '\n')
    file.close()
    pyperclip.copy('')
    print(Fore.GREEN + email_copy_to_save + ' copiado com sucesso')
    print(Fore.WHITE)
    time.sleep(4)
   
    sign_up_egawork(browser, email_copy_to_save, original_id)


def sign_up_egawork(browser, email, id):

    browser.get('https://egawork.com/')
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="navigation"]/li[2]/a').click()
    time.sleep(2)

    ##Imput Username
    username = browser.find_element_by_xpath('//*[@id="data"]/div[2]/input')
    time.sleep(2)
    username.send_keys(email[0] + email[1] + email[2] + email[3] + email[4])
    time.sleep(1)

    ##Input Email

    login = browser.find_element_by_xpath('//*[@id="data"]/div[3]/input')
    login.send_keys(email)
    time.sleep(1)

    password = browser.find_element_by_xpath('//*[@id="data"]/div[4]/input')
    password.send_keys('Sky10611')
    time.sleep(1)

    ##Btn Signup

    browser.find_element_by_xpath('//*[@id="data"]/div[6]/button').click()

    ##Goto Ads videos
    time.sleep(4)

    goto_videos(browser)


def goto_videos(browser):
    # print(Fore.BLUE, browser.current_window_handle)
    # browser.get('https://egawork.com/videos')
    # main_window = 'https://egawork.com/videos'
    # browser.find_element_by_xpath('//*[@id="v-pills-tab1-tab"]').click()
    # time.sleep(5)

    # print(Fore.BLUE, browser.current_window_handle)

    original_window = browser.current_window_handle
    assert len(browser.window_handles) == 1

    browser.get('https://egawork.com/videos')
    wait = WebDriverWait(browser, 10)
    browser.find_element_by_xpath('//*[@id="v-pills-tab1-tab"]').click()
    wait.until(EC.number_of_windows_to_be(2))
    time.sleep(5)

    if browser.window_handle != original_window:
        browser.switch_to.window(original_window)


browser = webdriver.Chrome()

temp_mail(browser)
