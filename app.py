from flask import Flask, request, jsonify
from search import search, record_click
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/search", methods=["POST"])
def search_api():
    file = request.files["image"]
    category = request.form.get("category")

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    df = search(path, k=5, category=category)

    return jsonify(df.to_dict(orient="records"))


@app.route("/click", methods=["POST"])
def click_api():
    product_id = int(request.form["product_id"])
    record_click(product_id)
    return jsonify({"status": "ok"})


@app.route("/clicks")
def get_clicks():
    import pandas as pd
    if os.path.exists("click_log.csv"):
        df = pd.read_csv("click_log.csv")
        return df.to_json(orient="records")
    return jsonify([])


app.run(debug=True)
