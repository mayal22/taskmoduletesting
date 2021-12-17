from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Utilities.Data import Menu_Bar
import pytest
import logging
class Base:
        driver = None
        @staticmethod
        def createdriver():
            if Base.driver == None:   
                Base.driver = webdriver.Chrome(executable_path="D:\\Tasks Module Automation\\PageObjects\\chromedriver.exe") 
        @staticmethod
        def set_logger():     
                logging.basicConfig(filename="D:\\Tasks Module Automation\\Logs\\loggg.log"
                ,level = logging.DEBUG,format = "%(asctime)s -- %(module)s  -- %(funcName)s -- %(lineno)d -- %(message)s")
        def open_new_window(self):
             Base.driver.execute_script("window.open('');")
             Base.driver.switch_to.window(Base.driver.window_handles[1])
             Base.driver.get(Menu_Bar.taskboard_summary())
