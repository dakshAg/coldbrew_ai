from flask import Flask
import image_search
import metrics
from flask import request

app = Flask(__name__)


@app.route("/")
def main():
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@app.route("/final_report", methods=['GET'])
def final_report():
    query = request.args.get('p', '')
    city_url = "https://www.melbourne.vic.gov.au/residents/waste-recycling/Pages/a-z-waste-disposal.aspx"
    return metrics.final_report(query, city_url)


@app.route("/image_search", methods=['GET'])
def image_search():
    query = request.args.get('url', '')
    return image_search.image_search(query)
