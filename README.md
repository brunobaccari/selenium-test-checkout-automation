# Selenium · Checkout no SauceDemo

[English](README.en.md)

Jornada de login, carrinho e checkout no [SauceDemo](https://www.saucedemo.com/). Verifica produto, quantidade, preço, subtotal, imposto, total, confirmação e esvaziamento do carrinho. Falhas encerram o processo com erro; o navegador fecha também quando uma validação falha.

## Executar

Com Python 3.14 e Chrome instalados:

```sh
python -m venv .venv
# Ative .venv no seu terminal
python -m pip install -r requirements.txt
cp .env.example .env
python -m pytest -q arquivo_principal.py --junitxml=results/junit.xml
```

No PowerShell, copie o exemplo com `Copy-Item .env.example .env`. A conta padrão é pública e exclusiva do site de demonstração. Configure `HEADLESS=false` para acompanhar o navegador. `python arquivo_principal.py` executa a mesma jornada sem o relatório JUnit. Selenium Manager resolve o driver; o binário histórico no repositório não é utilizado explicitamente.

## Decisões e limites

Esperas são por estado da página; não há retries para esconder falhas. Os valores esperados são do catálogo de demonstração. A suíte não verifica pagamento real, backend ou outros produtos. As preferências que desativam o gerenciador de senhas valem somente para o perfil temporário de teste.

No Actions, cada execução publica summary, JUnit e screenshots em **Artifacts**. Outputs ficam em `results/`, ignorado pelo Git; não são versionados.

O summary do Actions lista cada cenário, duração, totais e motivo de bloqueio. O gate exige a quantidade prevista no workflow, sem falhas ou skips; JUnit ausente ou inválido reprova. O resumo também acompanha o artifact.
