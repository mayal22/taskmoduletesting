from selenium.webdriver.common.by import By
from PageObjects.basefile import Base
from Utilities.Drivers import TaskBoard_Element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Data import Menu_Bar
import time
class Assigned_task(Base):
    def assigned_task_board(self):
        self.open_new_window()
        Base.driver.implicitly_wait(5)
        data = Base.driver.find_element(By.CSS_SELECTOR,TaskBoard_Element.assigned_task_board())
        list_of_menu = data.find_elements(By.TAG_NAME,"li")
        # breakpoint()
        for each in list_of_menu:
            myself = each.find_element(By.TAG_NAME,"a")
            if myself.text == "Assigned Task Board":
                # breakpoint()
                print("yes it found")
                time.sleep(10)
                myself.click()
                time.sleep(10)
                break
        Base.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR,TaskBoard_Element.assigned_task_button()).click()
        self.driver.implicitly_wait(10)
            
