from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('click orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('click cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()
