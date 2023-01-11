from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Hosttest(LiveServerTestCase):

    #example test case 1 to check if the webpage title is "Risk database mockup"
    # def testhomepage(self):
    #     driver = webdriver.Chrome()
    #     driver.get('http://127.0.0.1:8000/homepage/')
    #     time.sleep(5)
    #     assert "Risk Database mockup" in driver.title

    #test case 2 if login with correct username and password a homepage with "risk scenario database" heading
    def testlogin(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/homepage/login/')
        time.sleep(3)

        user_name = driver.find_element('name','username')
        pass_word = driver.find_element('name','password')
        time.sleep(3)

        login = driver.find_element(By.CLASS_NAME,'btn')

        user_name.send_keys('admin')
        pass_word.send_keys('admin')
        time.sleep(3)

        login.send_keys(Keys.RETURN)

        assert "Risk Scenario Database" in driver.page_source
