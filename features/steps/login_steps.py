import requests
from behave import given, when, then

BASE_URL = "http://localhost:5000"

@given('que o usuário "{email}" existe com senha "{senha}"')
def step_impl(context, email, senha):
    context.email = email
    context.senha = senha

@when('eu envio email "{email}" e senha "{senha}" para o endpoint de login')
def step_impl(context, email, senha):
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "senha": senha})
    context.response = response

