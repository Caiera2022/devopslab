from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "7ASO GRUPO 01"

if __name__ == '__main__':
    app.run()