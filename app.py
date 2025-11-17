from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    # retorna o HTML gerado pelo folium
    return send_from_directory(BASE_DIR, "mapa_praca_central.html")

# rota opcional para arquivos estáticos se você tiver assets locais
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(BASE_DIR, "static"), filename)

if __name__ == "__main__":
    app.run(debug=True)
