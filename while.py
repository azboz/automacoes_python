from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from db_list import lista


class InstagramBot:
    def __init__(self, username, password,influencer):
        self.username = username
        self.password = password
        # self.coments1 = coments1
        self.influencer = influencer
        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe"
        )  # Coloque o caminho para o seu geckodriver aqui

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        x = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        x.send_keys(self.username)
        x.clear()
        time.sleep(5)

        x = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        x.send_keys(self.password)
        x.clear()
        time.sleep(5)

        x = driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)
        
    def buscar_seguidores(self, number_of_followers):
         bot = self.driver
         bot.get('https://instagram.com/' + self.influencer)
         time.sleep(5)
         
         bot.find_element_by_xpath('//a[@href="/'+ self.influencer + '/follower/"]').click()
         
         time.sleep(4)
         
         popup = bot.find_element_by_class_name('isgrP')
         
         

         followers_array=[] 
        
         i = 1
         while len(followera_array) <= number_of_follower:
            bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)       
            time.sleep(4) 
            
            followers = bot.find_elements_by_class_name('FPmnX')
            
            for follower in followers:
                if follower not in followers_array:
                    followers_array.append(follower.text)
                       
	 

    def gotopage(self):
        driver = self.driver
        # Colocar aqui a pagina do sorteio
        driver.get('https://www.instagram.com/' + self.username)

        for i in range(16, len(lista)):
            x = driver.find_element_by_class_name('_15y0l')
            x.click()
            time.sleep(5 + i)
            driver.find_element_by_class_name('Ypffh').send_keys(lista[i])
            file = open('savepost.txt', 'a')
            time.sleep(2)
            file.write(str(i) + '\n->' + lista[i])
            file.close()
            time.sleep(0.5 + 1 / 0.3)

            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]'
            ).click()
            time.sleep(2 + i + 0.3)

    def curtir_fotos_com_a_hastag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(
                1, 3
        ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        testes = [
            href for href in pic_hrefs if hashtag in href
            and href.index("https://www.instagram.com/p") != -1
        ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("pulando link inválido")
                continue
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath(
                    '//button[@class="dCJp8 afkep"]').click()
                time.sleep(random.randint(19, 23))
            except Exception as e:
                print(e)
                time.sleep(5)

    def follow_open_modal(self):
        driver = self.driver
        driver.get('https://www.instagram.com/danielbergofficial/')
        time.sleep(3)

        open_modal_follow = driver.find_element_by_xpath(
            '//a[@href="/danielbergofficial/following/"]')
        open_modal_follow.click()

    def modal_follow_curtir(self):
        driver = self.driver
        for i in range(1, 3):

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")


tiago = InstagramBot('tiago_yun', 'Sky10612','tiago_yun')
tiago.login()
time.sleep(2)
# tiago.gotopage()
# tiago.follow_open_modal()
time.sleep(2)
tiago.buscar_seguidores(5)
# tiago.modal_follow_curtir()
