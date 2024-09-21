from flask import Flask, render_template
import time
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def lote():
    while True:
        # Lote number from Elche
        page_elche = requests.get('https://webparainmigrantes.com/extranjeria-elche-lote-nie/')
        soup_elche = BeautifulSoup(page_elche.text, 'html.parser')
        lote_number_elche = soup_elche.find_all('p')
        a = str('ÚLTIMO LOTE NUMERO DE ELCHE ' + lote_number_elche[11].text + '    ' + lote_number_elche[12].text)

        # Lote number from Murcia
        page_murcia = requests.get('https://webparainmigrantes.com/extranjeria-murcia-lote-nie/')
        soup_murcia = BeautifulSoup(page_murcia.text, 'html.parser')
        lote_number_murcia = soup_murcia.find_all('p')
        b = str('ÚLTIMO LOTE NUMERO DE MURCIA ' + lote_number_murcia[12].text + '    ' + lote_number_murcia[13].text)

        # Lote number from Alicante
        page_alicante = requests.get('https://webparainmigrantes.com/tie-extranjeria-alicante-oficina-campo-de-mirra/')
        soup_alicante = BeautifulSoup(page_alicante.text, 'html.parser')
        lote_number_alicante = soup_alicante.find_all('p')
        c = str(
            'ÚLTIMO LOTE NUMERO DE ALICANTE ' + lote_number_alicante[24].text + '    ' + lote_number_alicante[25].text)

        return f'''
        <html>
            <body style="background-color:powderblue;" style="font-size:300%;" style="text-align:center;">               
                {a} 
                <br>
                <br>
                {b}
                <br>
                <br>
                {c}             
            </body>
        </html> '''

    time.sleep(8000)


if __name__ == '__main__':
    app.run(debug=True)
