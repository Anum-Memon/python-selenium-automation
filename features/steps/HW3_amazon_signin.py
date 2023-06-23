from selenium.webdriver.common.by import By
from behave import given, when, then


@then('verify sign in page opens')
def verify_signin_opens(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == 'Sign in', f'Expected Sign in header but got (actual_text)'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'
