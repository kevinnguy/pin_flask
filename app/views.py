from app import app
from flask import Flask, render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')