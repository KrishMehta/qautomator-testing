from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            self.driver = webdriver.Remote('http://localhost:4723/session', options=options)
        except Exception as e:
            print(f"Error setting up Appium driver: {e}")
            raise

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def test_case_1(self):
        """
        Verify that the app launches and displays the home screen with app icons.
        """
        # Wait for the Home screen to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
        )
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()

    def test_case_2(self):
        """
        Verify that selecting the train status application transitions to the loading screen.
        """
        # Select the application for checking train status
        train_status_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PNR Status']")
        train_status_button.click()

        # Wait for the loading screen
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']"))
        )
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()

    def test_case_3(self):
        """
        Verify that the PNR status screen displays the correct title and input field.
        """
        self.test_case_2()  # Navigate to PNR Status screen

        # Verify elements on the PNR status screen
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Running Status']").is_displayed()
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']").is_displayed()

    def test_case_4(self):
        """
        Verify that entering a PNR number and clicking "Search" retains the input.
        """
        self.test_case_3()  # Navigate to PNR Status screen

        # Enter a PNR number
        pnr_input_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
        pnr_input_field.send_keys("1234567890")

        # Click the "Search" button
        search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
        search_button.click()

        # Verify the input is retained
        assert pnr_input_field.get_attribute('text').strip() == "1234567890"

    def test_case_5(self):
        """
        Verify that the app prompts for notification permissions after searching with a valid PNR.
        """
        self.test_case_4()  # Enter a valid PNR number

        # Wait for the notification prompt
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Add Manager')]"))
        )
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Add Manager')]").is_displayed()

    def test_case_6(self):
        """
        Verify that searching with an invalid PNR displays an error message.
        """
        self.test_case_3()  # Navigate to PNR Status screen

        # Enter an invalid PNR number
        pnr_input_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
        pnr_input_field.send_keys("12345")

        # Click the "Search" button
        search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
        search_button.click()

        # Wait for the error message
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='PNR No. is not valid']"))
        )
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PNR No. is not valid']").is_displayed()

    def test_case_7(self):
        """
        Verify that acknowledging the invalid PNR message returns the user to the previous screen.
        """
        self.test_case_6()  # Trigger invalid PNR message

        # Click "OK" on the alert
        ok_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='OK']")
        ok_button.click()

        # Verify the user is returned to the PNR status screen
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()

    def test_case_8(self):
        """
        Verify that the user can re-enter a valid PNR number after an invalid entry.
        """
        self.test_case_7()  # Return to PNR Status screen

        # Enter a valid PNR number
        pnr_input_field = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
        pnr_input_field.send_keys("1234567890")

        # Click the "Search" button
        search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
        search_button.click()

        # Verify the input is processed
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Add Manager')]").is_displayed()

    def test_case_9(self):
        """
        Verify that the user can navigate back to the home screen from the PNR status screen.
        """
        self.test_case_3()  # Navigate to PNR Status screen

        # Click back button
        back_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.ixigo.train.ixitrain:id/iv_toolbar_back']")
        back_button.click()

        # Verify the home screen is displayed
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()

    def test_case_10(self):
        """
        Verify the presence of static UI elements on the PNR status screen.
        """
        self.test_case_3()  # Navigate to PNR Status screen

        # Verify static UI elements
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Running Status']").is_displayed()
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']").is_displayed()


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
        print(f"Error during test execution: {e}")