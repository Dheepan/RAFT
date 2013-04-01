import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import conf
import unittest
import os
import subprocess

class HashCubeAutomation(object):
    # singleton object holder
    __single = None
    # driver object holder
    __driver=""

    # function and logic for instantiating a singleton object
    def __new__(classtype, *args, **kwargs):
        if classtype != type(classtype.__single):
          classtype.__single = object.__new__(classtype, *args, **kwargs)
          classtype.__single.__driver=classtype.__single.oneTimeLogin()
        return classtype.__single

    # constructor fucntion called after __new__
    def __init__(self,msg):
        self.driver=self.__driver
        print msg

    # function that is invoked onetime while instantiating the singleton
    def oneTimeLogin(self):
        time.sleep(1)
        driver = webdriver.Firefox()
        driver.get("http://www.facebook.com")
        elem = driver.find_element_by_id("email")
        elem.send_keys(conf.email)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(conf.password)
        elem.send_keys(Keys.RETURN)
        driver.get(conf.appurl)
        driver.switch_to_frame("iframe_canvas")
        driver.execute_script("$('.popup').dialog('close')")
        return driver

    # funtion that does the cleanup
    def cleanUp(self):
        driver=self.__driver
        print "Closing the browser"
        driver.close()
    # function for taking screenshots 
    def screenshot(self,s):
        driver=self.driver
        path=os.path.dirname(__file__)
        path+="/screenshots/"+s
        driver.get_screenshot_as_file(path)

    def click(self,s):
        driver=self.driver
        c=s[0]
        #if id
        if c=="#":
            ele=driver.find_element_by_id(s[1:]).click()
        # if class
        if c==".":
            ele=driver.find_element_by_class_name(s[1:]).click()
        # if xpath
        if c=="/":
            ele=driver.find_element_by_id(s).click()
        # if name
        if c=="@":
            ele=driver.find_element_by_id(s[1:]).click()
        #if text
        if c=="*":
            ele=driver.find_element_by_id(s[1:]).click()

    def is_displayed(self,s):
        driver=self.driver
        c=s[0]
        #if id
        if c=="#":
            ele=driver.find_element_by_id(s[1:]).is_displayed()
        # if class
        if c==".":
            ele=driver.find_element_by_class_name(s[1:]).is_displayed()
        # if xpath
        if c=="/":
            ele=driver.find_element_by_id(s).is_displayed()
        # if name
        if c=="@":
            ele=driver.find_element_by_id(s[1:]).is_displayed()
        #if text
        if c=="*":
            ele=driver.find_element_by_id(s[1:]).is_displayed()
        return ele

    def execute_script(self,s):
        driver=self.driver
        result=driver.execute_script(s)
        return result
        
    def switch_frame(self,s):
        driver=self.driver
        driver.switch_to_frame(s)

    def get(self,s):
        driver.get(s)
        





