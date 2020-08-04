import pytest
from selenium import webdriver




@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Firefox(executable_path='C:/Tools/geckodriver.exe')
    request.cls.driver = driver
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield
    driver.close()
    print("Browser closed")



