import time
import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
edgeoptions = webdriver.EdgeOptions()
edgeoptions.add_experimental_option("detach", True)


@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome(options=options)
    elif browser == 'Edge':
        driver = webdriver.Edge(options=edgeoptions)
    else:
        print("Provide Valid Browser")
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--url") We can provide url also while running the test cases, make one more fixture to return
    # url and use  that in set up fixture

@pytest.fixture(scope="class", autouse = True)
def browser(request):
    return request.config.getoption("--browser")

