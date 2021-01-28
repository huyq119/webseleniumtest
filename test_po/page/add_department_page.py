from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.page.base_page import BasePage
from test_po.page.department_page import DepartmentPage


class AddDepartmentPage(BasePage):

    def add_department(self, title):
        self.find(By.CSS_SELECTOR, ".ww_inputText[name='name']").send_keys(title)
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, "div.js_party_list_container div.jstree-default a.jstree-anchor").click()
        self.find(By.CSS_SELECTOR, "div.ww_dialog_foot a.ww_btn_Blue").click()
        # 添加显示等待，等待alert消失后操作
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_cnt_operation a.js_add_member")))

        return DepartmentPage(self._driver)

    def add_department_fail(self, title):
        self.find(By.CSS_SELECTOR, ".ww_inputText[name='name']").send_keys(title)
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()
        self.find(By.CSS_SELECTOR, "div.js_party_list_container div.jstree-default a.jstree-anchor").click()
        self.find(By.CSS_SELECTOR, "div.ww_dialog_foot a.ww_btn_Blue").click()
        # 添加显示等待，等待alert消失后操作
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "div.ww_operationBar a.js_add_member")))

        return DepartmentPage(self._driver)


