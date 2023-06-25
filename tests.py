from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Hosttest(LiveServerTestCase):

    def testindex(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        time.sleep(5)
        assert "Sklep" in driver.title


class LoginFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/login/')
        time.sleep(3)
        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME, 'password')
        submit = driver.find_element(By.ID, 'submit')

        user_name.send_keys('admin1')
        user_password.send_keys('admin')
        time.sleep(3)
        submit.send_keys(Keys.RETURN)

        #assert 'admin' in driver.page_source

class RegisterFormTest(LiveServerTestCase):

    def testregisterform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/register/')
        time.sleep(3)
        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME, 'password1')
        user_password1 = driver.find_element(By.NAME, 'password2')
        user_email = driver.find_element(By.NAME, 'email')
        submit = driver.find_element(By.ID, 'submit')

        user_name.send_keys('testselenium')
        user_password.send_keys('qwerty12345')
        user_password1.send_keys('qwerty12345')
        user_email.send_keys('testselenium@onet.pl')
        time.sleep(3)
        submit.send_keys(Keys.RETURN)

class Regulamintest(LiveServerTestCase):

    def testregulamin(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/regulamin/')
        time.sleep(3)
        assert "Regulamin sklepu" in driver.title

class Productstest(LiveServerTestCase):

    def testproducts(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/products/')
        time.sleep(3)
        assert "Produkty" in driver.title

class Pomoctest(LiveServerTestCase):

    def testpomoc(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/pomoc/')
        time.sleep(3)
        assert "Pomoc" in driver.title

class Gametest(LiveServerTestCase):

    def testgame(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/game/the-witcher-3-wild-hunt/')
        time.sleep(3)
        assert "Gry" in driver.title