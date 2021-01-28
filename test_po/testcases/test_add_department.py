
from test_po.page.main_page import MainPage


class TestAddDepartment():

    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        result = self.main.goto_contact().goto_add_department().add_department("tester").get_department_name()
        assert "tester" == result

    def test_add_department_fail(self):
        result = self.main.goto_contact().goto_add_department().add_department_fail("tester").get_department_name()
        assert "tester" != result



