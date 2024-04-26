import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators_order_page import LocatorsOrder
from data import SamocatAuthData
from conftest import driver


class OrderPage(BasePage):


    @allure.step('Клик на кнопку Заказать')
    def click_order_down_button(self):
        self.driver.find_element(*LocatorsOrder.BTN_ORDER_DOWN).click()


    @allure.step('Кликаем Заказать')
    def click_order_main_button(self):
        self.driver.find_element(*LocatorsOrder.BTN_ORDER_MAIN).click()


    @allure.step('Заполняем поле Имя')
    def set_name_input(self, name):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_NAME)
        login_input.send_keys(name)


    @allure.step('Заполняем поле Фамилия')
    def set_surname_input(self, surname):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_SURNAME)
        login_input.send_keys(surname)


    @allure.step('Заполняем поле Адресс')
    def set_adress_input(self,adress):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_ADRESS)
        login_input.send_keys(adress)


    @allure.step('Заполняем поле Станция метро')
    def click_metro_station_input(self):
         login_input = self.driver.find_element(*LocatorsOrder.FIELD_METRO_STATION)
         login_input.click()


    @allure.step('Заполняем поле Станция метро')
    def click_metro_station_input(self):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_METRO_STATION)
        login_input.click()


    @allure.step('Заполняем поле Станция метро')
    def click_station_input(self):
        login_input = self.driver.find_element(*LocatorsOrder.METRO_STATION2)
        login_input.click()


    @allure.step('Заполняем поле Телефон')
    def set_phone_input(self, phone):
        login_input = self.driver.find_element(*LocatorsOrder .FIELD_PHONE)
        login_input.send_keys(phone)


    @allure.step('Кликаем на кнопку Далее')
    def click_further_button(self):
        button = self.driver.find_element(*LocatorsOrder.BTN_FURTHER)
        button.click()


    @allure.step('Кликаем по полю Когда привезти самокат')
    def click_data_input(self):
        button = self.driver.find_element(*LocatorsOrder.FIELD_WHEN_GOTO_SAMOKAT)
        button.click()


    @allure.step('Выбираем конкретную дату')
    def click_concret_data(self):
        button = self.driver.find_element(*LocatorsOrder.DATA_WHEN_GOTO_SAMOKAT_TWO)
        button.click()


    @allure.step('Заполняем поле Срок аренды')
    def click_data_rent_input(self):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_DATA_RENT)
        login_input.click()


    @allure.step('Выбираем срок аренды в поле Срок аренды')
    def click_data_rent_three_input(self):
        login_input = self.driver.find_element(*LocatorsOrder.DATA_RENT_TWO_DAYS)
        login_input.click()


    @allure.step('Заполняем поле Цвет самоката')
    def click_colour_samokat_input(self):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_COLOUR_SAMOCAT_BLACK)
        login_input.click()


    @allure.step('Заполняем поле Комментарий')
    def set_comment_input(self, comment):
        login_input = self.driver.find_element(*LocatorsOrder.FIELD_COMMENT_TEXT)
        login_input.send_keys(comment)


    @allure.step('Кликаем по кнопке заказть в форме про аренду')
    def click_order_rent_button(self):
        button = self.driver.find_element(*LocatorsOrder.BTN_ORDER_RENT)
        button.click()



    @allure.step('Кликаем по  кнопке Да в форме Хотите завершить заказ')
    def click_yes_button(self):
        button = self.driver.find_element(*LocatorsOrder.BTN_YES_ARRANGE_ORDER)
        button.click()


    @allure.step('Кликаем по  кнопке Посмотреть статус в форме Заказ оформлен')
    def click_check_status_button(self):
        button = self.driver.find_element(*LocatorsOrder.BTN_CHECK_STATUS)
        button.click()


    @allure.step('Клик на логотип Яндекс')
    def click_logo_yandex(self):
        linc = self.driver.find_element(*LocatorsOrder.LOGO_YANDEX)
        linc.click()


    @allure.step('Клик на логотип Самокат')
    def click_logo_samocat(self):
        linc = self.driver.find_element(*LocatorsOrder.LOGO_SAMOKAT)
        linc.click()



