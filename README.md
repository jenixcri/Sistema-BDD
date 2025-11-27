# Projeto BDD - Sistema de Login e Cadastro

Este projeto demonstra a aplicação da técnica **BDD (Behavior Driven Development)** utilizando **Flask** para a aplicação web e **Behave** para os testes automatizados.

---

## 1. Histórias de Usuário

### Login
**Como** usuário cadastrado  
**Quero** realizar login no sistema  
**Para** acessar as funcionalidades disponíveis  

### Cadastro
**Como** visitante  
**Quero** me cadastrar no sistema  
**Para** poder realizar login posteriormente  

---

## 2. Cenários

### Login
- Login bem-sucedido  
- Login com senha incorreta  
- Login com usuário inexistente  

### Cadastro
- Cadastro bem-sucedido  
- Cadastro com email já existente  

---

## 3. Tecnologias Utilizadas
- Python 3.12  
- Flask  
- Behave  
- Requests  
- HTML + CSS (interface visual estilizada)  

---

## 4. Como Executar

1. Instale as dependências:
   ```bash
   pip install flask behave requests
2. Rode o servidor Flask:
   ```bash
   python app.py
3. Acesse no navegador:
Login → http://127.0.0.1:5000
Cadastro → http://127.0.0.1:5000/cadastro
4. Execute os testes BDD:
   ```bash
   behave
