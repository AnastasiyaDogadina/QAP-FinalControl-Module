from selenium.webdriver.common.by import By


class AuthtorizationLocators:
    auth_title = (By.TAG_NAME, 'h1')
    auth_login = (By.ID, 'username')
    auth_pass = (By.ID, 'password')
    btn_enter = (By.ID, "kc-login")
    login_placeholder = (
        By.XPATH, '//div[contains(@class, "tabs-input-container__login")]//span[@class="rt-input__placeholder"]')
    tab_phone = (By.ID, 't-btn-tab-phone')
    tab_mail = (By.ID, "t-btn-tab-mail")
    tab_login = (By.ID, "t-btn-tab-login")
    tab_pers_account = (By.ID, "t-btn-tab-ls")
    link_forgot_pass = (By.ID, "forgot_password")
    link_registration = (By.ID, "kc-register")
    link_agreement = (By.ID, "rt-footer-agreement-link")
    icon_vk = (By.ID, "oidc_vk")
    icon_ok = (By.ID, "oidc_ok")
    icon_male = (By.ID, "oidc_mail")
    icon_google = (By.ID, "oidc_google")
    icon_yandex = (By.ID, "oidc_ya")
    auth_error = (By.ID, 'form-error-message')


class AgrLocators:
    agr_title = (By.CLASS_NAME, 'offer-title')
