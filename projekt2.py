# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.sukienkimm.pl/sukienki/na-wesele/")

    def test_exaple(self):
        driver = self.driver
        dresswedding = driver.find_element_by_css_selector(".pr_list_div")
        availabledress = dresswedding.find_elements_by_css_selector('.preview')
        pressbutton = availabledress[0].find_element_by_css_selector('a')
        pressbutton.click()
        sleep(3)
        buttonBar = driver.find_element_by_css_selector(".rozmiary_div")
        availableSizes = buttonBar.find_elements_by_css_selector(".atts_6")
        sizeLink = availableSizes[0].find_element_by_css_selector('a')
        sizeLink.click()

        sleep(5)

        selectedSize = driver.find_element_by_id("selectedSize")
        assert selectedSize.text == sizeLink.text

        





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
