from lib.browser import Browser


class BasePage(Browser):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self):
        super(BasePage, self).__init__()
