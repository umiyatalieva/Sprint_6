import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.Lokators_main_page import LocatorsQuestion


class QuestionPage(BasePage):
    @allure.step('Кликаем на вопросы')
    def click_and_get_answer(self, i):
        question = (By.ID, f"accordion__heading-{i}")
        answer = (By.ID, f"accordion__panel-{i}")
        self.driver.find_element(*question).click()
        return self.driver.find_element(*answer).text







