from logging import getLogger

from playwright.sync_api import Page


class BasePage:
    """
    Base page to add shared properties and methods
    """

    def __init__(self, page: Page):
        self.url: str
        self.logger = getLogger(__name__)
        self.page = page
        self._choose_a_base_button: str = ""
        self._close_ai_button: str = ""
        self._natasha: str = ""
        self._close__natasha: str = ""

    def navigate(self):
        """
        Navigates to the specified url
        """
        self.page.goto(self.url)
        if self.page.locator(self._choose_a_base_button).count():
            self.page.wait_for_selector(self._choose_a_base_button).click()
            self.page.wait_for_selector(self._close_ai_button).click()
            self.page.wait_for_selector(self._natasha).hover(position={"x": 10, "y": 10})
            self.page.wait_for_selector(self._close__natasha).click()
