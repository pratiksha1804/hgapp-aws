import os
from config import app
from api import api
from api.Login import Login
from api.Authenticate import Authenticate
from flask import url_for,redirect
from flask_dance.contrib.github import make_github_blueprint, github

github_blueprint = make_github_blueprint(client_id='9557a35e2914f0b9d46d',
                                         client_secret='083335de8ec8366ba060119baba8870e1e5e1d80')

app.register_blueprint(github_blueprint, url_prefix='/login')

api.add_resource(Login, '/api/login')
api.add_resource(Authenticate, '/api/authenticate')

@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return '<h1>Your Github name is {}'.format(account_info_json['login'])

    return '<h1>Request failed!</h1>'




if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5002, debug=True)