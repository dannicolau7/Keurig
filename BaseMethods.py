

from selenium.webdriver.common.by import By

from PythonProject.HomePageTests import base_methods


class BaseMethods:
    

    def __init__(self):
        self.driver = None

    def log_in(self):
        self.driver.find_element(By.XPATH, '//input[@id="couponsSignup"]').send_keys("dan.nicolau_ex@kdrp.com")
        self.driver.find_element(By.XPATH, '//input[@id ="popup_signupbutton"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="_tealiumModalClose"]').click()
        self.driver.find_element(By.XPATH, '(//div[@class ="subMenuContainer text-center  css-f1zt5s"])[1]').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[3]/div[1]/label/span').click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/div[1]/input').send_keys(
            "dan.nicolau_ex@kdrp.com")
        self.driver.find_element(By.XPATH, '//*[@id="L_Password"]').send_keys("D@nn2604")
        self.driver.find_element(By.XPATH, '//*[@id="login-tabs-section-tabpane-logIn"]/section/form/button').click()

        print(BaseMethods)
