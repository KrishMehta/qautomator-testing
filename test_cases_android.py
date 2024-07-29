import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

class TestFlightBooking:
    def setup(self):
        # Set up the Appium options
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.app_package = 'com.krishvmehta.application'
        options.app_activity = 'MainActivity'
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
        """
        Verify that the app launches and displays the home screen with app icons.
        """
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
            )
            element = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']")
            assert element.is_displayed()
            logging.info("Test Case 1 passed: Home screen loaded successfully")
        except Exception as e:
            logging.error(f"Test Case 1 failed: {e}")
            raise

    def test_case_2(self):
        """
        Verify that selecting the train status application transitions to the loading screen.
        """
        try:
            train_status_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PNR Status']")
            train_status_button.click()

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']"))
            )
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
            logging.info("Test Case 2 passed: Train status application loaded successfully")
        except Exception as e:
            logging.error(f"Test Case 2 failed: {e}")
            raise

    def test_case_3(self):
        """
        Verify that the PNR status screen displays the correct title and input field.
        """
        self.test_case_2()

        try:
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Running Status']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']").is_displayed()
            logging.info("Test Case 3 passed: PNR status screen displays correct elements")
        except Exception as e:
            logging.error(f"Test Case 3 failed: {e}")
            raise

    def test_case_4(self):
        """
        Verify that entering a PNR number and clicking "Search" retains the input.
        """
        self.test_case_3()

        try:
            pnr_input_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
            pnr_input_field.send_keys("1234567890")

            search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
            search_button.click()

            assert pnr_input_field.get_attribute('text').strip() == "1234567890"
            logging.info("Test Case 4 passed: PNR input is retained after searching")
        except Exception as e:
            logging.error(f"Test Case 4 failed: {e}")
            raise

    def test_case_5(self):
        """
        Verify that the app prompts for notification permissions after searching with a valid PNR.
        """
        self.test_case_4()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Add Manager')]"))
            )
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Add Manager')]").is_displayed()
            logging.info("Test Case 5 passed: Notification prompt displayed after valid PNR search")
        except Exception as e:
            logging.error(f"Test Case 5 failed: {e}")
            raise

    def test_case_6(self):
        """
        Verify that searching with an invalid PNR displays an error message.
        """
        self.test_case_3()

        try:
            pnr_input_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
            pnr_input_field.send_keys("12345")

            search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
            search_button.click()

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='PNR No. is not valid']"))
            )
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PNR No. is not valid']").is_displayed()
            logging.info("Test Case 6 passed: Error message displayed for invalid PNR")
        except Exception as e:
            logging.error(f"Test Case 6 failed: {e}")
            raise

    def test_case_7(self):
        """
        Verify that acknowledging the invalid PNR message returns the user to the previous screen.
        """
        self.test_case_6()

        try:
            ok_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='OK']")
            ok_button.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
            logging.info("Test Case 7 passed: User returned to PNR status screen after invalid PNR")
        except Exception as e:
            logging.error(f"Test Case 7 failed: {e}")
            raise

    def test_case_8(self):
        """
        Verify that the user can re-enter a valid PNR number after an invalid entry.
        """
        self.test_case_7()

        try:
            pnr_input_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
            pnr_input_field.send_keys("1234567890")

            search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
            search_button.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Add Manager')]").is_displayed()
            logging.info("Test Case 8 passed: User can re-enter valid PNR after invalid entry")
        except Exception as e:
            logging.error(f"Test Case 8 failed: {e}")
            raise

    def test_case_9(self):
        """
        Verify that the user can navigate back to the home screen from the PNR status screen.
        """
        self.test_case_3()

        try:
            back_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.ixigo.train.ixitrain:id/iv_toolbar_back']")
            back_button.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()
            logging.info("Test Case 9 passed: User navigated back to home screen from PNR status screen")
        except Exception as e:
            logging.error(f"Test Case 9 failed: {e}")
            raise

    def test_case_10(self):
        """
        Verify the presence of static UI elements on the PNR status screen.
        """
        self.test_case_3()

        try:
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Running Status']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']").is_displayed()
            logging.info("Test Case 10 passed: Static UI elements are present on the PNR status screen")
        except Exception as e:
            logging.error(f"Test Case 10 failed: {e}")
            raise


if __name__ == "__main__":
    test = TestFlightBooking()
    try:
        test.setup()
        try:
            test.test_case_1()
            test.test_case_2()
            test.test_case_3()
            test.test_case_4()
            test.test_case_5()
            test.test_case_6()
            test.test_case_7()
            test.test_case_8()
            test.test_case_9()
            test.test_case_10()
        finally:
            test.teardown()
    except Exception as e:
        logging.error(f"Error during test execution: {e}")
