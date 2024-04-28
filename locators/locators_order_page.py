from selenium.webdriver.common.by import By

class LocatorsOrder:

# Кнопка куки
    BTN_CUCI = (By.XPATH , "//button[contains(text() , 'да все привыкли')]")
# Кнопка Заказать на главной странице
    BTN_ORDER_MAIN = (By.XPATH , ".//button[@class='Button_Button__ra12g']")
# Кнопка Заказать внизу страницы
    BTN_ORDER_DOWN = (By.XPATH , "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
# Поле Имя
    FIELD_NAME = (By.XPATH , ".//input[contains(@placeholder, 'Имя')]")
# Поле Фамилия
    FIELD_SURNAME = (By.XPATH , ".//input[contains(@placeholder, 'Фамилия')]")
# Поле Адрес
    FIELD_ADRESS = (By.XPATH , ".//input[contains(@placeholder, ' Адрес: куда привезти заказ')]")
# Поле Станция метро
    FIELD_METRO_STATION = (By.XPATH ,"//input[contains(@placeholder, ' Станция метро')]")
# Сама станция метро
    METRO_STATION = (By.XPATH,  ".//div[@class = 'select-search__select']//div[text()='Преображенская площадь']")
    METRO_STATION2 =(By.XPATH,  ".//div[@class = 'select-search__select']//div[text()='Черкизовская']")
# Поле телефон
    FIELD_PHONE = (By.XPATH , "//input[contains(@placeholder, ' Телефон: на него позвонит курьер')]")
# Кнопка Далее
    BTN_FURTHER = (By.XPATH , ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
# Поле Когда привезти самокат
    FIELD_WHEN_GOTO_SAMOKAT = (By.XPATH , "//div[@class='react-datepicker__input-container']")
# Первая дата
    DATA_WHEN_GOTO_SAMOKAT_ONE =(By.XPATH , "//div[@aria-label='Choose среда, 1-е мая 2024 г.']")
# Вторая дата
    DATA_WHEN_GOTO_SAMOKAT_TWO = (By.XPATH , "//div[@aria-label='Choose четверг, 2-е мая 2024 г.']")
# Поле Срок аренды
    FIELD_DATA_RENT = (By.XPATH , "//div[@class='Dropdown-placeholder']")
# Колличество суток
    DATA_RENT_TREE_DAYS = (By.XPATH , "//div[text()='трое суток']/parent::div[@class='Dropdown-menu']")
    DATA_RENT_TWO_DAYS = (By.XPATH , "//div[text()='двое суток']/parent::div[@class='Dropdown-menu']")
# Цвет самоката Черная жемчужина
    FIELD_COLOUR_SAMOCAT_BLACK = (By.XPATH , "//label[@for='black']")
# Цвет самоката Серая безысходность
    FIELD_COLOUR_SAMOCAT_GREY = (By.XPATH , "//label[@for='grey']")
# Поле комментарий
    FIELD_COMMENT_TEXT = (By.XPATH , "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='Комментарий для курьера']")
# Кнопка Заказать в форме Про аренду
    BTN_ORDER_RENT = (By.XPATH , "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
# Кнопка Назад в форме про аренду
    BTN_BACK_RENT = (By.XPATH , "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")
# Заголовок формы Хотите завершить заказ
    TITLE_ARRANGE_ORDER =(By.XPATH , "//div[@class='Order_ModalHeader__3FDaJ']")
# Кнопка Да в форме Хотите завершить заказ
    BTN_YES_ARRANGE_ORDER =(By.XPATH , "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
# Кнопка Нет Хотите завершить заказ
    BTN_NO_ARRANGE_ORDER = (By.XPATH , "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Нет']")
# Заголовок Заказ оформлен
    TITLE_ORDER_REGISTR = (By.XPATH , "//div[@class='Order_ModalHeader__3FDaJ']")
# Кнопка Посмотреть статус в форме заказоформлен
    BTN_CHECK_STATUS = (By.XPATH , "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")
# Поле Номера заказа в форме статус заказа
    FIELD_NUMBER_ORDER = (By.XPATH , "Input_Input__1iN_Z Track_Input__1g7lq Input_Filled__1rDxs Input_Responsible__1jDKN")
# Логотип Яндекс
    LOGO_YANDEX = ( By.XPATH , "//img[@src='/assets/ya.svg']")
# Логотип Самокат
    LOGO_SAMOKAT = (By.XPATH , "//img[@src='/assets/scooter.svg']")
# Куки
    COCKIE = (By.XPATH, "//button[contains(text() , 'да все привыкли')]")


