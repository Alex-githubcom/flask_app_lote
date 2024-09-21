from flask import Flask, render_template
import time
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def lote():
    # Lote number from Elche
    page_elche = requests.get('https://webparainmigrantes.com/extranjeria-elche-lote-nie/')
    soup_elche = BeautifulSoup(page_elche.text, 'html.parser')
    #print(soup_elche.text)

    return soup_elche.text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8989, debug=True)
