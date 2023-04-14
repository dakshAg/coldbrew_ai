from flask import Flask
from scores.waste import waste_guide
from flask import request

app = Flask(__name__)


@app.route("/")
def main():
    query = request.form['q']
    city_url = "https://www.melbourne.vic.gov.au/residents/waste-recycling/Pages/a-z-waste-disposal.aspx"
    return waste_guide.ai_disposal(query, city_url)


@app.route("/ai_disposal", methods=['GET'])
def ai_disposal():
    query = request.args.get('q', '')
    city_url = "https://www.melbourne.vic.gov.au/residents/waste-recycling/Pages/a-z-waste-disposal.aspx"
    return waste_guide.ai_disposal(query, city_url)
