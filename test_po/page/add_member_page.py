from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, name, id, mobile):
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(id)
        self.find(By.ID, "memberAdd_phone").send_keys(mobile)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self._driver)

    def add_member_fail(self, name, id, mobile):
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(id)
        self.find(By.ID, "memberAdd_phone").send_keys(mobile)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return ContactPage(self._driver)
