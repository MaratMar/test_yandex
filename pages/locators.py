from selenium.webdriver.common.by import By


class FiledFromTo():
    FIELD_FROM = (By.CSS_SELECTOR, '#from')
    FIELD_TO = (By.CSS_SELECTOR, "#to")


class ModeTrips():
    MODE_OPTIMAL = (By.XPATH, '//*[@class="modes-container"]/div[1]')
    MODE_FAST = (By.XPATH, '//*[@class="modes-container"]/div[2]')
    MODE_OWN = (By.XPATH, '//*[@class="modes-container"]/div[3]')


class TypesTrips():
    TYPE_CAR = (By.XPATH, '//*[@class="types-container"]//div[1]//img')
    TYPE_WALK = (By.XPATH, '//*[@class="types-container"]//div[2]//img')
    TYPE_TAXI = (By.XPATH, '//*[@class="types-container"]//div[3]//img')
    TYPE_BIKE = (By.XPATH, '//*[@class="types-container"]//div[4]//img')
    TYPE_SCOOTER = (By.XPATH, '//*[@class="types-container"]//div[5]//img')
    TYPE_DRIVE = (By.XPATH, '//*[@class="types-container"]//div[last()]//img')


class ButtonResult():
    BUTTON_RESULT = (By.XPATH, '//*[@class="results-container"]//button')


class TypeCar():
    TYPE_EVERYDAY = (By.XPATH, '//*[@class="tariff-cards"]//*[@alt="Повседневный"]')
    TYPE_HIKI = (By.XPATH, '//*[@class="tariff-cards"]//*[@alt="Походный"]')
    TYPE_LUX = (By.XPATH, '//*[@class="tariff-cards"]//*[@alt="Роскошный"]')


class FiledForm():
    FIELD_PAYMENT = (By.XPATH, '//*[@class="form"]//*[@class="pp-value"]')
    ADD_CARD = (By.XPATH, '//*[@class="modal"]//*[@class="pp-checkbox"]')
    FIELD_NUMBER_CARD = (By.XPATH, '//*[@class="section active unusual"]//*[@id="number"]')
    FILED_CODE = (By.XPATH, '//*[@class="section active unusual"]//*[@id="code"]')