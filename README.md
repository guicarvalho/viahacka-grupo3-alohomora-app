# Alohomora Web

A aplicação web foi construida durante o evento `ViaHacka em: O enigma dos dados`.

## Ferramentas

- Python 3.x
- PostgreSQL

## Execução Local

Siga os passos para rodar localmente:

```sh
python -m venv .env
. ./env/bin/activate
pip install -r requirements.txt
export DB_HOST=<endereco_banco_de_dados>
python main.py
```

O projeto está disponível em [https://alohomora-app.us-south.cf.appdomain.cloud/](https://alohomora-app.us-south.cf.appdomain.cloud/). Para acessar é necessário informar um ID de Seller válido e qualquer valor para senha.
