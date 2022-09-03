

from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from self import self
from webdriver_manager.chrome import ChromeDriverManager

from PythonProject.BaseMethods import BaseMethods
from PythonProject.seleniumexamples import driver
base_methods: BaseMethods = BaseMethods()
driverChrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def set_up():
    driverChrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.keurig.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)


class BaseMethods:

    base_methods.log_in()

    driver.find_element(By.XPATH, '//a[@title=" Keurig® Starter Kit"]/div[@class="oz-hide-in-mobile"]').click()

    driver.find_element(By.XPATH, '//div[@data-at-id="dealsComponent"]').click()

    driver.find_element(By.XPATH,
                        '//a[@href="/content/auto-delivery?open=ad&cm_sp=25off-_-deals+page-_-subscribe"]').click()

    driver.find_element(By.XPATH, '//div[@class="s7innercontrolbarcontainer"]').click()

    driver.find_element(By.XPATH, '//div[@id="s7_videoview_advideo_mutableVolume"]').click()
    driver.find_element(By.XPATH, '//div[@class="yCmsComponent keurig-logo logo-desktop-only"]').click()

    driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys("pods")

    driver.find_element(By.XPATH,
                        '//*[@class="search-container input-container css-1hp7dkc"]/div[@class="input-group"]').click()

    driver.find_element(By.XPATH,
                        '//div[@class="css-vy5380 col"]/a[@href="/search?text=pod|search_suggestion"]').click()

    driver.find_element(By.XPATH, '//input[@placeholder="Your email"]').send_keys("dan.nicolau_ex@kdrp.com")

    driver.find_element(By.XPATH, '//*[@class="btn-submit css-nnbjkw"]').click()
    print("Test Completed")
