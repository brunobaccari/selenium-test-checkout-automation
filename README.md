# selenium-test-checkout-automation
Descrição do projeto
Este é um projeto de automação de teste utilizando o Selenium WebDriver em Python. O objetivo é realizar uma compra em um site de e-commerce (https://www.saucedemo.com/) preenchendo informações do usuário e realizando o checkout.

Pré-requisitos
Python 3.x
ChromeDriver (versão compatível com a versão do seu Chrome)

Como funciona
O script principal (arquivo_principal.py) abre o site de e-commerce, realiza o login com as credenciais fornecidas no arquivo config.py, adiciona um item ao carrinho e preenche as informações necessárias para a finalização da compra. Durante o processo, o script tira prints da tela e salva em uma pasta de evidências.

O arquivo config.py contém as informações de configuração, como as credenciais de login, as informações de checkout e os caminhos para as pastas de log e evidências.

Como utilizar
Para utilizar o script, é necessário ter o Python e o ChromeDriver instalados na máquina. Além disso, é preciso instalar as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt

Após a instalação das dependências, basta executar o script principal:
python Código_principal.py
