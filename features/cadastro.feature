Feature: Cadastro de usuário
  Como visitante
  Quero me cadastrar no sistema
  Para poder realizar login posteriormente

  Scenario: Cadastro bem-sucedido
    When eu envio email "novo@exemplo.com" e senha "abc123" para o endpoint de cadastro
    Then devo receber status 200
    And a mensagem "Cadastro realizado com sucesso! Faça login."

  Scenario: Cadastro com email já existente
    Given que o usuário "teste@exemplo.com" existe com senha "123456"
    When eu envio email "teste@exemplo.com" e senha "novaSenha" para o endpoint de cadastro
    Then devo receber status 400
    And a mensagem "Usuário já existe"
