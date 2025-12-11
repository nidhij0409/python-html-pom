from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.common.exceptions import NoSuchElementException

import os
import random
import time
import pytest
import re

_driver = None

def get_driver():
    """Get the existing driver instance or return None"""
    global _driver
    return _driver

def create_driver():
    global _driver
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    return _driver