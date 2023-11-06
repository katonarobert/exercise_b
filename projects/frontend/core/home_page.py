from os import getenv

import pytest
from playwright.sync_api import Page

from projects.frontend.core.base_page import BasePage


class HomePage(BasePage):
    """
    Home page class to contain locators and methods
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{getenv('BASE_URL')}/home"

        # Locators
        self._choose_a_base_button = (
            "#main > welcome-to-studio > div > div.popHolder.studioIntroModal > div.sticky-bottom-bar > button"
        )
        self._close_ai_button = "#app-component > div.wrapper > div.middlePart.middleWithFooter > main > app-home-templates > div.templateIntroduction > div.closeButton"
        self._natasha = "#main > div.rightBlock > div.bdrBtm > div > div > h2 > div.natashaPanel > div.natashaMsgPanel"
        self._close__natasha = "#main > div.rightBlock > div.bdrBtm > div > div > h2 > div.natashaPanel > div.natashaMsgPanel > div.closePanel"

    @property
    def sign_in_button_on_home_page(self):
        return self.page.wait_for_selector("#header > div > div > div.loginPanel > ul > li > button")

    @property
    def email_field(self):
        return self.page.wait_for_selector("#loginEmailInput")

    @property
    def password_field(self):
        return self.page.wait_for_selector(
            "#app-component > div:nth-child(2) > login > div > div.popHolder.loginScreen > div.loginRight > form > ul > li:nth-child(2) > div.relativeRow > input"
        )

    @property
    def sign_in_button_on_form(self):
        return self.page.wait_for_selector(
            "#app-component > div:nth-child(2) > login > div > div.popHolder.loginScreen > div.loginRight > form > div.footersection > div.actionbtn > button"
        )

    def submit_login_form(self):
        """
        Submits the login form with current user and password defined in .env
        """
        self.sign_in_button_on_home_page.click()
        self.email_field.fill(pytest.current_user["email"])
        self.password_field.fill(getenv("PASSWORD"))
        self.sign_in_button_on_form.click()
