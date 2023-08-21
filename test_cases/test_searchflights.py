import time
import pytest
from selenium.webdriver.common.by import By

from pages.search_flights_results_page import ResultPage
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.rp = ResultPage(self.driver)
        self.ut = Utils()

    def test_search_flights(self):
        self.lp.searchFlights('New Delhi', 'New York', '22/08/2023')
        self.lp.scroll_down()
        self.rp.filter_flights('1 Stop')
        all_stops1 = self.rp.get_flight_filter_result()
        self.ut.assrtListItemText(all_stops1, "1 Stop")
'''
    def test_search_flights_2(self):
        self.lp.searchFlights('New Delhi', 'New York', '22/08/2023')
        self.lp.scroll_down()
        self.rp.filter_flights('2 Stop')
        all_stops1 = self.rp.get_flight_filter_result()
        self.ut.assrtListItemText(all_stops1, "2 Stops ")
        '''
