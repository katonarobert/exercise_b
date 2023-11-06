from playwright.sync_api import Page

from projects.frontend.core.home_page import HomePage


def test_login(page: Page):
    """
    Navigates to home page and submits the login form
    """
    HomePage(page).navigate()
    HomePage(page).submit_login_form()
