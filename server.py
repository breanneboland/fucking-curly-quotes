from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route("/")
def index():
    """Homepage with form"""
    return render_template("homepage.html")

@app.route("/submit", methods=["GET"])
def text_form_post():
    """Stub to pass submitted text through"""
    text = request.args.get("text")
    print text
    print "text_form_post!"
    return render_template("submit.html", text=text)

if __name__ == "__main__":
    app.debug = True
    app.run()