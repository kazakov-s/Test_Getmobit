from data import START_URL
from pages.delete_user import DeleteUser
import allure

class TestLoginUser():

    @allure.suite("Тестовое задание для Getmobit")
    @allure.title('Удаляем созданного пользователя')
    @allure.description('Производим авторизацию с учетными данными менеджера и удалям созданного пользователя.')
    @allure.tag('Delete')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label('Developer', 'Sergey Kazakov')
    def test_delete_user(self, browser):
        browser.get(START_URL)
        self.page = DeleteUser(browser)
        self.page.manager_login()
        self.page.user_delete()
