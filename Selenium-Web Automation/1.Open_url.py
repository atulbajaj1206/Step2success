#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
# Selenium is used for Gui testing as well as we can use it for web scrapping and web automation to fill up forms in complex sites and tools.
#pip install selenium        

#improting selenium driver(always copy paste all this function to minimse hassle)


from selenium import webdriver

#importing chrome driver shuold be in same folder 

chrome_options = webdriver.ChromeOptions()

#path where driver is stored

driver=webdriver.Chrome(executable_path=r"chromedriver.exe")

#url which nned to be open

driver.get("http://step2success.in/")