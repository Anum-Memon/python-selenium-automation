from selenium.webdriver.common.by import By
from behave import given, when, then


@then('verify Your Amazon Cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty').text
    assert actual_text == 'Your Amazon Cart is empty', f'Expected Your Amazon Cart is empty header but got (actual_text)'

