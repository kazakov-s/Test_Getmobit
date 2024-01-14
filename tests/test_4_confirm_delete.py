import pytest
import allure
from data import START_URL
from pages.confirm_delete import ConfirmDelete


class TestConfirmDelete():

    @pytest.mark.xfail(reason="Ожидаемо падает, т.к. пользователь удалён.") #
    @allure.suite("Тестовое задание для Getmobit")
    @allure.title('Проверяем, что пользователь удален')
    @allure.description('Производим поиск пользователя и проводим проверку факта уничтожения сущности.')
    @allure.tag('Confirm')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label('Developer', 'Sergey Kazakov')
    def test_confirm_delete_user(self, browser):
        browser.get(START_URL)
        self.page = ConfirmDelete(browser)
        self.page.manager_login()
        self.page.confirm_delete()
