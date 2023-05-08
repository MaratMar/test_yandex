import time

from pages.base_page import BasePage
from pages.locators import *


class Precondition(BasePage):
    def precondition_started(self, value_from, value_to):
        self.fill_filelds_from_to(value_from, value_to)
        self.fill_choice(ModeTrips.MODE_OWN, TypesTrips.TYPE_DRIVE, ButtonResult.BUTTON_RESULT)

    def fill_filelds_from_to(self, value_from, value_to):
        self.browser.find_element(*FiledFromTo.FIELD_FROM).send_keys(value_from)
        self.browser.find_element(*FiledFromTo.FIELD_TO).send_keys(value_to)

    def fill_choice(self, mod_trips, types_trips, button_result):
        self.browser.find_element(*mod_trips).click()
        time.sleep(5)
        self.browser.find_element(*types_trips).click()
        self.browser.find_element(*button_result).click()

    def open_payment(self):
        self.browser.find_element(*FiledForm.FIELD_PAYMENT).click()

    def open_add_card(self):
        self.browser.find_element(*FiledForm.ADD_CARD).click()
