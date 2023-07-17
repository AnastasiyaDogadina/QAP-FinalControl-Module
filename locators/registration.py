from selenium.webdriver.common.by import By


class RegistrationLocators:
    name = (By.NAME, 'firstName')
    surname = (By.NAME, 'lastName')
    reg_title = (By.TAG_NAME, 'h1')
    reg_login = (By.ID, 'address')
    reg_password = (By.ID, 'password')
    reg_password_confirm = (By.ID, 'password-confirm')
    reg_btn = (By.NAME, 'register')
    reg_error = (By.XPATH, '//span[contains(@class, "rt-input-container__meta--error")]')
