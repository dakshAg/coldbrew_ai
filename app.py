from flask import Flask
from scores.waste import waste_guide
from scores.sustainability import sustainability_score
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


@app.route("/ai_sustainability_score", methods=['GET'])
def ai_sustainability_score():
    query = request.args.get('q', '')
    x, scores, result = sustainability_score.ai_sustainability_score(query)
    return {
        "response": x,
        "scores": scores,
        "final_score": result
    }
