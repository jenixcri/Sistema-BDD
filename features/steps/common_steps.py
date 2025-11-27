from behave import then

@then('devo receber status {status:d}')
def step_impl(context, status):
    assert context.response.status_code == status

@then('a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    # funciona tanto para JSON quanto para HTML
    try:
        # se a resposta for JSON
        assert context.response.json()["mensagem"] == mensagem
    except:
        # se a resposta for HTML
        assert mensagem in context.response.text
