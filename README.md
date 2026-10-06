# Selenium · Jornada de checkout

[English version](README.en.md)

Script Python para percorrer login, carrinho e checkout no [SauceDemo](https://www.saucedemo.com/), registrando telas e logs das etapas.

## Executar

Com Python e Chrome instalados:

```sh
python -m venv .venv
```

Ative com `.venv\Scripts\Activate.ps1` no PowerShell ou `source .venv/bin/activate` no Linux/macOS.

```sh
python -m pip install -r requirements.txt
python arquivo_principal.py
```

`config.py` contém a URL, a conta pública do SauceDemo, os dados de checkout e os diretórios de saída. Essa implementação lê o módulo diretamente; não carrega `.env`. Use apenas dados de demonstração.

## O que o código faz

1. Abre o Chrome e realiza login.
2. Adiciona a mochila ao carrinho.
3. Preenche os dados do checkout e conclui a jornada.
4. Salva screenshots em `evidencias` e registros em `logs`.

É um exemplo de interação e coleta de evidências. A mensagem de conclusão do script não substitui assertions do total ou da confirmação do pedido; essas verificações não estão implementadas como testes.

## Ambiente

O projeto preserva dependências antigas, incluindo Selenium 4.8, e um `chromedriver.exe`. Confira a compatibilidade do driver com o navegador. Essa revisão corrigiu o nome do comando de execução e documentou o comportamento existente; não reexecutou o script nem atualizou as dependências.
