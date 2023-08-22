import logging
import time

from selenium.webdriver.common.by import By
from utilities.utils import Utils
from base.base_driver import BaseDriver


class ResultPage(BaseDriver):
    log = Utils.custom_logger(loglevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    filter_by_1 = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    filter_by_2 = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    filter_by_3 = "//p[@class='font-lightgrey bold'][normalize-space()='3']"
    filter_results = "//span[contains(text() ,'1 Stop') or contains(text(), '2 Stops') or contains(text(), '3 Stops')]"

    def get_filter_by_1_stop_icon(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.filter_by_1)

    def get_filter_by_2_stop_icon(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.filter_by_2)

    def get_filter_by_3_stop_icon(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.filter_by_3)

    def get_flight_filter_result(self):
        return self.wait_for_all_element_to_be_located(By.XPATH, self.filter_results)

    def filter_flights(self, num_of_stops):
        if num_of_stops == '1 Stop':
            self.get_filter_by_1_stop_icon().click()
            self.log.info("Selected flight with 1 stop")
            time.sleep(2)
        elif num_of_stops == '2 Stops':
            self.get_filter_by_2_stop_icon().click()
            self.log.info("Selected flight with 2 stops")
            time.sleep(2)
        elif num_of_stops == '3 Stops':
            self.get_filter_by_3_stop_icon().click()
            self.log.info("Selected flight with 3 stops")
            time.sleep(2)
        else:
            self.log.info("Please enter valid option")




