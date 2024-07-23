from flask import Flask, render_template, request, jsonify
from src.pipeline.prediction_pipeline import Features, Prediction

application = Flask(__name__)
app = application


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("form.html")
    else:
        f = Features(
            creditscore=int(request.form.get("creditscore")),
            country=request.form.get("country"),
            gender=request.form.get("gender"),
            age=int(request.form.get("age")),
            tenure=int(request.form.get("tenure")),
            balance=int(request.form.get("balance")),
            hascrcard=request.form.get("hascrcard"),
            isactivemember=request.form.get("isactivemember"),
            estimatedsalary=int(request.form.get("estimatedsalary"))
        )
        processed_data = f.to_dataframe()
        print(processed_data)
        p = Prediction()
        op = p.initiate_prediction(processed_data)
        result = op[0]
        return render_template("result.html", final_result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
