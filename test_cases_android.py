import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

driver = None


def setup():
    global driver
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'emulator-5556'
    options.app_package = 'com.ixigo.train.ixitrain'
    options.app_activity = 'com.ixigo.train.ixitrain.TrainActivity'
    options.no_reset = True

    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

        # Navigate to the home screen
        driver.press_keycode(3)

        # Open the app drawer
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=800)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='ixigo trains']"))
        )

        # Click on the ixigo app icon
        ixigo_icon = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='ixigo trains']")
        ixigo_icon.click()

        # Wait until the app is launched
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
        )

    except Exception as e:
        logging.error(f"Error setting up Appium driver: {e}")
        raise


def teardown():
    global driver
    if driver:
        driver.quit()


if __name__ == "__main__":
    codeSnippet = """
def test_case_1():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']"))
        )
        assert driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Trains']").is_displayed()
        logging.info("Test Case 1 passed: Splash screen displayed correctly.")
    except Exception as e:
        logging.error(f"Test Case 1 failed: {e}")
        raise

test_case_1()
        """
    try:
        setup()
        exec(codeSnippet)
    except Exception as e:
        logging.error(f"Error during test execution: {e}")
    finally:
        teardown()
