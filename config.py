import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name('.env'))
site = os.getenv('BASE_URL', 'https://www.saucedemo.com/')
user_name = os.getenv('SAUCE_USERNAME', 'standard_user')
password = os.getenv('SAUCE_PASSWORD', 'secret_sauce')
first_name = os.getenv('CHECKOUT_FIRST_NAME', 'Teste')
last_name = os.getenv('CHECKOUT_LAST_NAME', 'QA')
postalcode = os.getenv('CHECKOUT_POSTAL_CODE', '01001000')
headless = os.getenv('HEADLESS', 'true').lower() == 'true'
