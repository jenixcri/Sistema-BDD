import requests
from behave import when, then, given

BASE_URL = "http://127.0.0.1:5000"

@when('eu envio email "{email}" e senha "{senha}" para o endpoint de cadastro')
def step_impl(context, email, senha):
    response = requests.post(f"{BASE_URL}/registrar", data={"email": email, "senha": senha})
    context.response = response

