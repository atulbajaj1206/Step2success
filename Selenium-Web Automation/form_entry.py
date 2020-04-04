#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
# Selenium is used for Gui testing as well as we can use it for web scrapping and web automation to fill up forms in complex sites and tools.
#pip install selenium        

#improting selenium driver(always copy paste all this function to minimse hassle)


from selenium import webdriver
import time

#importing chrome driver shuold be in same folder 

chrome_options = webdriver.ChromeOptions()

#path where driver is stored

driver=webdriver.Chrome(executable_path=r"chromedriver.exe")

#url which nned to be open

driver.get("https://step2success.in/selenium-form/")
time.sleep(5)
f_name=driver.find_element_by_id("first_name")
f_name.send_keys("Ankit")

l_name=driver.find_element_by_id("last_name")
l_name.send_keys("Kothari")