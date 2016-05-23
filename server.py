from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from unfuck import unfuck_your_string

app = Flask(__name__)

@app.route("/")
def index():
    """Homepage with form"""
    return render_template("homepage.html")

@app.route("/sample")
def sample_route():
    """Just a test"""
    return render_template("sample.html")

@app.route("/submit", methods=["GET"])
def text_form_post():
    """Stub to pass submitted text through"""
    text = request.args.get("text")
    forbidden_characters = ["“", "”", "‘", "’"]
    # answer = unfuck_your_string(text)
    return render_template("submit.html", text=text, forbidden=forbidden_characters)

if __name__ == "__main__":
    app.debug = True
    app.run()