
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
paths = r"C:\Users\MageSaran\OneDrive\Desktop\Saraniya_GUVI\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# time.sleep(2)
driver.get("https://www.cowin.gov.in/")
print("Title of webpage:",driver.title)
print("HomePage:",driver.current_url)
driver.maximize_window()

ACCESS_FAQ=driver.find_element(By.LINK_TEXT,"FAQ")
time.sleep(4)
ACCESS_FAQ.click()
driver.switch_to.window(driver.window_handles[1])
print("First window:",driver.current_url)


ACCESS_PARTNER=driver.find_element(By.LINK_TEXT,"PARTNERS")
time.sleep(4)
ACCESS_PARTNER.click()
driver.switch_to.window(driver.window_handles[2])
print("Second window:",driver.current_url)

driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.close()
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.close()
time.sleep(5)

