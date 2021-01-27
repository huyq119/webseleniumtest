from test_po.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        # 实例化 TestMainPage类
        result = self.main.goto_add_member().add_member("number4", "121200", "13301199950").get_list()
        assert "number4" in result

    def test_add_member_fail(self):
        result = self.main.goto_add_member().add_member_fail("number5", "121200", "13301199950").get_list()
        assert "number5" not in result


