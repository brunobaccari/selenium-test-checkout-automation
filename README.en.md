# Selenium · SauceDemo checkout

[Português](README.md)

A login, cart and checkout journey on [SauceDemo](https://www.saucedemo.com/). Checks product, quantity, price, subtotal, tax, total, confirmation and cart clearing. Failed checks produce a failing exit status; the browser closes even when assertions fail.

## Run

With Python 3.14 and Chrome installed:

```sh
python -m venv .venv
# Activate .venv in your terminal
python -m pip install -r requirements.txt
cp .env.example .env
python -m pytest -q arquivo_principal.py --junitxml=results/junit.xml
```

On PowerShell, use `Copy-Item .env.example .env`. The default account is public demo data. Set `HEADLESS=false` to watch the browser. `python arquivo_principal.py` runs the same journey without JUnit. Selenium Manager resolves the driver; the historical binary in this repository is not explicitly used.

## Decisions and limits

Waits follow page state; retries do not hide failures. Expected amounts come from the demo catalog. This suite does not verify actual payments, backend behavior or other products. Password-manager preferences affect only the temporary test profile.

Each Actions run publishes a summary, JUnit and screenshots as **Artifacts**. Generated files stay in Git-ignored `results/` and are not committed.
