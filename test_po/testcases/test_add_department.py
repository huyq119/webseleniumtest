from test_po.page.contact_page import ContactPage
from test_po.page.main_page import MainPage


class TestAddDepartment():

    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        result = self.main.goto_contact().goto_add_department().add_department("huyuqi").get_department_name()
        assert "huyuqi" == result
