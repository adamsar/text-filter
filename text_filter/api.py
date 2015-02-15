from flask import Flask, request, render_template, make_response
from text_filter.massage import massage
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/filter", methods=["POST"])
def modify_text():
    text = request.form['text']
    filtered_text = massage(text)
    response = make_response(filtered_text)
    response.headers['Content-Disposition'] = 'attachment; filename=filtered.txt'
    return response
