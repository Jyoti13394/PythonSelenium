import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    '''def handle_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()'''

    def scroll_down(self):
        """A method for scrolling the page."""

        # Get scroll height.
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load the page.
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

            last_height = new_height

    def handle_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def wait_for_all_element_to_be_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(expected_conditions.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.presence_of_element_located((locator_type, locator)))
        return element
