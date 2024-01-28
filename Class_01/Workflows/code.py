from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# open_browser
srvc = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=srvc)

driver.get("https://www.python.org/")
driver.maximize_window()
driver.get('https://www.facebook.com')
driver.minimize_window()
driver.get('https://www.youtube.com')
driver.maximize_window()
driver.get('https://www.google.com')

time.sleep(5)  # import time
driver.quit()
