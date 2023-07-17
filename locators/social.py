from selenium.webdriver.common.by import By


class SocialLocators:
    vk_login = (By.NAME, 'email')
    vk_pass = (By.NAME, 'pass')
    vk_submit_btn = (By.ID, 'install_allow')
    vk_error_message = (By.CLASS_NAME, 'box_error')
    ok_login = (By.ID, 'field_email')
    ok_pass = (By.ID, 'field_password')
    ok_submit_btn = (By.CLASS_NAME, 'form-actions_yes')
    ok_error_message = (By.CLASS_NAME, 'input-e')
    mail_login = (By.ID, 'login')
    mail_pass = (By.ID, 'password')
    mail_submit_btn = (By.CLASS_NAME, 'ui-button-main')
    mail_error_message = (By.CLASS_NAME, 'login-form__error')
    google_login = (By.ID, 'identifierId')
    google_submit_btn = (By.XPATH, '//button[contains(@class, "AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b")]')
    google_error_message = (By.CLASS_NAME, 'o6cuMc')
    yandex_login = (By.ID, 'passp-field-login')
    yandex_submit_btn = (By.ID, 'passp:sign-in')
    yandex_error_message = (By.ID, 'field:input-login:hint')
