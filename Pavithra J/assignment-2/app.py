from flask import Flask, Blueprint, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def login():
    return render_template('login.html')
