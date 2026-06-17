import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Pages shown in the nav bar (label + route endpoint)
PAGES = [
    {"name": "Home", "endpoint": "index"},
    {"name": "Experience", "endpoint": "experience"},
    {"name": "Hobbies", "endpoint": "hobbies"},
    {"name": "Travel", "endpoint": "travel"},
]


@app.context_processor
def inject_pages():
    return {"pages": PAGES, "url": os.getenv("URL")}


@app.route('/')
def index():
    return render_template('index.html', title="Tarek Elsayed")


@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience")


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies")


@app.route('/travel')
def travel():
    return render_template('travel.html', title="Travel")
