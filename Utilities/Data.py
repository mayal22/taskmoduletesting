import configparser
config = configparser.ConfigParser()
config.read("D:\\Tasks Module Automation\\Configrations\\config.ini")
class Login:
    @staticmethod
    def data_admin_username():
        user = config.get("Admin Login","username")
        return user
    @staticmethod
    def data_admin_password():
        password = config.get("Admin Login","password")
        return password
class Choose_env:
    @staticmethod
    def choose_stagging():
        stagging = config.get("environment","test")
        return stagging
    @staticmethod
    def choose_production():
        erp = config.get("environment","production")
        return erp
class Menu_Bar:
    @staticmethod
    def taskboard_summary():
        task_board_summary = config.get("Menu url","Task Board Summary")
        return task_board_summary

        

