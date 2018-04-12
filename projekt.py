import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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
        self.driver.get("http://www.sukienkimm.pl/sukienki/mini/sliczna-zwiewna-elegancka-sukienka-model-pw-3021-25113.html")




    def test_exaple(self):
        driver = self.driver
        buttonBar = driver.find_element_by_css_selector(".rozmiary_div")
        availableSizes = buttonBar.find_elements_by_css_selector(".atts_6")
        sizeButton = availableSizes[0].find_element_by_css_selector('a')
        sizeButton.click()

        selectedSize = driver.find_element_by_id("selectedSize")
        assert selectedSize.text == "34(XS)"

        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
