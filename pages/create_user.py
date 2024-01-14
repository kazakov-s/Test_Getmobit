import os
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from data import *
from pages.base_page import BasePage


class CreateUser(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//ul[@class="nav nav-tabs hidden-xs"]/li[2]/a')
    INPUT_EMAIL = (By.XPATH, '//input[@name="login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    AUTH_BUTTON = (By.XPATH, '//input[@type="submit"]')
    ADD_USER_BUTTON = (By.XPATH, '//a[text()="Добавить пользователя"]')
    SEARCH_INPUT = (By.XPATH, '//input[@name="q"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    VIEW_BUTTON = (By.XPATH, '//a[@class="btn btn-success"]')

    USER_NAME = (By.XPATH, '//input[@name="noibiz_name"]')
    USER_EMAIL = (By.XPATH, '//input[@name="noibiz_email"]')
    USER_PASSWORD = (By.XPATH, '//input[@name="noibiz_password"]')
    USER_AVATAR = (By.XPATH, '//input[@name="noibiz_avatar"]')
    AVATAR_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\' + 'avatar.jpg'
    USER_BIRTHDAY = (By.XPATH, '//input[@name="noibiz_birthday"]')
    GENDER_DROPDOWN = (By.XPATH, '//select[@name="noibiz_gender"]')
    WORK_START_DATE = (By.XPATH, '//input[@name="noibiz_date_start"]')
    USER_HOBBY = (By.XPATH, '//textarea[@name="noibiz_hobby"]')
    USER_NAME1 = (By.XPATH, '//input[@name="noibiz_name1"]')
    USER_SURNAME1 = (By.XPATH, '//input[@name="noibiz_surname1"]')
    USER_FATHERNAME = (By.XPATH, '//input[@class="form-control numberfilter"]')
    USER_CAT = (By.XPATH, '//input[@name="noibiz_cat"]')
    USER_DOG = (By.XPATH, '//input[@name="noibiz_dog"]')
    USER_PARROT = (By.XPATH, '//input[@name="noibiz_parrot"]')
    USER_CAVY = (By.XPATH, '//input[@name="noibiz_cavy"]')
    USER_HAMSTER = (By.XPATH, '//input[@name="noibiz_hamster"]')
    USER_SQUIRREL = (By.XPATH, '//input[@name="noibiz_squirrel"]')
    USER_PHONE = (By.XPATH, '//input[@name="noibiz_phone"]')
    USER_ADDRESS = (By.XPATH, '//input[@name="noibiz_adres"]')
    USER_INN = (By.XPATH, '//input[@name="noibiz_inn"]')
    SUBMIT_BTN = (By.XPATH, '//input[@type="submit"]')

    def manager_login(self):
        self.find(self.LOGIN_BUTTON, 'Элемент LOGIN_BUTTON не найден, функция manager_login').click()
        self.find(self.INPUT_EMAIL, 'Элемент INPUT_EMAIL не найден, функция manager_login').send_keys(MANAGER_NAME)
        self.find(self.INPUT_PASSWORD, 'Элемент INPUT_PASSWORD не найден, функция manager_login').send_keys(
            MANAGER_PASS)
        self.find(self.AUTH_BUTTON, 'Элемент AUTH_BUTTON не найден, функция manager_login').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                      attachment_type=AttachmentType.PNG)

    def confirm_manager_login(self):
        try:
            self.find(self.ADD_USER_BUTTON, 'Элемент ADD_USER_BUTTON не найден, функция confirm_manager_login')
        except NoSuchElementException:
            return False
        return True

    def select_gender(self):
        dropdown = self.find(self.GENDER_DROPDOWN, '')
        dropdown.click()
        se = Select(dropdown)
        for item in se.options:
            if item.text == 'Мужской':
                item.click()
                break

    def create_new_user(self):
        self.find(self.ADD_USER_BUTTON, '').click()
        self.find(self.USER_NAME, '').send_keys(NAME)
        self.find(self.USER_EMAIL, '').send_keys(USER_NAME)
        self.find(self.USER_PASSWORD, '').send_keys(USER_PASS)
        print(self.AVATAR_PATH)
        self.find(self.USER_AVATAR, '').send_keys(self.AVATAR_PATH)
        self.find(self.USER_BIRTHDAY, '').send_keys(BIRTHDAY)
        self.select_gender()
        self.find(self.WORK_START_DATE, '').send_keys(DATE_START)
        self.find(self.WORK_START_DATE, '').send_keys(DATE_START)
        self.find(self.USER_HOBBY, '').send_keys(HOBBY)
        self.find(self.USER_NAME1, '').send_keys(NAME1)
        self.find(self.USER_SURNAME1, '').send_keys(SURNAME1)
        self.find(self.USER_FATHERNAME, '').send_keys(FATHERNAME)
        self.find(self.USER_CAT, '').send_keys(CAT)
        self.find(self.USER_DOG, '').send_keys(DOG)
        self.find(self.USER_PARROT, '').send_keys(PARROT)
        self.find(self.USER_CAVY, '').send_keys(CAVY)
        self.find(self.USER_HAMSTER, '').send_keys(HAMSTER)
        self.find(self.USER_SQUIRREL, '').send_keys(SQUIRREL)
        self.find(self.USER_PHONE, '').send_keys(PHONE)
        self.find(self.USER_ADDRESS, '').send_keys(ADDRESS)
        self.find(self.USER_INN, '').send_keys(INN)
        self.find(self.SUBMIT_BTN, '').click()
        allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot',
                      attachment_type=AttachmentType.PNG)
