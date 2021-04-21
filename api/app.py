from flask import Flask, jsonify, request
from flask_cors import CORS
from model import get_stores_data

app = Flask(__name__)
CORS(app)


@app.route('/stores', methods=["GET", "POST"])
def get_stores():
    """
    Get stores to return in response from search query input
    Returns json response object with the application/json mimetype set
    """
    # Get data from stores.json static file
    all_stores_data = get_stores_data()
    query = request.args.get('q')
    # print(query)

    # App search input is min 2 characters
    # but if no query params, return all data from stores.json file
    if not query:
        return jsonify(all_stores_data)
    else:
        filtered_stores_data = filter_stores_data(query, all_stores_data)

    return jsonify(filtered_stores_data)


def filter_stores_data(query, all_stores_data):
    """
    Check if stores.json data contains query string submitted in the response
    If a match, add store dict to new list
    :param query:
    :param all_stores_data:
    :return: list of dicts
    """
    filtered_stores = []

    for store in all_stores_data:
        if query.lower() in store['postcode'].lower():
            filtered_stores.append(store)
        elif query.lower() in store['name'].lower():
            filtered_stores.append(store)

    return filtered_stores


app.run()
