import time

import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()
