import pickle
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, template_folder="templates")

# 1
@app.before_first_request
def load_model():
    global pipe
    # 2
    with open("model/pipe.pkl", "rb") as f:
        pipe = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def predict():
    # 3
    form = request.form
    # 4
    new = pd.DataFrame({
        'carat': [form['carat']],
        'cut': [form['cut']],
        'color': [form['color']],
        'clarity': [form['clarity']],
    })
    # 5
    price = pipe.predict(new)[0]
    price = "${:,.2f}".format(price)
    return render_template("result.html", price=price)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)