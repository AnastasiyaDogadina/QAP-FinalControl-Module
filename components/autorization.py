from components.base import BasePage
from locators import AuthtorizationLocators, RegistrationLocators, PasswordRecoveryLocators


class AuthPage(BasePage):

    def enter_data(self, locator, text):
        input_field = self.find_element(locator)
        input_field.click()
        input_field.send_keys(text)
        return input_field

    def click_enter_btn(self):
        return self.find_element(AuthtorizationLocators.btn_enter).click()

    def click_reg_btn(self):
        return self.find_element(RegistrationLocators.reg_btn).click()

    def click_continue_btn(self):
        return self.find_element(PasswordRecoveryLocators.pass_btn).click()

    def click_link(self, locator: object) -> object:
        return self.find_element(locator).click()