from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

SEARCH_URL = "http://www.google.es"
MAX_WAIT_TIME = 10

class TestHabitissimo(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def search_on_google(self):
        self.driver.get( SEARCH_URL )
        search_input = self.driver.find_element_by_id("lst-ib")
        search_input.send_keys("habitissimo")
        search_input.submit()

    def wait_for_1st_google_result(self):
        wait = WebDriverWait(self.driver, MAX_WAIT_TIME)
        first_result = wait.until(
            expected_conditions.element_to_be_clickable( (By.CLASS_NAME, "g") )
        )
        return first_result

    def wait_for_redirect(self, url_to_wait_for):
        wait_for_redirect = WebDriverWait(self.driver, MAX_WAIT_TIME)
        wait_for_redirect.until(lambda driver: url_to_wait_for in driver.current_url)


    def test_habitissimo_is_first_result(self):
        self.search_on_google()

        first_result = self.wait_for_1st_google_result()
        first_result.find_element_by_tag_name("a").click()

        self.wait_for_redirect("http://www.habitissimo.es")
        self.assertIs(True, "habitissimo.es" in self.driver.current_url )

if __name__ == "__main__":
    unittest.main()
