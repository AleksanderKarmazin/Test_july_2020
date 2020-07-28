import time
from selenium import webdriver
import pytest
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from loginPage import LoginPage
from homePage import HomePage



@pytest.mark.usefixtures("driver_init")
class Test_Class_01():
    # ТС_1.1. Логин с корректным  ID пользователя  и корректным  паролем
    def test_TC_01(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.click_logout()


    # ТС_1.2. Логин с пустым  полем ID пользователя  и пустым полем  паролем
    def test_TC_02(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("")
        login.enter_password("")
        login.click_login()
        openElement = driver.find_element_by_css_selector("div.invalid-feedback")
        elementText = openElement.text
        Text = "Login is not given."
        assert Text == elementText
        openElement2 = driver.find_element_by_xpath("//form/div[2]/div")
        elementText2 = openElement2.text
        Text2 = "Password is not given."
        assert Text2 == elementText2


    # ТС_1.3. Логин с корректным ID пользователя  и не корректным паролем (5 символов)
    def test_TC_03(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("12345")
        login.click_login()
        openElement = driver.find_element_by_xpath("//form/div[2]/div")
        elementText = openElement.text
        Text = "The entered password must be not less than 6 symbols."
        assert Text == elementText

    # ТС_1.4. Логин с корректным ID пользователя  и не корректным паролем (6 символов)
    def test_TC_04(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123455")
        login.click_login()
        openElement = driver.find_element_by_xpath("//form/div/div")
        elementText = openElement.text
        Text = "Login or password is incorrect!"
        assert Text == elementText

    # ТС_1.5. Логин с корректным ID пользователя  и не корректным паролем (7 символов)
    def test_TC_05(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("1234567")
        login.click_login()
        openElement = driver.find_element_by_xpath("//form/div/div")
        elementText = openElement.text
        Text = "Login or password is incorrect!"
        assert Text == elementText

    # ТС_1.6. Логин с не  корректным ID пользователя  и  корректным паролем
    def test_TC_06(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.comm")
        login.enter_password("123456")
        login.click_login()
        openElement = driver.find_element_by_xpath("//form/div/div")
        elementText = openElement.text
        Text = "Login or password is incorrect!"
        assert Text == elementText

    # ТС_1.7. Логин с не  корректным ID пользователя  и  не корректным паролем (6 символов)
    def test_TC_07(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.comm")
        login.enter_password("123455")
        login.click_login()
        openElement = driver.find_element_by_xpath("//form/div/div")
        elementText = openElement.text
        Text = "Login or password is incorrect!"
        assert Text == elementText

    # ТС_2.1 Корректный номер телефона (Russia, номер   9181234567, Health Care)
    def test_TC_08(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("Russia")
        homepage.enter_phone("9181234567")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()


    # ТС_2.2. Повторный ввод корректного телефона без изменений информации (Russia, номер   9181234567, Health Care )
    def test_TC_09(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("Russia")
        homepage.enter_phone("9181234567")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()

    # 2.3. Повторный ввод корректных данных с изменениями дропдауна  Business segment
    def test_TC_10(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("Russia")
        homepage.enter_phone("9181234567")
        homepage.select_business_segment("Finance")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()

    # 2.4. Повторный ввод корректного телефона с изменениями дропдауна Country (United States , номер   2026794501, Health Care )
    def test_TC_11(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("United States")
        homepage.enter_phone_code("+1")
        homepage.enter_phone("2026794501")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()


    # 2.5. Пустое поле кода (USA , номер   2026794501)
    def test_TC_12(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("United States")
        homepage.enter_phone_code("")
        homepage.enter_phone("2026794501")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()

    # 2.6. Пустое поле телефон
    def test_TC_13(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("United States")
        homepage.enter_phone_code("+1")
        homepage.enter_phone("")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()

    # 2.7. Ввод номера телефона не корректного формата
    def test_TC_14(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("United States")
        homepage.enter_phone_code("+1")
        homepage.enter_phone("202 679 45 01")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        homepage.open_profile_menu()
        homepage.click_logout()

    # 2.8. Ввод не действительного номера телефона
    def test_TC_15(self):
        driver = self.driver
        driver.get("https://area.mtg-bi.com")
        login = LoginPage(driver)
        login.sign_in()
        login.enter_username("testcaseqa5@gmail.com")
        login.enter_password("123456")
        login.click_login()
        homepage = HomePage(driver)
        homepage.open_profile_menu()
        homepage.open_profile()
        homepage.select_country("United States")
        homepage.enter_phone_code("+1")
        homepage.enter_phone("956-42-84")
        homepage.select_business_segment("Health Care")
        homepage.click_update()
        time.sleep(10)
        homepage.open_profile_menu()
        homepage.click_logout()

