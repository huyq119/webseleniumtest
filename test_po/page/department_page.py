from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class DepartmentPage(BasePage):

    def get_department_name(self):
        """
        返回当前部门名称，进行判断
        :return:
        """
        party_name = self.find(By.CSS_SELECTOR, ".ww_commonCntHead_title_inner_text #party_name").text
        print(party_name)

        return party_name
