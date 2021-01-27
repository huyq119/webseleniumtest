from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self):
        self.driver.find_element(By.ID, "username").send_keys("number3")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("12123")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13301190003")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)
