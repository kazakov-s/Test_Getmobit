from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import AttachmentType
from data import *
from pages.base_page import BasePage


class VerifyUser(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//ul[@class="nav nav-tabs hidden-xs"]/li[2]/a')
    INPUT_EMAIL = (By.XPATH, '//input[@name="login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    AUTH_BUTTON = (By.XPATH, '//input[@type="submit"]')
    ADD_USER_BUTTON = (By.XPATH, '//a[text()="Добавить пользователя"]')
    SEARCH_INPUT = (By.XPATH, '//input[@name="q"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    VIEW_BUTTON = (By.XPATH, '//a[text()="Посмотреть"]')

    USER_EMAIL = (By.XPATH, f'//td[text()="{USER_NAME}"]')
    USER_FIO = (By.XPATH, f'//td[text()="{NAME}"]')
    USER_GENDER = (By.XPATH, '//select[@name="gender"]')
    USER_BIRTHDAY = (By.XPATH, '//td[contains(text(), "1971-07-29")]')
    WORK_START_DATE = (By.XPATH, '//td[contains(text(), "2004-01-01")]')
    USER_HOBBY = (By.XPATH, f'//textarea[@name="hobby"]')
    USER_NAME_1 = (By.XPATH, f'//td[text()="{NAME1}"]')
    USER_SURNAME1 = (By.XPATH, f'//td[text()="{SURNAME1}"]')
    USER_FATHERNAME1 = (By.XPATH, f'//td[text()="{FATHERNAME}"]')
    USER_CAT = (By.XPATH, f'//td[text()="{CAT}"]')
    USER_DOG = (By.XPATH, f'//td[text()="{DOG}"]')
    USER_PARROT = (By.XPATH, f'//td[text()="{PARROT}"]')
    USER_CAVY = (By.XPATH, f'//td[text()="{CAVY}"]')
    USER_HAMSTER = (By.XPATH, f'//td[text()="{HAMSTER}"]')
    USER_SQUIRREL = (By.XPATH, f'//td[text()="{SQUIRREL}"]')
    USER_PHONE = (By.XPATH, f'//td[text()="{PHONE}"]')
    USER_ADDRESS = (By.XPATH, f'//td[text()="{ADDRESS}"]')
    USER_INN = (By.XPATH, f'//td[text()="{INN}"]')

    def user_login(self):
        self.find(self.LOGIN_BUTTON, 'Элемент LOGIN_BUTTON не найден, функция user_login').click()
        self.find(self.INPUT_EMAIL, 'Элемент INPUT_EMAIL не найден, функция user_login').send_keys(USER_NAME)
        self.find(self.INPUT_PASSWORD, 'Элемент INPUT_PASSWORD не найден, функция user_login').send_keys(USER_PASS)
        self.find(self.AUTH_BUTTON, 'Элемент AUTH_BUTTON не найден, функция user_login').click()

    def user_search(self):
        self.find(self.SEARCH_INPUT, '').send_keys(USER_NAME)
        self.find(self.SEARCH_BUTTON, '').click()
        self.find(self.VIEW_BUTTON, '').click()

    def verify_user(self):
        email = self.find(self.USER_EMAIL, 'Элемент USER_EMAIL не найден').text
        assert email == USER_NAME
        fio = self.find(self.USER_FIO, 'Элемент USER_FIO не найден').text
        assert fio == NAME
        selected_element = self.find(self.USER_GENDER, 'Элемент USER_GENDER не найден')
        select = Select(selected_element)
        selected_option = select.first_selected_option
        assert selected_option.__getattribute__(
            'text') == 'Мужской', 'Пол пользователя не совпадает с тестовыми данными'
        birthday = self.find(self.USER_BIRTHDAY, 'Элемент USER_BIRTHDAY не найден').text
        assert birthday == '1971-07-29', 'Дата рождения не совпадает с тестовыми данными'  # хардкод, переформатирование даты не проводил
        work_start = self.find(self.WORK_START_DATE, 'Элемент WORK_START_DATE не найден').text
        assert work_start == '2004-01-01', 'Дата начала работы не совпадает с тестовыми данными'  # хардкод, переформатирование даты не проводил
        hobby = self.find(self.USER_HOBBY, 'Элемент USER_HOBBY не найден').text
        assert hobby == HOBBY, 'Хобби пользователя не совпадает с тестовыми данными'
        name1 = self.find(self.USER_NAME_1, 'Элемент USER_NAME_1 не найден').text
        assert name1 == NAME1, 'Имя1 пользователя не совпадает с тестовыми данными'
        surname1 = self.find(self.USER_SURNAME1, 'Элемент USER_SURNAME1 не найден').text
        assert surname1 == SURNAME1, 'Фамилия1 пользователя не совпадает с тестовыми данными'
        fathername1 = self.find(self.USER_FATHERNAME1, 'Элемент USER_FATHERNAME1 не найден').text
        assert fathername1 == FATHERNAME, 'Отчество пользователя не совпадает с тестовыми данными'
        cat = self.find(self.USER_CAT, 'Элемент USER_CAT не найден').text
        assert cat == CAT, 'Имя кошечки пользователя не совпадает с тестовыми данными'
        dog = self.find(self.USER_DOG, 'Элемент USER_DOG не найден').text
        assert dog == DOG, 'Имя собачки пользователя не совпадает с тестовыми данными'
        parrot = self.find(self.USER_PARROT, 'Элемент USER_PARROT не найден').text
        assert parrot == PARROT, 'Имя попугайчика пользователя не совпадает с тестовыми данными'
        cavy = self.find(self.USER_CAVY, 'Элемент USER_CAVY не найден').text
        assert cavy == CAVY, 'Имя свинки пользователя не совпадает с тестовыми данными'
        hamster = self.find(self.USER_HAMSTER, 'Элемент USER_HAMSTER не найден').text
        assert hamster == HAMSTER, 'Имя хомячка пользователя не совпадает с тестовыми данными'
        squirrel = self.find(self.USER_SQUIRREL, 'Элемент USER_SQUIRREL не найден').text
        assert squirrel == SQUIRREL, 'Имя хомячка пользователя не совпадает с тестовыми данными'
        tel = self.find(self.USER_PHONE, 'Элемент USER_PHONE не найден').text
        assert tel == PHONE, 'Телефон пользователя не совпадает с тестовыми данными'
        address = self.find(self.USER_ADDRESS, 'Элемент USER_ADDRESS не найден').text
        assert address == ADDRESS, 'Адрес пользователя не совпадает с тестовыми данными'
        inn = self.find(self.USER_INN, 'Элемент USER_INN не найден').text
        assert inn == INN, 'ИНН пользователя не совпадает с тестовыми данными'
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                      attachment_type=AttachmentType.PNG)
