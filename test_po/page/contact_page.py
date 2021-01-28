from time import sleep

from selenium.webdriver.common.by import By

from test_po.page.add_department_page import AddDepartmentPage
from test_po.page.base_page import BasePage


class ContactPage(BasePage):

    def goto_add_member(self):
        pass

    def goto_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartmentPage(self._driver)

    def goto_import_list(self):
        pass

    def get_list(self):
        """
        返回通讯录页面的人员信息
        :return:
        """
        name_webelement_list = self._driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)
        return name_list
