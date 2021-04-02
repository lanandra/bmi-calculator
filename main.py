# main.py

from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    bmi = ""
    label = ""
    if request.method == "POST" and "weight" in request.form:   
        height = float(request.form.get("height"))
        weight = float(request.form.get("weight"))
        bmi = bmi_calculation(height, weight)
        label = bmi_label(bmi)
    return render_template("index.html", bmi=bmi, label=label)

def bmi_calculation(height, weight):
    return round(weight / (height / 100) ** 2, 2)

def bmi_label(bmi):
    if bmi < 18.5:
        label = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        label = "Normal weight"
    elif bmi >= 25.0:
        label = "Overweight"
    return label

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)