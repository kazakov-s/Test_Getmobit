import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from data import MANAGER_NAME, MANAGER_PASS, USER_NAME
from data import NAME
from pages.base_page import BasePage


class ConfirmDelete(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//ul[@class="nav nav-tabs hidden-xs"]/li[2]/a')
    INPUT_EMAIL = (By.XPATH, '//input[@name="login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    AUTH_BUTTON = (By.XPATH, '//input[@type="submit"]')
    SEARCH_INPUT = (By.XPATH, '//input[@name="q"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    USER_FIO = (By.XPATH, f'//td[text()="{NAME}"]')

    def manager_login(self):
        self.find(self.LOGIN_BUTTON, 'Элемент LOGIN_BUTTON не найден, функция manager_login').click()
        self.find(self.INPUT_EMAIL, 'Элемент INPUT_EMAIL не найден, функция manager_login').send_keys(MANAGER_NAME)
        self.find(self.INPUT_PASSWORD, 'Элемент INPUT_PASSWORD не найден, функция manager_login').send_keys(
            MANAGER_PASS)
        self.find(self.AUTH_BUTTON, 'Элемент AUTH_BUTTON не найден, функция manager_login').click()

    def confirm_delete(self):
        self.find(self.SEARCH_INPUT, '').send_keys(USER_NAME)
        self.find(self.SEARCH_BUTTON, '').click()
        self.find(self.USER_FIO, 'Тест ожидаемо упал. Пользователь уже удален из базы.').text
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                      attachment_type=AttachmentType.PNG)
