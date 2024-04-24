import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_order_page import LocatorsOrder


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Закрываем соощение о куки')
    def click_cockie_button(self):
        self.driver.find_element(*LocatorsOrder.COCKIE).click()