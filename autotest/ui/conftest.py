import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from autotest.auxiliary import logout_from_disk_page


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    opts = webdriver.ChromeOptions()
    # opts.add_argument('-headless')
    opts.add_argument('window-size=1920x1480')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    yield driver
    print("\nLogOut..")
    logout_from_disk_page(driver)
    print("\nQuit browser..")
    driver.quit()
