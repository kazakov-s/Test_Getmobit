from data import START_URL
from pages.create_user import CreateUser
import allure

class TestCreateUser():

    @allure.suite("Тестовое задание для Getmobit")
    @allure.title('Создание нового пользователя под учетной записью менеджера')
    @allure.description('Проверка функционала создания нового пользователя под учетной записью менеджера.')
    @allure.tag('Creare')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('Developer', 'Sergey Kazakov')
    def test_manager_create_user(self, browser):
        browser.get(START_URL)
        self.page = CreateUser(browser)
        self.page.manager_login()
        self.page.confirm_manager_login()
        self.page.create_new_user()

