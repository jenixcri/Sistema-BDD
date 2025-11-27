from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

usuarios = {"teste@exemplo.com": "123456"}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    email = request.form.get("email")
    senha = request.form.get("senha")

    if email in usuarios:
        return render_template("cadastro.html", mensagem="Usuário já existe"), 400
    else:
        usuarios[email] = senha
        return render_template("login.html", mensagem="Cadastro realizado com sucesso! Faça login."), 200

@app.route("/login", methods=["POST"])
def login():
    if request.content_type == "application/x-www-form-urlencoded":
        email = request.form.get("email")
        senha = request.form.get("senha")
        if email not in usuarios:
            return render_template("login.html", mensagem="Usuário não encontrado")
        elif usuarios[email] != senha:
            return render_template("login.html", mensagem="Credenciais inválidas")
        else:
            return render_template("welcome.html", mensagem="Bem-vindo!")
    else:
        data = request.json
        email = data.get("email")
        senha = data.get("senha")
        if email not in usuarios:
            return jsonify({"mensagem": "Usuário não encontrado"}), 404
        elif usuarios[email] != senha:
            return jsonify({"mensagem": "Credenciais inválidas"}), 401
        else:
            return jsonify({"mensagem": "Bem-vindo!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
