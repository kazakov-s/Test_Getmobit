from data import START_URL
from pages.verify_user import VerifyUser
import allure

class TestLoginUser():

    @allure.suite("Тестовое задание для Getmobit")
    @allure.title('Логин под созданным пользователем и проверка полей')
    @allure.description('Производим авторизацию с учетными данными созданного пользователя и проводим проверки корректности данных.')
    @allure.tag('Verify')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label('Developer', 'Sergey Kazakov')
    def test_verify_user(self, browser):
        browser.get(START_URL)
        self.page = VerifyUser(browser)
        self.page.user_login()
        self.page.user_search()
        self.page.verify_user()
