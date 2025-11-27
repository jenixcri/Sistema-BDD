from behave import then

@then('devo receber status {status:d}')
def step_impl(context, status):
    assert context.response.status_code == status

@then('a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    try:
        assert context.response.json()["mensagem"] == mensagem
    except:
        assert mensagem in context.response.text
