import time
import pytest
import softest as softest
from selenium.webdriver.common.by import By

from pages.search_flights_results_page import ResultPage
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.rp = ResultPage(self.driver)
        self.ut = Utils()

    # @data(("New Delhi", "JFK", "25/08/2023", "1 Stop"), ("BOM", "JFK", "31/08/2023", "2 Stops"))
    # @unpack
    @file_data("../test_data/testdata.json")
    def test_search_flights(self, goingfrom, goingto, date, stops):
        self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.scroll_down()
        self.rp.filter_flights(stops)
        all_stops1 = self.rp.get_flight_filter_result()
        self.ut.assrtListItemText(all_stops1, "1 Stop")

    # def test_search_flights_2(self):
    #     self.lp.searchFlights('New Delhi', 'New York', '26/08/2023')
    #     self.lp.scroll_down()
    #     self.rp.filter_flights('2 Stops')
    #     all_stops1 = self.rp.get_flight_filter_result()
    #     self.ut.assrtListItemText(all_stops1, "2 Stops ")
