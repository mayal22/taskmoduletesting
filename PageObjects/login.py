from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PageObjects.basefile import Base
from Utilities.Data import Login
from Utilities.Drivers import Element
class Loggedin(Base):
    def capture_username(self):
        return self.driver.find_element(By.ID,Element.cap_username()).send_keys(Login.data_admin_username())
    def capture_password(self):
        self.driver.find_element(By.ID,Element.cap_password()).send_keys(Login.data_admin_password())
        self.driver.find_element(By.ID,Element.cap_password()).send_keys(Keys.ENTER)
        element = WebDriverWait(self.driver, 10).until(
        EC.title_is("Dashboards | Index"))
    def capture_home_title(self):
        return self.driver.title