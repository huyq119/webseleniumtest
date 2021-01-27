from selenium.webdriver.common.by import By

from test_po.page.add_member_page import AddMemberPage
from test_po.page.base_page import BasePage


class MainPage(BasePage):

    def goto_signin(self):
        pass

    def goto_signup(self):
        pass

    def goto_contact(self):
        pass

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)

    def goto_import_list(self):
        pass
