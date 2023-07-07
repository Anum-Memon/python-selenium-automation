from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


DOG_IMG = (By.CSS_SELECTOR, 'img#d')


@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:',context.original_window)
    print('All window:', context.driver.window_handles)


@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('after window opened, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[1])


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))


@then('Close Blog')
def close_blog(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('after blog closed, all windows:', all_windows)


@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)