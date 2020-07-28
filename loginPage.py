
class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.sign_in_button_xpath = "//a[contains(text(),'Sign IN')]"
        self.username_text_id = "signin-login"
        self.password_text_id = "signin-pass"
        self.login_button_xpath = "(//button[@type='button'])[3]"

    def sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_id).clear()
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_text_id).clear()
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
