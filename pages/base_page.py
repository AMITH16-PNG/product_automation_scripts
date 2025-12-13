from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Find element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        """Find clickable element with explicit wait"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """Click on an element"""
        element = self.find_clickable_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Enter text into an input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from an element"""
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, text, timeout=10):
        """Wait for URL to contain specific text"""
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
