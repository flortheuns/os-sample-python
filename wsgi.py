import requests
import json
from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    

    url='https://vault-hashicorp-vault.172.17.155.103.nip.io/v1/secret/example'
    token = getToken()
    headers={'X-Vault-Token': token}
    r=requests.get(url, headers=headers, verify=False)
    r_json=r.json()
    data=r_json["data"]
    cert=data["cert"]
    key=data["key"]
    cert2 = '-----BEGIN CERTIFICATE-----'+'\n'
    key2 = '-----BEGIN RSA PRIVATE KEY-----'+'\n'
    check = 0
    check2 = 0
    for line in cert.split():
        if line == "CERTIFICATE-----":
            if check == 1:
                cert2 += " CERTIFICATE-----\n"
            check = 1
            continue
        if check == 1:
            cert2 += '\n'
            cert2 += line
    for line in key.split():
        if line == "KEY-----":
            check2 = 1
            continue
        if line == "-----END":
            check2 = 2
            key2 += '\n'
            key2 += "-----END RSA PRIVATE KEY-----\n"
            continue
        if check2 == 1:
            key2 += '\n'
            key2 += line
    rendered = render_template('home.html', \
        cert = cert2, \
        key = key2)
    return rendered

if __name__ == "__main__":
    application.run()

def getToken():
    url='https://vault-hashicorp-vault.172.17.155.103.nip.io/v1/auth/kubernetes/login'
    f = open('/var/run/secrets/kubernetes.io/serviceaccount/token')
    jwt = f.read()
    params = {
            "role": "example",
            "jwt": jwt,
    }
    r = requests.post(url, data=json.dumps(params), verify=False)
    r_json=r.json()
    auth = r_json["auth"]
    token = auth["client_token"]
    return token

