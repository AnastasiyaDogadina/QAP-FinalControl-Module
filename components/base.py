from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from name_keys import BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get(self, url):
        return self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        try:
            text = str(element.text)
            return text
        except Exception as e:
            print('Error: {0}'.format(e))
            return None

