from selenium.webdriver.common.by import By
from behave import given, when, then


SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


@then('verify sign in page opens')
def verify_signin_opens(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in header but got (actual_text)'
    assert context.driver.find_element(*EMAIL).is_displayed(), 'Email field not shown'
