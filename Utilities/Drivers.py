import configparser
configg = configparser.ConfigParser()
configg.read("D:\\Tasks Module Automation\\Configrations\\element_drivers.ini")
class Element:
    @staticmethod
    def cap_username():
        user = configg.get("Admin Login Drivers","username id")
        return user
    @staticmethod
    def cap_password():
        password = configg.get("Admin Login Drivers","password id")
        return password
class Menu_Element:
    @staticmethod
    def cap_menu():
        menus = configg.get("Menu Elements","menu css")
        return menus
class TaskBoard_Element:
    def assigned_task_board():
        assigned_task = configg.get("Task Board Elements","assigned task board css")
        return assigned_task
    def assigned_task_button():
        task_button = configg.get("Task Board Elements","assgined task button css")
        return task_button