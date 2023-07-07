from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULT = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, '.a-size-base-plus.a-color-base.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, "[data-image-latency='s-product-image']")


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Verify that every product has a names and image')
def verif_product_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULT)
    print(all_products)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Title should not be blank'
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Image is not found'
