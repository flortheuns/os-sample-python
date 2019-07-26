import requests
import json
from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    

    url='https://vault-hashicorp-vault.172.17.155.108.nip.io/v1/secret/example'
    token ='5AElSCMsMzdpIFbA1l1uW1yC'
    headers={'X-Vault-Token': token}
    r=requests.get(url, headers=headers, verify=False)
    cert = r
    key = " "
    # r_json=r.json()
    # data=r_json["data"]
    # cert=data["cert"]
    # key=data["key"]
    # cert=cert.dumps()
    # key=key.dumps()
    rendered = render_template('home.html', \
        cert = cert, \
        key = key)
    return rendered

if __name__ == "__main__":
    application.run()
