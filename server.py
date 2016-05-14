from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage with form"""
    return render_template("homepage.html")

@app.route('/', methods=['POST'])
def text_form_post():
    text = request.form('text')
    return text

if __name__ == '__main__':
    # app.debug = True
    app.run()