from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
CART_BTN = (By.CSS_SELECTOR, '.nav-cart-icon.nav-sprite')
POPUP_SIGNIN_BTN =(By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.driver.find_element(*SEARCH_FILED).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('click cart')
def click_cart(context):
    context.driver.find_element(*CART_BTN).click()


@when('Verify Orders btn present')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN)


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    ).click()


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))

    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) # 36
    print(type(links_count))

    # 36 == 36
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'