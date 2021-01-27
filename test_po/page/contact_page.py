from time import sleep

from selenium.webdriver.common.by import By

from test_po.page.add_department_page import AddDepartmentPage
from test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def goto_add_department(self):
        return AddDepartmentPage()

    def goto_import_list(self):
        pass

    def get_list(self):
        """
        返回通讯录页面的人员信息
        :return:
        """
        self.driver.find_elements(By.CSS_SELECTOR, "")
        sleep(5)
        return True
