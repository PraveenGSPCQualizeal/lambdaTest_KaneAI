from selenium import webdriver
import yaml

def load_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

def get_driver():
    config = load_config()
    browser = config["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
