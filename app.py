from flask import Flask, render_template, request
from slang_module import convert_slang

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    output_text = ""
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("slang_text")
        output_text = convert_slang(input_text)

    return render_template("index.html",
                           input_text=input_text,
                           output_text=output_text)

if __name__ == "__main__":
    app.run(debug=True)
