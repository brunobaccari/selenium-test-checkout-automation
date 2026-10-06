import logging
from decimal import Decimal
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import site, user_name, password, first_name, last_name, postalcode, headless


def test_checkout():
    output = Path('results')
    output.mkdir(exist_ok=True)
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--window-size=1440,1000')
    options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'profile.password_manager_leak_detection': False,
    })
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    wait = WebDriverWait(driver, 15)

    def element(selector):
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def click(selector):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()

    try:
        driver.get(site)
        element('#user-name').send_keys(user_name)
        element('#password').send_keys(password)
        click('#login-button')
        wait.until(EC.url_contains('/inventory.html'))
        click('#add-to-cart-sauce-labs-backpack')
        assert element('.shopping_cart_badge').text == '1'
        click('.shopping_cart_link')
        assert element('.inventory_item_name').text == 'Sauce Labs Backpack'
        assert element('.cart_quantity').text == '1'
        assert element('.inventory_item_price').text == '$29.99'
        click('#checkout')
        element('#first-name').send_keys(first_name)
        element('#last-name').send_keys(last_name)
        element('#postal-code').send_keys(postalcode)
        click('#continue')
        assert element('.inventory_item_name').text == 'Sauce Labs Backpack'
        assert element('.summary_subtotal_label').text == 'Item total: $29.99'
        tax = Decimal(element('.summary_tax_label').text.split('$')[1])
        total = Decimal(element('.summary_total_label').text.split('$')[1])
        assert tax == Decimal('2.40')
        assert total == Decimal('29.99') + tax == Decimal('32.39')
        click('#finish')
        assert element('.complete-header').text == 'Thank you for your order!'
        assert not driver.find_elements(By.CSS_SELECTOR, '.shopping_cart_badge')
        driver.save_screenshot(str(output / 'checkout-completo.png'))
    except Exception:
        try:
            driver.save_screenshot(str(output / 'falha.png'))
        except Exception:
            logging.exception('Não foi possível capturar a tela da falha')
        raise
    finally:
        driver.quit()


if __name__ == '__main__':
    test_checkout()
