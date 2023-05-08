import time

import pytest
import parametrize_from_file
from pages.base_page import BasePage
from pages.locators import *
from pages.precondition_page import Precondition

link = "https://ade60bcc-6435-4a77-ac32-29afb1a25aa8.serverhub.praktikum-services.ru"


@pytest.mark.skip
def test_presence_fileds_from(browser):
    page = BasePage(browser, link)
    page.open()
    page.is_element_present(*FiledFromTo.FIELD_FROM)


@pytest.mark.skip
def test_presence_fileds_to(browser):
    page = BasePage(browser, link)
    page.open()
    page.is_element_present(*FiledFromTo.FIELD_TO)


@pytest.mark.skip
def test_check_mode(browser):
    page = Precondition(browser, link)
    page.open()
    page.fill_filelds_from_to("Хамовнический Вал, 34", "3-я Фрунзенская улица, 12")
    page.go_to_choice(*ModeTrips.MODE_OWN)
    page.go_to_choice(*TypesTrips.TYPE_DRIVE)
    page.go_to_choice(*ButtonResult.BUTTON_RESULT)


test_data = {
    ('000000001234', '12', '0000 0000 1234'),
    ('000011001234', '13', '000000001234'),
    ('111111111234', '14', '111111111234'),

}


@pytest.mark.parametrize("number_card, code, expected_result", test_data)
def test_add_grant(browser, number_card, code, expected_result):
    page = Precondition(browser, link)
    page.open()
    page.precondition_started("Хамовнический Вал, 34", "3-я Фрунзенская улица, 12")
    page.open_payment()
    time.sleep(5)
    page.open_add_card()
    page.fill_filed(*FiledForm.FIELD_NUMBER_CARD, number_card)
    page.fill_filed(*FiledForm.FILED_CODE, code)
    res = page.return_status(By.XPATH, '//*[@class="pp-buttons"]//*[@type="submit"]')
    print(res)
    assert res == "active", 'disabled button'
