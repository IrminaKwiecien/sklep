# -*- coding: utf-8 -*-
import unittest
from time import sleep
from selenium import webdriver

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.sukienkimm.pl/sukienki/na-wesele/")
