import json
import urllib.parse
from flask import Flask, jsonify, Response
from scraper import scrape


app = Flask(__name__)

@app.route("/search/<searchQueryString>", methods=["GET"])
def getSearchResults(searchQueryString):
    searchQueryURL = 'https://www.amazon.com/s?k=' + urllib.parse.quote_plus(searchQueryString)
    data = scrape(searchQueryURL, "search")
    if data:
        formattedData = json.dumps(data)
        # sleep(5)
    return Response(formattedData, mimetype='text/json')

@app.route("/product/<productQueryString>", methods=["GET"])
def getProductResults(productQueryString):
    productQueryURL = 'https://www.amazon.com/dp/' + urllib.parse.quote_plus(productQueryString)
    data = scrape(productQueryURL, "product")
    if data:
        formattedData = json.dumps(data)
        # sleep(5)
    return Response(formattedData, mimetype='text/json')


if __name__ == '__main__':
    app.run(port=8080)
