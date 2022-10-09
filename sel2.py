
import sys
sys.exit(0)

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Python_code\\chromedriver_path\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
driver.find_element_by_name("enter-name").send_keys("ABC")
driver.find_element_by_id("alertbtn").click()
time.sleep(3)

# driver.find_element_by_link_text("Free Access to InterviewQues/ResumeAssistance/Material").click()

# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
