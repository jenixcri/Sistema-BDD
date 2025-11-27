Feature: Login de usuário
  Como usuário cadastrado
  Quero realizar login no sistema
  Para acessar as funcionalidades disponíveis

  Scenario: Login bem-sucedido
    Given que o usuário "teste@exemplo.com" existe com senha "123456"
    When eu envio email "teste@exemplo.com" e senha "123456" para o endpoint de login
    Then devo receber status 200
    And a mensagem "Bem-vindo!"

  Scenario: Login com senha incorreta
    Given que o usuário "teste@exemplo.com" existe com senha "123456"
    When eu envio email "teste@exemplo.com" e senha "errada" para o endpoint de login
    Then devo receber status 401
    And a mensagem "Credenciais inválidas"

  Scenario: Login com usuário inexistente
    When eu envio email "naoexiste@exemplo.com" e senha "123456" para o endpoint de login
    Then devo receber status 404
    And a mensagem "Usuário não encontrado"
