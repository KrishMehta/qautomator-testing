import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":

    # Define the code snippet as a string
    code_snippet = """
class TestFlightBooking:
    def setup(self):
        # Set up the Appium options
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5556'
        options.app_package = 'com.ixigo.train.ixitrain'
        options.app_activity = 'com.ixigo.train.ixitrain.TrainActivity'
        options.no_reset = True

        self.driver = None

        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

            # Navigate to the home screen
            self.driver.press_keycode(3)

            # Open the app drawer
            self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=800)
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='ixigo trains']"))
            )

            # Click on the ixigo app icon
            ixigo_icon = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='ixigo trains']")
            ixigo_icon.click()

            # Wait until the app is launched
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
            )

        except Exception as e:
            logging.error(f"Error setting up Appium driver: {e}")
            raise

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def test_case_1(self):
        \"""
        Verify that the splash screen is displayed correctly upon launching the app.
        \"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
            )
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()
            logging.info("Test Case 1 passed: Splash screen displayed correctly.")
        except Exception as e:
            logging.error(f"Test Case 1 failed: {e}")
            raise


if __name__ == "__main__":
    test = TestFlightBooking()
    test.setup()
    try:
        test.test_case_1()
    finally:
        test.teardown()
    """

    try:
        # Use exec to execute the code snippet
        exec(code_snippet)
    except Exception as e:
        logging.error(f"Error during test execution: {e}")