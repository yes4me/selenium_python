from page_objects.base_page import BasePage


class GoogleHomePage(BasePage):
    def __init__(self):
        super(GoogleHomePage, self).__init__()

    def visit(self):
        self.navigate(self.HOME)

    def search(self, text_to_search):
        element = self.find_element_by_name('q')
        self.type(element, text_to_search)
        self.submit(element)
