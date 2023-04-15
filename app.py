from flask import Flask
import image_search
import metrics
from flask import request

app = Flask(__name__)


@app.route("/")
def main():
    """Not Much. Just Empty Placeholder Function"""
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@app.route("/final_report", methods=['GET'])
def final_report():
    """Takes in the user selected product name, and returns the Carbon Footprint and Water Footprint"""
    query = request.args.get('p', '')
    city_url = "https://www.melbourne.vic.gov.au/residents/waste-recycling/Pages/a-z-waste-disposal.aspx"
    return metrics.final_report(query, city_url)


@app.route("/image_search", methods=['GET'])
def image_search():
    """Takes in the url of user clicked image, and returns a list of 5 similar items, to look up further data for"""
    query = request.args.get('url', '')
    return image_search.image_search(query)
