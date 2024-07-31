import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)


# class TestFlightBooking:
#     def setup(self):
#         # Set up the Appium options
#         options = UiAutomator2Options()
#         options.platform_name = 'Android'
#         options.device_name = 'emulator-5556'
#         options.app_package = 'com.ixigo.train.ixitrain'
#         options.app_activity = 'com.ixigo.train.ixitrain.TrainActivity'
#         options.no_reset = True

#         self.driver = None

#         try:
#             self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

#             # Navigate to the home screen
#             self.driver.press_keycode(3)

#             # Open the app drawer
#             self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=800)
#             WebDriverWait(self.driver, 30).until(
#                 EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='ixigo trains']"))
#             )

#             # Click on the ixigo app icon
#             ixigo_icon = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='ixigo trains']")
#             ixigo_icon.click()

#             # Wait until the app is launched
#             WebDriverWait(self.driver, 30).until(
#                 EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
#             )

#         except Exception as e:
#             logging.error(f"Error setting up Appium driver: {e}")
#             raise

#     def teardown(self):
#         if self.driver:
#             self.driver.quit()

    # def test_case_2(self):
    #     """
    #     Verify navigation to the home screen after the splash screen.
    #     """
    #     try:
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
    #         )
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()
    #         logging.info("Test Case 2 passed: Home screen loaded successfully.")
    #     except Exception as e:
    #         logging.error(f"Test Case 2 failed: {e}")
    #         raise

    # def test_case_3(self):
    #     """
    #     Verify the selection of the "PNR Status" option from the home screen.
    #     """
    #     try:
    #         pnr_status_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PNR Status']")
    #         pnr_status_button.click()

    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']"))
    #         )
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
    #         logging.info("Test Case 3 passed: Navigated to PNR status screen.")
    #     except Exception as e:
    #         logging.error(f"Test Case 3 failed: {e}")
    #         raise

    # def test_case_4(self):
    #     """
    #     Verify the input field for entering the PNR number on the PNR status screen.
    #     """
    #     try:
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']").is_displayed()
    #         logging.info("Test Case 4 passed: Input field for PNR number is displayed.")
    #     except Exception as e:
    #         logging.error(f"Test Case 4 failed: {e}")
    #         raise

    # def test_case_5(self):
    #     """
    #     Verify the functionality of the numeric keypad for entering the PNR number.
    #     """
    #     try:
    #         pnr_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
    #         pnr_input.click()
    #         pnr_input.send_keys("1234567890")
    #         assert pnr_input.text == "1234567890"
    #         logging.info("Test Case 5 passed: PNR number entered correctly.")
    #     except Exception as e:
    #         logging.error(f"Test Case 5 failed: {e}")
    #         raise

    # def test_case_6(self):
    #     """
    #     Verify the "Search" button functionality after entering a PNR number.
    #     """
    #     try:
    #         # search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
    #         search_button = self.driver.find_element(AppiumBy.ID, "com.ixigo.train.ixitrain:id/btn_search")
    #         search_button.click()

    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'not valid')]"))
    #         )
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'not valid')]").is_displayed()
    #         logging.info("Test Case 6 passed: Search functionality works correctly for invalid PNR.")
    #     except Exception as e:
    #         logging.error(f"Test Case 6 failed: {e}")
    #         raise

    # def test_case_7(self):
    #     """
    #     Verify the error message when an invalid PNR number is entered.
    #     """
    #     try:
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'PNR No. is not valid')]").is_displayed()
    #         logging.info("Test Case 7 passed: Error message displayed for invalid PNR.")
    #     except Exception as e:
    #         logging.error(f"Test Case 7 failed: {e}")
    #         raise

    # def test_case_8(self):
    #     """
    #     Verify the option to re-enter the PNR number after an invalid entry.
    #     """
    #     try:
    #         pnr_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
    #         assert pnr_input.is_displayed()
    #         pnr_input.clear()  # Clear the input field for re-entry
    #         logging.info("Test Case 8 passed: Input field cleared for re-entry.")
    #     except Exception as e:
    #         logging.error(f"Test Case 8 failed: {e}")
    #         raise

    # def test_case_9(self):
    #     """
    #     Verify the retrieval of train details for a valid PNR number.
    #     """
    #     try:
    #         pnr_input = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter your 10 digit PNR']")
    #         pnr_input.send_keys("VALID_PNR_NUMBER")  # Replace with a valid PNR number
    #         # search_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Search']")
    #         search_button = self.driver.find_element(AppiumBy.ID, "com.ixigo.train.ixitrain:id/btn_search")
    #         search_button.click()

    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='11072 Kamayani Exp']"))
    #         )
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='11072 Kamayani Exp']").is_displayed()
    #         logging.info("Test Case 9 passed: Train details retrieved successfully.")
    #     except Exception as e:
    #         logging.error(f"Test Case 9 failed: {e}")
    #         raise

    # def test_case_10(self):
    #     """
    #     Verify the options available after retrieving train details.
    #     """
    #     try:
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Cancel Ticket']").is_displayed()
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Download Ticket']").is_displayed()
    #         logging.info("Test Case 10 passed: Options for further actions are available.")
    #     except Exception as e:
    #         logging.error(f"Test Case 10 failed: {e}")
    #         raise

    # def test_case_11(self):
    #     """
    #     Verify navigation back to the home screen from the train details screen.
    #     """
    #     try:
    #         back_button = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.ixigo.train.ixitrain:id/iv_toolbar_back']")
    #         back_button.click()

    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
    #         )
    #         assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()
    #         logging.info("Test Case 11 passed: Successfully navigated back to home screen.")
    #     except Exception as e:
    #         logging.error(f"Test Case 11 failed: {e}")
    #         raise


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
        \"\"\"
        Verify that the splash screen is displayed correctly upon launching the app.
        \"\"\"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
            )
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()
            logging.info("Test Case 1 passed: Splash screen displayed correctly.")
        except Exception as e:
            logging.error(f"Test Case 1 failed: {e}")
            raise

test = TestFlightBooking()
test.setup()
try:
    test.test_case_1()
finally:
    test.teardown()
    """

    try:
        # Use eval to execute the code snippet
        eval(code_snippet)
    except Exception as e:
        logging.error(f"Error during test execution: {e}")


    # try:
    #     test.setup()
    #     try:
    #         # test.test_case_1()
    #         # test.test_case_2()
    #         # test.test_case_3()
    #         # test.test_case_4()
    #         # test.test_case_5()
    #         # test.test_case_6()
    #         # test.test_case_7()
    #         # test.test_case_8()
    #         # test.test_case_9()
    #         # test.test_case_10()
    #         # test.test_case_11()
    #     finally:
    #         test.teardown()
    # except Exception as e:
    #     logging.error(f"Error during test execution: {e}")
