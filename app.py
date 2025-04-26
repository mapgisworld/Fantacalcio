from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fair_play')
def fair_play():
    return render_template('fair_play.html')

if __name__ == '__main__':
    app.run(debug=True)