import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from db_list import lista


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        window = self.driver

        try:
            window.get('http://www.intagram.com')
            time.sleep(5)
            set_username = window.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[1]/div/label/input')
            set_username.send_keys(self.username)

            set_pass = window.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[2]/div/label/input')
            set_pass.send_keys(self.password)

            time.sleep(2)

            button = window.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[3]/button/div')
            button.click()

            time.sleep(5)

        except:
            time.sleep(10)

    def go_to_page(self):
        x = 0
        for i in range(x, len(lista)):
            window = self.driver
            window.get('https://www.instagram.com/p/COQ6-_SDP2B/')

            get_dialog = window.find_element_by_class_name('_15y0l')
            get_dialog.click()

            time.sleep(2)

            send_comment = window.find_element_by_class_name('Ypffh')
            send_comment.send_keys(lista[i])

            file = open('savepost.txt', 'a')
            time.sleep(2)
            file.write(str(i) + '\n->' + lista[i])
            file.close()

            time.sleep(2)
            try:
                on_click_submit = window.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]'
                )
                on_click_submit.click()

                time.sleep(5)

            except:
                time.sleep(60)


start = InstagramBot('@tiago.alvesmoc', 'Sky10612')
start.login()
start.go_to_page()
