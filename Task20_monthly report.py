import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import requests
paths = r"C:\Users\MageSaran\OneDrive\Desktop\Saraniya_GUVI\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
from selenium.webdriver.common.action_chains import ActionChains
driver.get("https://labour.gov.in/")
time.sleep(3)
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")

# Use ActionChains to hover over the "Documents" menu
actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()
time.sleep(2)  # Wait for the dropdown menu to appear

# Click on "Monthly Progress Report"
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_url = monthly_report_link.get_attribute('href')
monthly_report_link.click()


# Download the monthly progress report
report_response = requests.get(monthly_report_url)
with open(r"C:\Users\MageSaran\OneDrive\Desktop\Saraniya_GUVI\Monthly_Progress_Report.pdf",'wb') as file:
     file.write(report_response.content)
print("Monthly Progress Report downloaded successfully.")
