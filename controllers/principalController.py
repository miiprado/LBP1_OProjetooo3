from flask import Blueprint, request, render_template, redirect, url_for, session
from models.userr import listaUsuarios

loginController = Blueprint('loginController', __name__)
geralController = Blueprint('geralController', __name__)

@geralController.route("/")
def homepage():
    return render_template("homepage.html")

@loginController.route("/login", methods=["GET", "POST"])
def login():
    usuario = request.form.get("nome")
    senha = request.form.get("senha")
    
    if request.method == "POST":
        for pessoa in listaUsuarios:
            if pessoa.nome == usuario:
                if pessoa.senha == senha:
                    session['username'] = usuario
                    return redirect(url_for("loginController.login_sucedido"))
                
        return redirect(url_for("geralController.homepage"))
    
@loginController.route("/login_sucedido")
def login_sucedido():
    if 'username' in session:
        return render_template("login_sucedido.html")
    return redirect(url_for("geralController.homepage"))

@loginController.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("geralController.homepage"))