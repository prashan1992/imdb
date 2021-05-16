import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


def test_register():
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


def test_login():
    driver = webdriver.Chrome(executable_path="/Users/anandpandey/Desktop/Prashant/chromedriver")
    driver.maximize_window()
    driver.get("https://www.imdb.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//div[contains(text(),'Sign in to IMDb')]").click()
    driver.find_element_by_class_name("auth-provider-text").click()
    driver.find_element_by_id("ap_email").send_keys('use registered email')
    driver.find_element_by_name("password").send_keys('use registered pwd')
    driver.find_element_by_class_name("a-button-input").click()
    driver.find_element_by_id("imdbHeader-navDrawerOpen--desktop").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[2]/nav[1]/div[2]/aside[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/ul[1]/a[3]").click()
    Select(driver.find_element_by_css_selector("#lister-sort-by-options")).select_by_visible_text("Release Date")
    driver.find_element_by_link_text("The Kid").click()
    release_date = driver.find_element_by_partial_link_text("March 1921 (U").text
    print(release_date)