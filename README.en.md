# Selenium · Checkout journey

[Versão em português](README.md)

A Python script that walks through login, cart and checkout on [SauceDemo](https://www.saucedemo.com/), recording screenshots and step logs.

## Run

With Python and Chrome installed:

```sh
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on Linux/macOS.

```sh
python -m pip install -r requirements.txt
python arquivo_principal.py
```

`config.py` contains the URL, public SauceDemo account, checkout data and output directories. This implementation reads that module directly; it does not load `.env`. Use demonstration data only.

## What the code does

1. Opens Chrome and logs in.
2. Adds the backpack to the cart.
3. Fills in checkout details and completes the journey.
4. Saves screenshots in `evidencias` and records in `logs`.

This is an interaction and evidence-capture example. The script's completion message is not a substitute for assertions on the order total or confirmation; those checks are not implemented as tests.

## Environment

The project preserves older dependencies, including Selenium 4.8, and a `chromedriver.exe`. Check driver/browser compatibility. This review corrected the run command's filename and documented existing behavior; it did not rerun the script or update dependencies.
