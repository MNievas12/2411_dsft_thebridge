from flask import Flask
application = Flask(__name__)  # ¡El objeto debe llamarse "application"!

@application.route('/')
def hello():
    return "¡Desplegando en Elastic Beanstalk!"