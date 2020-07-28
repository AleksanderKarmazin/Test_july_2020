from selenium.webdriver.support.ui import Select


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.profile_menu_css = "span.userName"
        self.logout_button_xpath = "//a[5]"
        self.profile_xpath = "//li[2]/div/div/a"
        self.country_by_id = "profile-country"
        self.phone_by_id = "profile-phone"
        self.business_segment_by_id = "profile-busseg"
        self.update_button_xpath = "//div[7]/button"
        self.phone_code_xpath = "//input[@type='tel']"


    def open_profile_menu(self):
        self.driver.find_element_by_css_selector(self.profile_menu_css).click()

    def open_profile(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()

    def select_country(self, country):
        self.driver.find_element_by_id(self.country_by_id).click()
        Select(self.driver.find_element_by_id(self.country_by_id)).select_by_visible_text(country)
        self.driver.find_element_by_id(self.country_by_id).click()

    def enter_phone_code(self, phone_code):
        self.driver.find_element_by_xpath(self.phone_code_xpath).clear()
        self.driver.find_element_by_xpath(self.phone_code_xpath).send_keys(phone_code)


    def enter_phone(self, phone):
        self.driver.find_element_by_id(self.phone_by_id).clear()
        self.driver.find_element_by_id(self.phone_by_id).send_keys(phone)


    def select_business_segment(self, business_segment):
        self.driver.find_element_by_id(self.business_segment_by_id).click()
        Select(self.driver.find_element_by_id(self.business_segment_by_id)).select_by_visible_text(business_segment)
        self.driver.find_element_by_id(self.business_segment_by_id).click()

    def click_update(self):
        self.driver.find_element_by_xpath(self.update_button_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

