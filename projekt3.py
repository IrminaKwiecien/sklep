# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver

invalid_discount = "A2A2A2A2"

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
        sleep(3)
        selectedSize = driver.find_element_by_id("selectedSize")
        assert selectedSize.text == sizeLink.text
        cookies_info = driver.find_element_by_id("close-cookie-info")
        cookies_info.click()
        sleep(1)
        addToBasket = driver.find_element_by_id("add2BasketBtn")
        driver.execute_script("window.scrollTo(0, 30)")
        addToBasket.click()
        sleep(1)
        discount =driver.find_element_by_xpath('//*[@id="pcode"]')
        driver.execute_script("window.scrollTo(0, 300)")
        discount.click()
        discount.send_keys(invalid_discount)
        sleep(1)
        activateBar = driver.find_element_by_css_selector(".kupon")
        activateBar2 = activateBar.find_element_by_css_selector(".button")
        activateBar2.click()
        sleep(5)
        modalcontent = driver.find_element_by_css_selector(".nyroModalIframe")
        frames = modalcontent.find_elements_by_css_selector("iframe")
        assert len(frames) == 1
        frame = frames[0]
        driver.switch_to.frame(frame)
        error = driver.find_element_by_css_selector("h1")
        assert error.text == u"BŁĄD: KOD NIEPOPRAWNY"
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()