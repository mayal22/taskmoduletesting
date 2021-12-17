import pytest
from PageObjects.login import Loggedin
from Utilities.Data import Choose_env
@pytest.fixture
def logged_as():
    admin = Loggedin()
    admin.createdriver()
    admin.driver.get(Choose_env.choose_stagging())
    admin.capture_username()
    admin.capture_password()
    home_page = admin.capture_home_title()
    yield
    admin.driver.quit()


