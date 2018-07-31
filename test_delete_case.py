# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_delete_case(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_delete_case(self):
        success = True
        wd = self.wd
        wd.get("https://staging-app.face2gene.com/")
        wd.find_element_by_xpath("//div[@class='s-c-form']/div/form/div/div[1]/div[1]/div/div/input").click()
        wd.find_element_by_xpath("//div[@class='s-c-form']/div/form/div/div[1]/div[1]/div/div/input").clear()
        wd.find_element_by_xpath("//div[@class='s-c-form']/div/form/div/div[1]/div[1]/div/div/input").send_keys("test.sheva9@gmail.com")
        wd.find_element_by_xpath("//div[@class='s-f-input']/div/div/input").click()
        wd.find_element_by_xpath("//div[@class='s-f-input']/div/div/input").clear()
        wd.find_element_by_xpath("//div[@class='s-f-input']/div/div/input").send_keys("qwer1234")
        wd.find_element_by_xpath("//div[@class='s-c-form']/div/div[2]/div").click()
        wd.find_element_by_link_text("10180374").click()
        wd.find_element_by_xpath("//div[@class='case-header']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/img").click()
        wd.find_element_by_xpath("//div[@class='stage']//div[.='Delete Case']").click()
        wd.find_element_by_xpath("//div[@class='action-btns']//div[.='Delete']").click()
        wd.find_element_by_xpath("//div[@id='user-options-dropdown']/div/div[1]/div/div[2]/div/img").click()
        wd.find_element_by_xpath("//div[@class='dd-items-wrap']//div[.='Sign Out']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
