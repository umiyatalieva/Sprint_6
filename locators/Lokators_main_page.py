from selenium.webdriver.common.by import By

class LocatorsQuestion:
    # Заголовок Вопросы о важном
    TITLE_QUESTION = (By.XPATH,"//div[text()='Вопросы о важном'] ")
    # Вопросы и ответы
    QUESTION1 = (By.ID, "accordion__heading-0")
    ANSWER1 = (By.ID, "accordion__panel-0")
    QUESTION2 = (By.ID, "accordion__heading-1")
    ANSWER2 = (By.ID, "accordion__panel-1")
    QUESTION3 = (By.ID, "accordion__heading-2")
    ANSWER3 = (By.ID, "accordion__panel-2")
    QUESTION4 = (By.ID, "accordion__heading-3")
    ANSWER4 = (By.ID, "accordion__panel-3")
    QUESTION5 = (By.ID, "accordion__heading-4")
    ANSWER5 = (By.ID, "accordion__panel-4")
    QUESTION6 = (By.ID, "accordion__heading-5")
    ANSWER6 = (By.ID, "accordion__panel-5")
    QUESTION7 = (By.ID, "accordion__heading-6")
    ANSWER7 = (By.ID, "accordion__panel-6")
    QUESTION8 = (By.ID, "accordion__heading-7")
    ANSWER8 = (By.ID, "accordion__panel-7")

