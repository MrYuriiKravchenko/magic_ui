from selenium import webdriver
import pytest
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

