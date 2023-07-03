from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then
from time import sleep


HEADER_LINKS = (By.CSS_SELECTOR, "#zg_header a")


@given('open amazon BestSellers page')
def open_amazon_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(5)


@then('Verify there are 5 links')
def verify_link_count(context):
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(HEADER_LINKS))

    links_count = len(context.driver.find_elements(*HEADER_LINKS))
    page_html = context.driver.page_source

    assert links_count == 5, f'Expected {5} links, but got {links_count}\n\nPage HTML:\n{page_html}'
    sleep(10)
