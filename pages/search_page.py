from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    PRODUCT_RESULTS = (By.CLASS_NAME, "product-thumb")

    def search_product(self, keyword):
        search = self.driver.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(keyword)
        search.send_keys(Keys.RETURN)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_RESULTS))
