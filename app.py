from flask import Flask, session
from controllers.principalController import loginController, geralController

app = Flask(__name__)

app.secret_key = 'chavemuitosecreta'

app.register_blueprint(loginController)
app.register_blueprint(geralController)


if __name__ == "__main__":
    app.run(debug = True)