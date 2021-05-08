from flask_pymongo import PyMongo
from mars_scrape import scrape_all
from flask import Flask, render_template, redirect

app = Flask(__name__)

mongo = PyMongo(app, uri = 'mongodb://localhost:27017/mars_db')

app.route('/')
def home():
    return 'Hello'


if __name__=='__main__':
    app.run(debug=True)