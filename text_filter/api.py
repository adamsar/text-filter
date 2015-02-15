from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/modify_text", methods=["POST"])
def modify_text():
    #TODO
    pass
