# -*- coding: utf-8 -*-

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


valid_name = "Anna"
valid_surname = "Nowak"
valid_street = "Prosta"
valid_number = "4"
valid_code = "42-789"
valid_city = "Cracov"
valid_email = "anna.nowak@gmail.com"
valid_password = "asdfzxcv"
valid_password2 = "asdfqwer"

class test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.sukienkimm.pl")

    def test_exaple(self):
        driver = self.driver
        login_shop=driver.find_element_by_class_name("loginIco")
        login_shop.click()
        cookies_info = driver.find_element_by_id("close-cookie-info")
        cookies_info.click()
        sleep(1)
        regestration_shop = driver.find_element_by_class_name('xlarge')
        regestration_shop.click()
        name_user = driver.find_element_by_id('usr_first_name')
        name_user.send_keys(valid_name)
        surname_user = driver.find_element_by_id("usr_last_name")
        surname_user.send_keys(valid_surname)
        street_user = driver.find_element_by_id("usr_address")
        street_user.send_keys(valid_street)
        number_user = driver.find_element_by_id("usr_address_str_no")
        number_user.send_keys(valid_number)
        code_user = driver.find_element_by_id("usr_post_code")
        code_user.send_keys(valid_code)
        city_user = driver.find_element_by_id("usr_city")
        city_user.send_keys(valid_city)
        email_user = driver.find_element_by_id("usr_email")
        email_user.send_keys(valid_email)
        password_user = driver.find_element_by_id("usr_password")
        password_user.send_keys(valid_password)
        password2_user = driver.find_element_by_id("usr_password_confirm")
        password2_user.send_keys(valid_password2)
        agree_user = driver.find_element_by_xpath('//*[@id="usr_terms_agree"]')
        agree_user.click()
        checkbox_user = driver.find_element_by_xpath('//*[@id="usr_data_manage"]')
        checkbox_user.click()
        registration_user = driver.find_element_by_id("newUser_submit_button")
        registration_user.click()
        WebDriverWait(driver, 3).until(EC.alert_is_present(), '')
        alert = driver.switch_to.alert
        assert alert.text == u'Potwierdzenie hasła musi być takie same jak hasło !'
        alert.accept()
        print("alert accepted")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
