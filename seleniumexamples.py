from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#driver = webdriver.Firefox(executable_path="C:\\Users\\danicola\\Desktop\\danp\\geckodriver.exe")

#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

driver.get("https://www.keurig.com/")

driver.maximize_window()

title = driver.title

print(title)


