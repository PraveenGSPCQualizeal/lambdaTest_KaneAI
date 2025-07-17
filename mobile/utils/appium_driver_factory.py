from appium import webdriver

def get_android_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "platformVersion": "15",
        "app": "https://prod-mobile-artefacts.lambdatest.com/assets/docs/proverbial_android.apk",
        "automationName": "UiAutomator2"
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

def get_ios_driver():
    desired_caps = {
        "platformName": "iOS",
        "deviceName": "iPhone 16",
        "platformVersion": "18",
        "app": "https://prod-mobile-artefacts.lambdatest.com/assets/docs/proverbial_ios.ipa",
        "automationName": "XCUITest"
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
