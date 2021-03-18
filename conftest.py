from selenium import webdriver
import pytest

import json
import os.path


def load_config(file_path):
    config_path = os.path.join(os.path.dirname
                               (os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target


def api_user_config_data():
    config_data = load_config("recourses/variables/user_api_data.json")
    return config_data['user_name'], \
           config_data['password'], config_data['new_user_name']


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def user_change_config_data():
    config_data = load_config("recourses/variables/user_change_data.json")
    return config_data['email'], config_data['passwd'], \
           config_data['new_first_name'], config_data['new_last_name']
