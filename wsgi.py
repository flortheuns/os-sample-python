import requests
import json
from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    f = open('/var/run/secrets/kubernetes.io/serviceaccount/token')
    jwt = f.read()
    rendered = render_template('home.html', \
        cert = jwt, \
        key = "niks")
    return rendered

if __name__ == "__main__":
    application.run()