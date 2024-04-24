import time

import allure
from locators.locators_order_page import LocatorsOrder
from data import SamocatAuthData
from data import Urls
from pages.order_page import OrderPage
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class TestOrderPage:

    @allure.title("Проверка оформления заказа через кнопку Заказать вверху страницы")
    @allure.description("Заполняем все поля и пытаемся оформить заказ")
    def test_order_main(self, driver):
        login_page = OrderPage(driver)
        login_page.open_page(Urls.SAMOKAT)
        login_page.click_cockie_button()
        login_page.click_order_main_button()
        login_page.set_name_input(SamocatAuthData.FIRST_NAME)
        login_page.set_surname_input(SamocatAuthData.FIRST_SURNAME)
        login_page.set_adress_input(SamocatAuthData.FIRST_ADRESS)
        login_page.click_metro_station_input()
        login_page.click_station_input()
        login_page.set_phone_input(SamocatAuthData.FIRST_PHONE)
        login_page.click_further_button()
        login_page.click_data_input()
        login_page.click_concret_data()
        login_page.click_data_rent_input()
        login_page.click_data_rent_three_input()
        login_page.click_colour_samokat_input()
        login_page.set_comment_input(SamocatAuthData.COMMENT)
        login_page.click_order_rent_button()
        login_page.click_yes_button()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LocatorsOrder.BTN_CHECK_STATUS)))

        assert driver.find_element(*LocatorsOrder.BTN_CHECK_STATUS).is_displayed()

    def test_logo_yandex(self, driver):
        login_page = OrderPage(driver)
        login_page.open_page(Urls.SAMOKAT)
        login_page.click_cockie_button()
        login_page.click_order_main_button()
        time.sleep(4)
        login_page.click_logo_yandex()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url == Urls.DZEN_URL

    def test_logo_samokat(self, driver):
        login_page = OrderPage(driver)
        login_page.open_page(Urls.SAMOKAT)
        login_page.click_cockie_button()
        login_page.click_order_main_button()
        login_page.click_logo_samocat()
        driver.switch_to.window(driver.window_handles[-1])
        assert driver.current_url == Urls.SAMOKAT


    @allure.title("Проверка оформления заказа через кнопку Заказать внизу старницы")
    @allure.description("Заполняем все поля и пытаемся оформить заказ")
    def test_order_main_down(self, driver):
        login_page = OrderPage(driver)
        login_page.open_page(Urls.SAMOKAT)
        login_page.click_cockie_button()
        login_page.click_order_down_button()
        login_page.set_name_input(SamocatAuthData.TWO_NAME)
        login_page.set_surname_input(SamocatAuthData.TWO_SURNAME)
        login_page.set_adress_input(SamocatAuthData.TWO_ADRESS)
        login_page.click_metro_station_input()
        login_page.click_station_input()
        login_page.set_phone_input(SamocatAuthData.TWO_PHONE)
        login_page.click_further_button()
        login_page.click_data_input()
        login_page.click_concret_data()
        login_page.click_data_rent_input()
        login_page.click_data_rent_three_input()
        login_page.click_colour_samokat_input()
        login_page.set_comment_input(SamocatAuthData.COMMENT)
        login_page.click_order_rent_button()
        login_page.click_yes_button()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LocatorsOrder.BTN_CHECK_STATUS)))

        assert driver.find_element(*LocatorsOrder.BTN_CHECK_STATUS).is_displayed()




