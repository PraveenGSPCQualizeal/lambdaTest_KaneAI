from mobile.utils.appium_driver_factory import get_android_driver
import time

def test_android_tap_button():
    driver = get_android_driver()
    driver.implicitly_wait(10)

    color_button = driver.find_element_by_accessibility_id("color")
    color_button.click()
    time.sleep(2)

    driver.quit()
