from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    pass_title = (By.TAG_NAME, 'h1')
    pass_login = (By.ID, 'username')
    pass_btn = (By.ID, 'reset')
    pass_error = (By.ID, 'form-error-message')