from test_po.page.contact_page import ContactPage


class TestAddDepartment():

    def setup_class(self):
        pass

    def test_add_department(self):
        contact = ContactPage()
        result = contact.goto_add_department().add_department().get_department_name()
        assert result == True
