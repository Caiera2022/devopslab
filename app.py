from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "7ASO GRUPO 1"

@app.route("/bug")
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)
    except TypeError as e:
        print("Duplicando, ou seja, nunca vai entrar aqui.")

if __name__ == '__main__':
    app.run() 