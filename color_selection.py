from selenium.webdriver.common.by import By
from behave import *
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product B07BJKRR25 page')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')

@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = context.driver.find_element(*COLOR_OPTIONS)
    for color in expected_colors:
        color.click()
    current_color = context.driver.find_element(*CURRENT_COLOR).text
    print(current_color)
