from flask import Flask, render_template, request
from preprocessing import preprocess_text
from model import predict
from verifier import verification_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        text = request.form.get("article", "")

        if text.strip():
            original, processed = preprocess_text(text)
            probs = predict(processed)

            for i in range(len(original)):
                prob = probs[i]
                extra = verification_score(processed[i])

                score = prob

                if extra < 0:
                    score += extra * 0.6

                if prob > 0.65:
                    score += 0.1

                score = max(0, min(score, 1))

                if score < 0.4:
                    color = "red"
                elif score < 0.6:
                    color = "orange"
                else:
                    color = "green"

                results.append({
                    "sentence": original[i],
                    "score": round(score, 2),
                    "color": color
                })

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
