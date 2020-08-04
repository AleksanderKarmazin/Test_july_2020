from BaseApp import BasePage
from selenium.webdriver.common.by import By

class Locators:
    sign_in_button_xpath = (By.XPATH, "//a[contains(text(),'Sign IN')]")
    username_text_id = (By.ID, "signin-login")
    password_text_id = (By.ID, "signin-pass")
    login_button_xpath = (By.XPATH, "(//button[@type='button'])[3]")

class LoginPage(BasePage):
        # self.sign_in_button_xpath = "//a[contains(text(),'Sign IN')]"
        # self.username_text_id = "signin-login"
        # self.password_text_id = "signin-pass"
        # self.login_button_xpath = "(//button[@type='button'])[3]"

    def sign_in(self):
        sign_in_button = self.find_element(Locators.sign_in_button_xpath)
        sign_in_button.click()
        return sign_in_button


        # self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()

    def enter_username(self, username):
        username_field = self.find_element(Locators.username_text_id)
        username_field.clear()
        username_field.send_keys(username)
        return username_field

        # self.driver.find_element_by_id(self.username_text_id).clear()
        # self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def enter_password(self, password):
        password_field = self.find_element(Locators.password_text_id)
        password_field.clear()
        password_field.send_keys(password)
        return password_field


        # self.driver.find_element_by_id(self.password_text_id).clear()
        # self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def click_login(self):
        click_login = self.find_element(Locators.login_button_xpath)
        click_login.click()
        return click_login


        # self.driver.find_element_by_xpath(self.login_button_xpath).click()
