import time

import allure
import pytest
from answers import answers
from locators.locators_order_page import LocatorsOrder
from data import SamocatAuthData
from data import Urls
from pages.main_page import QuestionPage
from conftest import driver
from locators.Lokators_main_page import LocatorsQuestion
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class TestQuestion:
    @allure.title('Проверка ответов по вопросам')
    @allure.description('Через параметризированный тестроверяем соответствие вопросам ответов')
    @pytest.mark.parametrize('question' ,answers)
    def test_click_and_get_answer(self ,driver, question):
        number, question = question
        question_page = QuestionPage(driver)
        question_page.open_page(Urls.SAMOKAT)
        question_page.click_cockie_button()
        question_page.skroll(driver)
        question_page.driver.find_element(*LocatorsQuestion.QUESTION1)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LocatorsQuestion.QUESTION1)))
        question_page.click_and_get_answer(number)
        assert question_page.click_and_get_answer(number) == question




