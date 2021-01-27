from test_po.page.main_page import MainPage


class TestAddMember():

    def setup_class(self):
        pass

    def test_add_member(self):
        # 实例化 TestMainPage类
        main = MainPage()
        result = main.goto_add_member().add_member().get_list()
        assert result == True