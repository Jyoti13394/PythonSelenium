import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    depart_from_field = 'BE_flight_origin_city'
    depart_to_field= 'BE_flight_arrival_city'
    depart_to_search_result= "//div[@class= 'viewport']/div/div/li"
    select_date_field = "BE_flight_origin_date"
    search_button = "//input[@value = 'Search Flights']"

    def getDepartfromField(self):
        return self.wait_element_to_be_clickable(By.ID, self.depart_from_field)

    def getDeparttoField(self):
        return self.wait_until_presence_of_element_located(By.ID, self.depart_to_field)

    def searchresults(self):
        return self.wait_for_all_element_to_be_located(By.XPATH, self.depart_to_search_result)

    def getDateField(self):
        return self.wait_element_to_be_clickable(By.ID, self.select_date_field)

    def getSearchbutton(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.search_button)

    def enterDepartFromLocation(self, departlocation):
        self.getDepartfromField().click()
        time.sleep(2)
        self.getDepartfromField().send_keys(departlocation)
        self.getDepartfromField().send_keys(Keys.ENTER)

    def enterDeparttoField(self, arrival_location):
        self.getDeparttoField().click()
        time.sleep(2)
        self.getDeparttoField().send_keys(arrival_location)
        time.sleep(3)
        search_results = self.searchresults()

        for item in search_results:
            print(item.text)
            if "New York (JFK)" in item.text:
                item.click()
                break

    def enterDate(self, depart_date):
        self.getDateField().click()
        all_dates = self.wait_for_all_element_to_be_located(By.XPATH,
                                                            "//table[@class = 'days-head day-container-table']/tbody[@class = 'BE_flight_origin_date']/tr/td[@data-date != '']")
        for date in all_dates:
            if date.get_attribute("data-date") == depart_date:
                date.click()
                time.sleep(2)
                break

    def clicksearchflightbutton(self):
        self.getSearchbutton().click()
        time.sleep(3)

    def searchFlights(self, departlocation, arrival_location, depart_date):
        self.enterDepartFromLocation(departlocation)
        self.enterDeparttoField(arrival_location)
        self.enterDate(depart_date)
        self.clicksearchflightbutton()


