import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            option = webdriver.ChromeOptions()
            option.add_experimental_option("w3c", False)
            self._driver = webdriver.Chrome("/Users/huyuqi/software/chromedriver", options=option)
            # env = os.getenv("browser")
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
            self._cookie_login()
        else:
            self._driver = base_driver
        # self.vars = {}

    def _cookie_login(self):
        self._driver.get("https://work.weixin.qq.com")
        with open("/Users/huyuqi/PycharmProjects/webseleniumtest/test_po/page/cookie.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def find(self, by, value):
        return self._driver.find_element(by=by, value=value)

    # def teardown(self):
    #     pass
    #     # self.driver.quit()
