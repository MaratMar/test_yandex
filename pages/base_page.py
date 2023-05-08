from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self):  # открываем url
        self.browser.get(self.url)

    def is_element_present(self, how, what):  # проверка наличия элемента
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_choice(self, how, what):  # выбираем что-то и кликаем
        choice = self.browser.find_element(how, what)
        choice.click()

    def fill_filed(self, how, what, value):  # заполняем поле значнием value
        self.browser.find_element(how, what).send_keys(value)

    def return_status(self, how, what):
        return self.browser.find_element(how, what).is_enabled()
