import os

site= 'https://www.saucedemo.com/'
user_name= 'standard_user'
password= 'secret_sauce'
first_name='Bruno'
last_name = 'Baccari'
postalcode='13482-820'
dir_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(dir_path, 'logs')
evidence_path = os.path.join(dir_path, 'evidencias')