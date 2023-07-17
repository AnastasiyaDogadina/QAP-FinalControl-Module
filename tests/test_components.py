from components.autorization import AuthPage
from locators import AuthtorizationLocators, RegistrationLocators, PasswordRecoveryLocators, AgrLocators, \
    SocialLocators
import pytest
from data_for_test import invalid, text_messages, valid


# Тест загрузки страницы регистрации

def test_load_reg_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    assert 'registration' in page.get_current_url()
    assert page.get_text_from_element(RegistrationLocators.reg_title) == 'Регистрация'


# Тест загрузки страницы авторизации

def test_load_auth_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()
    assert page.get_text_from_element(AuthtorizationLocators.auth_title) == 'Авторизация'


# Тест загрузки страницы восстановления пароля

def test_load_forgot_pass_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_forgot_pass)
    assert 'login-actions/reset-credentials' in page.get_current_url()
    assert page.get_text_from_element(PasswordRecoveryLocators.pass_title) == 'Восстановление пароля'


# Тест смены типов логина на странице авторизации
@pytest.mark.parametrize('locator, expected',
                         [(AuthtorizationLocators.tab_mail, 'Электронная почта'),
                          (AuthtorizationLocators.tab_login, 'Логин'),
                          (AuthtorizationLocators.tab_pers_account, 'Лицевой счёт'),
                          (AuthtorizationLocators.tab_phone, 'Мобильный телефон')])
def test_change_tabs_auth_page_positive(browser, locator, expected):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(locator)
    assert page.get_text_from_element(AuthtorizationLocators.login_placeholder) == expected


# Тест регистрации нового пользователя без указания учетных данных
def test_reg_user_without_data_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    reg_url = page.get_current_url()
    page.click_reg_btn()
    assert reg_url == page.get_current_url()


# Тест регистрации нового пользователя c указанием адреса почты в неверном формате
@pytest.mark.parametrize('email', invalid.incorrect_emails)
def test_reg_invalid_email_negative(browser, email):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_login, email)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == text_messages.wrong_login_message


# Тест регистрации нового пользователя c указанием пароля в неверном формате
@pytest.mark.parametrize('password', invalid.incorrect_passwords)
def test_reg_invalid_password_negative(browser, password):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_password, password)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == text_messages.wrong_password_message


# Тест регистрации нового пользователя c указанием номера телефона в неверном формате
@pytest.mark.parametrize('phone', invalid.incorrect_phones)
def test_reg_invalid_phone_negative(browser, phone):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_login, phone)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == text_messages.wrong_login_message


# Тест регистрации нового пользователя c указанием имени в неверном формате
@pytest.mark.parametrize('name', invalid.incorrect_names)
def test_reg_invalid_name_negative(browser, name):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.name, name)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == text_messages.wrong_name_message


# Тест регистрации нового пользователя c указанием фамилии в неверном формате
@pytest.mark.parametrize('surname', invalid.incorrect_surnames)
def test_reg_invalid_surname_negative(browser, surname):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.surname, surname)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == text_messages.wrong_surname_message


# Тест авторизации пользователя с валидными учетными данными
@pytest.mark.parametrize('login', valid.correct_logins)
def test_auth_user_with_valid_email_positive(browser, login):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, login)
    page.enter_data(AuthtorizationLocators.auth_pass, valid.correct_pass)
    page.click_enter_btn()


# Тест авторизации пользователя с невалидным адресом почты и валидным паролем
def test_auth_user_with_invalid_mail_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, invalid.incorrect_email)
    page.enter_data(AuthtorizationLocators.auth_pass, valid.correct_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthtorizationLocators.auth_error) == text_messages.wrong_login_or_pass_message or text_messages.wrong_capcha_message


# Тест авторизации пользователя с невалидным невалидным номером телефона и валидным паролем
def test_auth_user_with_invalid_phone_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, invalid.incorrect_phone)
    page.enter_data(AuthtorizationLocators.auth_pass, valid.correct_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthtorizationLocators.auth_error) == text_messages.wrong_login_or_pass_message or text_messages.wrong_capcha_message


# Тест авторизации пользователя с валидным логином и невалидным паролем
@pytest.mark.parametrize('login', valid.correct_logins)
def test_auth_user_with_invalid_pass_negative(browser, login):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, login)
    page.enter_data(AuthtorizationLocators.auth_pass, invalid.incorrect_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthtorizationLocators.auth_error) == text_messages.wrong_login_or_pass_message or text_messages.wrong_capcha_message


# Тест работоспособности ссылки на пользовательское соглашение и политику конфиденциальности
def test_agreement_link_positive(browser):
    page = AuthPage(browser)
    page.get(valid.agreement_url)
    assert page.get_text_from_element(AgrLocators.agr_title) == valid.agreement_title


# Тест авторизации пользователя при помощи учетной записи google с указанием невалидных учетных данных
def test_auth_with_google_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_google)
    page.enter_data(SocialLocators.google_login, invalid.incorrect_email)
    page.click_link(SocialLocators.google_submit_btn)
    assert page.get_text_from_element(SocialLocators.google_error_message) == text_messages.google_wrong_message
    assert 'accounts.google.com' in page.get_current_url()


# Тест авторизации пользователя при помощи учетной записи yandex с указанием невалидных учетных данных
def test_auth_with_yandex_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_yandex)
    page.enter_data(SocialLocators.yandex_login, invalid.incorrect_login_yandex)
    page.click_link(SocialLocators.yandex_submit_btn)
    assert page.get_text_from_element(SocialLocators.yandex_error_message) == text_messages.yandex_wrong_message
    assert 'passport.yandex.ru' in page.get_current_url()


# Тест авторизации пользователя при помощи учетной записи mail.ru с указанием невалидных учетных данных
def test_auth_with_mail_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_male)
    page.enter_data(SocialLocators.mail_login, invalid.incorrect_email)
    page.enter_data(SocialLocators.mail_pass, invalid.incorrect_pass)
    page.click_link(SocialLocators.mail_submit_btn)
    assert page.get_text_from_element(SocialLocators.mail_error_message) == text_messages.mail_wrong_message
    assert 'connect.mail.ru' in page.get_current_url()


# Тест авторизации пользователя при помощи учетной записи vk с указанием невалидных учетных данных
def test_auth_with_vk_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_vk)
    page.enter_data(SocialLocators.vk_login, invalid.incorrect_email)
    page.enter_data(SocialLocators.vk_pass, invalid.incorrect_pass)
    page.click_link(SocialLocators.vk_submit_btn)
    assert page.get_text_from_element(SocialLocators.vk_error_message) == text_messages.vk_wrong_message
    assert 'oauth.vk.com' in page.get_current_url()