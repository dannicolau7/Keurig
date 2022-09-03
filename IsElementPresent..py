import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.keurig.com/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//input[@id="couponsSignup"]').send_keys("dan.nicolau_ex@kdrp.com")
driver.find_element(By.XPATH, '//input[@id ="popup_signupbutton"]').click()
driver.find_element(By.XPATH, '//*[@id="_tealiumModalClose"]').click()
driver.find_element(By.XPATH, '(//div[@class ="subMenuContainer text-center  css-f1zt5s"])[1]').click()
driver.find_element(By.XPATH,
                                 '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[3]/div[1]/label/span').click()
driver.find_element(By.XPATH,
                                 '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[1]/input').send_keys(
            "dan.nicolau_ex@kdrp.com")
driver.find_element(By.XPATH, '//*[@id="L_Password"]').send_keys("D@nn2604")
driver.find_element(By.XPATH, '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/button').click()

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

types = driver.find_elements(By.TAG_NAME, ("a"))
total_types = (len(types))
print(len(types))
print("Test Completed")
