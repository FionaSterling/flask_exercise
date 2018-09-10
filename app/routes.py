from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    welcome = 'Welcome to my page!'
    favorites = ['Gorillas', 'Elephants', 'Capybaras', 'Turtles', 'Monkeys', 'Pigeons', 'Lions']
    d = {
        'Favorite Place': 'Maine',
    }
    return render_template('index.html', welcome=welcome, favorites=favorites, d=d)

@app.route('/data')
def my_data():
    info = {
        'Favorite Color': 'Red',
        'Favorite Programming Language': 'Python, obviously...',
        'Favorite Season': 'Summer!',
    }
    
    travel = ['Albania', 'Greece', 'Italy', 'Bahamas', 'Turkey', 'Turks and Caicos', 'Bermuda', 'Canada', 'Mexico']

    return render_template('data.html', info=info, travel=travel)

@app.route('/redirect')
def my_redirect():
    return redirect(url_for('index'))
