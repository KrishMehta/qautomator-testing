from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
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
        Verify the app launches and displays the home screen with the app logo.
        Steps:
            1. Launch the application.
            2. Observe the home screen.
        Expected Outcome: The app logo is prominently displayed, and various app icons are visible on the home screen.
        """
        # Wait for the home screen to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "android.widget.FrameLayout[@resource-id='com.ixigo.train.ixitrain:id/action_bar_root']"))
        )
        app_logo = self.driver.find_element(AppiumBy.XPATH, "android.widget.ImageView[@resource-id='com.ixigo.train.ixitrain:id/iv_logo']")
        assert app_logo.is_displayed(), "App logo is not displayed on the home screen."

    def test_case_2(self):
        """
        Verify the splash screen is displayed during app loading.
        Steps:
            1. Launch the application.
            2. Observe the splash screen.
        Expected Outcome: The splash screen with the app logo is displayed until the app is fully loaded.
        """
        # Wait for the splash screen to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "android.widget.ImageView[@resource-id='com.ixigo.train.ixitrain:id/iv_logo']"))
        )
        splash_screen = self.driver.find_element(AppiumBy.XPATH, "android.widget.ImageView[@resource-id='com.ixigo.train.ixitrain:id/iv_logo']")
        assert splash_screen.is_displayed(), "Splash screen is not displayed."

    def test_case_3(self):
        """
        Verify the login screen is displayed with login options.
        Steps:
            1. After the splash screen, observe the login screen.
        Expected Outcome: The login screen displays options for logging in via Facebook, Google, and a button to continue as a guest.
        """
        # Wait for the login screen to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "android.widget.Button[@text='Continue as Guest']"))
        )
        guest_button = self.driver.find_element(AppiumBy.XPATH, "android.widget.Button[@text='Continue as Guest']")
        assert guest_button.is_displayed(), "Login screen is not displayed with login options."

    def test_case_4(self):
        """
        Verify the search bar functionality on the main screen.
        Steps:
            1. Log in to the app.
            2. Observe the main screen.
            3. Click on the search bar labeled "Search for destinations..."
        Expected Outcome: The search bar is active, and a keyboard appears for text input.
        """
        self.test_case_3()  # Ensure we are on the login screen
        # Simulate login (assuming login is successful)
        self.driver.find_element(AppiumBy.XPATH, "android.widget.Button[@text='Continue as Guest']").click()

        # Wait for the main screen to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "android.widget.EditText[@text='Search for destinations...']"))
        )
        search_bar = self.driver.find_element(AppiumBy.XPATH, "android.widget.EditText[@text='Search for destinations...']")
        search_bar.click()
        assert search_bar.is_displayed(), "Search bar is not displayed on the main screen."

    def test_case_5(self):
        """
        Verify the Preferred Section is displayed on the main screen.
        Steps:
            1. Log in to the app.
            2. Observe the main screen.
        Expected Outcome: The Preferred Section is visible, showing frequently searched destinations or saved trips.
        """
        self.test_case_4()  # Ensure we are on the main screen
        preferred_section = self.driver.find_element(AppiumBy.XPATH, "android.widget.TextView[@text='Preferred Section']")
        assert preferred_section.is_displayed(), "Preferred Section is not displayed on the main screen."

    def test_case_6(self):
        """
        Verify the selection of the "Flights" option.
        Steps:
            1. Log in to the app.
            2. On the main screen, select the "Flights" option.
        Expected Outcome: The app transitions to the flight search options screen.
        """
        self.test_case_4()  # Ensure we are on the main screen
        flights_option = self.driver.find_element(AppiumBy.XPATH, "android.widget.TextView[@text='Flights']")
        flights_option.click()

        # Wait for the flight search options screen to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "android.widget.TextView[@text='Search Flights']"))
        )
        assert self.driver.find_element(AppiumBy.XPATH, "android.widget.TextView[@text='Search Flights']").is_displayed(), "Flight search options screen is not displayed."


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
        finally:
            test.teardown()
    except Exception as e:
        print(f"Error during test execution: {e}")