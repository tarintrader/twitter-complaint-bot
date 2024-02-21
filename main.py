import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "@gmail.com"
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:

    def __init__(self):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(60)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get(
            "https://www.google.com/search?q=test+de+velocidad&sca_esv=582900893&bih=923&biw=2560&hl=es&sxsrf=AM9HkKm3ex6BTSA8gHGVe-zaKCv28q6Mgw%3A1700114953118&source=hp&ei=CbJVZeWcBae-hbIPsaSmuAU&iflsig=AO6bgOgAAAAAZVXAGTXrwLbzEQHBcB7BklOqXwtUgoyZ&oq=te&gs_lp=Egdnd3Mtd2l6IgJ0ZSoCCAAyBxAjGIoFGCcyBBAjGCcyBBAjGCcyBxAAGIoFGEMyBxAAGIoFGEMyBxAAGIoFGEMyCxAuGIAEGMcBGNEDMgUQLhiABDIFEAAYgAQyCxAuGIAEGMcBGNEDSKoSUABYDXAAeACQAQCYAWygAcABqgEDMS4xuAEDyAEA-AEB&sclient=gws-wiz")
        try:
            self.accept_cookies = self.driver.find_element(By.XPATH,
                                                           '/html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div')
        except NoSuchElementException:
            print("NoSuchElementException")

        self.accept_cookies.click()
        self.test_button = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/g-raised-button/div')
        self.test_button.click()
        time.sleep(60)

        self.down_html = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/g-lightbox/div/div[2]/div/span/div/div/div[2]/div[2]/div[1]/div[1]/p[1]')
        self.down = self.down_html.text

        self.up_html = self.driver.find_element(By.XPATH,
                                                '/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/g-lightbox/div/div[2]/div/span/div/div/div[2]/div[2]/div[1]/div[2]/p[1]')
        self.up = self.up_html.text
        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        self.accept_cookies = self.driver.find_element(By.XPATH,
                                                       '/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span/span')
        self.accept_cookies.click()

        time.sleep(3)
        self.login_button = self.driver.find_element(By.XPATH,
                                                     '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        self.login_button.click()

        time.sleep(3)
        self.email = self.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.send_keys("@gmail.com")
        self.next = self.driver.find_element(By.XPATH,
                                             '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        self.next.click()

        time.sleep(3)
        self.password = self.driver.find_element(By.XPATH,
                                                 '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.send_keys("")
        self.login_button = self.driver.find_element(By.XPATH,
                                                     '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        self.login_button.click()

        time.sleep(3)

        def send_tweet():
            try:
                self.text_post = self.driver.find_element(By.XPATH,
                                                          '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
                self.text_post.send_keys(
                    f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")
                time.sleep(3)
                self.post_button = self.driver.find_element(By.XPATH,
                                                            '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
                self.post_button.click()
            except ElementClickInterceptedException:
                self.body_html = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main')
                self.body_html.click()
                send_tweet()

        send_tweet()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
