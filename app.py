from flask import Flask, render_template
import time
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def lote():
    print ('Hello, lote')
    #return str(page_elche.status_code)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8989, debug=True)
