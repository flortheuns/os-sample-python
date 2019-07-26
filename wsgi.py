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
    r_json=r.json()
    data=r_json["data"]
    cert=data["cert"]
    key=data["key"]
    cert2 = '-----BEGIN CERTIFICATE-----'
    key2 = '-----BEGIN RSA PRIVATE KEY-----'
    check = 0
    check2 = 0
    for line in cert.split():
        if line == "CERTIFICATE-----":
            check = 1
            continue
        if check == 1:
            cert2 += '<br>'
            cert2 += line
    for line in key.split():
        if line == "KEY-----":
            check2 = 1
            continue
        if check2 == 1:
            key2 += '<br>'
            key2 += line
    rendered = render_template('home.html', \
        cert = cert2, \
        key = key2)
    return rendered

if __name__ == "__main__":
    application.run()
