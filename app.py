from flask import Flask
import image_search
import metrics
from flask import request

app = Flask(__name__)
if __name__ == "__main__":
    app.run(host="192.168.2.18", port=5000)


@app.route("/")
def main():
    """This is just a placeholder function

    Returns:
        None: nothing for now.
    """
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@app.route("/final_report", methods=['GET'])
def final_report():
    """Takes in the string of user selected product name, and returns the Carbon Footprint and Water Footprint

    Returns:
        str: Strings of the carbon and water footprint.
    """
    query = request.args.get('p', '')
    city_url = "https://www.melbourne.vic.gov.au/residents/waste-recycling/Pages/a-z-waste-disposal.aspx"
    return metrics.final_report(query, city_url)


@app.route("/image_search", methods=['GET'])
def img_search():
    """Takes in the string url of user clicked image, and returns a list of 5 similar items, to look up further data for

    Returns:
        list: list of dictionaries comprised of name, image link and url.
    """
    query = request.args.get('url', '')
    return image_search.image_search(query)
