from flask import Flask, request, render_template, redirect, url_for
import json
from flask import make_response
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        recipients = request.form['recipients']
        print(recipients)
        #return render_template("index.html")
        return render_template('review.html', recipients = recipients)
    else:
        return render_template("index.html")
test=1
# page to review and send transaction
@app.route('/review', methods=['GET','POST'])
def review(recipients):
    return render_template('review.html', recipients = recipients)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
