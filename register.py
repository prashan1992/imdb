from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/anandpandey/Desktop/Prashant/chromedriver")
driver.maximize_window()
driver.get("https://www.imdb.com/")
driver.find_element_by_xpath("//div[contains(text(),'Sign in to IMDb')]").click()
driver.find_element_by_link_text("Create a New Account").click()
driver.find_element_by_name("customerName").send_keys("Testings")
driver.find_element_by_name("email").send_keys('use valid email id')
driver.find_element_by_id("ap_password").send_keys('use valid pwd')
driver.find_element_by_xpath("//input[@id='ap_password_check']").send_keys('re enter used password')
driver.find_element_by_class_name("a-button-input").click()
driver.quit()