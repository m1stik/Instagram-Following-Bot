from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

# enter your login data here
USERNAME = "YOUR LOGIN"
PASSWORD = "YOUR PASSWORD"
INSTA_LOGIN_PAGE = "https://www.instagram.com/accounts/login/"

target_account = input("Enter account to target: ").strip()
follow_mode = input("Grab their followers or following?: ")
amount_to_follow = int(input("How many to follow?: "))

class InstaFollower:

    # Initializing, opening the login page
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(INSTA_LOGIN_PAGE)

    def login(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[2]").click()
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(USERNAME)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(PASSWORD)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
        sleep(4)

    # mode 3 - following, 2 - followers
    def find_followers(self, mode, target):
        self.driver.get(f"https://www.instagram.com/{target}")
        self.driver.find_element_by_xpath(f"//*[@id='react-root']/section/main/div/header/section/ul/li[{mode}]").click()
        sleep(4)

    def follow(self, amount):
        follow_count = 0

        #While loop is for scrolling down, and updating the array with buttons
        while follow_count < amount:
            # Parsing all the buttons
            accounts = self.driver.find_elements_by_css_selector("li button div")

            for i in accounts:
                # If there is the follow button, click it
                if i.text == "Follow" and follow_count < amount:
                    i.click()
                    print("followed")
                    follow_count += 1
                    sleep(4)

                # If none of the buttons are "follow" in the array, then pass
                else:
                    pass

            # Quit if followed enought. If not, scroll down, wait, and repeat
            if follow_count >= amount: break
            self.driver.find_element_by_css_selector("li button").send_keys(Keys.END)
            sleep(4)

        print("Done!")
        self.driver.quit()

web_browser = InstaFollower()
web_browser.login()

if follow_mode == "followers":
    web_browser.find_followers(mode=2, target=target_account)
elif follow_mode == "following":
    web_browser.find_followers(mode=3, target=target_account)

web_browser.follow(amount=amount_to_follow)