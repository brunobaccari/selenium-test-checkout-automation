import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configurações do Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options= chrome_options)

# Definir caminhos de log e evidências
if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(evidence_path):
    os.makedirs(evidence_path)
timestamp = time.strftime('%Y%m%d-%H%M%S')
log_filename = f'log_{timestamp}.txt'
log_file = os.path.join(log_path, log_filename)

# Adicionar o handler ao logger
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(file_handler)

# Função para tirar prints e salvar em pasta de evidências
def take_screenshot():
    num_prints = len(os.listdir(evidence_path))
    nome_arquivo = f'CT_evidencia_{str(num_prints+1).zfill(3)}.png'
    path_arquivo = os.path.join(evidence_path, nome_arquivo)
    driver.get_screenshot_as_file(path_arquivo)
    logging.info('tirando print' + f'CT_evidencia_{str(num_prints+1).zfill(3)}.png')

# Abrir o site e preencher campos
logging.info('Abrindo site')
driver.get(site)
driver.implicitly_wait(2)
take_screenshot()
logging.info('escrevendo usuário')
driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)

logging.info('escrevendo senha')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
take_screenshot()
logging.info('clicando no botão de login')
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
driver.implicitly_wait(2)

# Adicionar item ao carrinho e realizar checkout
take_screenshot()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
logging.info('adicionando ao carrinho')
take_screenshot()
driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()
take_screenshot()
driver.find_element(By.CSS_SELECTOR, '#checkout').click()
take_screenshot()
logging.info('escrevendo dados')
driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postalcode)
take_screenshot()
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
take_screenshot()
driver.find_element(By.CSS_SELECTOR, '#finish').click()
take_screenshot()

# Finalizar testes e fechar driver
logging.info('Teste Passou')
file_handler.close()
time.sleep(5)
driver.quit()
