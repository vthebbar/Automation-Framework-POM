import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def driver_setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        print("Launching Chrome browser")

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        print("Launching Firefox browser")

    elif browser == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
        driver.maximize_window()
        print("Launching IE browser")

    else:
        driver = webdriver.Edge()
        driver.maximize_window()
        print("Launching MS Egde (Default) browser")

    return driver


"""This method will get value from command line Interface (CLI)/hook/terminal"""

def pytest_addoption(parser):   # This method will get value from command line Interface (CLI)/hook/terminal
    parser.addoption("--browser")

"""This will return browser value to set up method"""

@pytest.fixture()
def browser(request):   # This will return browser value to set up method
    return request.config.getoption("--browser")


""" Customize html report  """
"""  Hook for adding environment info to HTML report """

def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart Demo'
    config._metadata['Tested by'] = 'Vishwa'

# Hook for delete/modify environment info to HTML file
@pytest.mark.optioalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
