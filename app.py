import os
from config import app
from api import api
from api.Login import Login
from api.Authenticate import Authenticate
from flask import url_for,redirect, render_template
from flask_dance.contrib.github import make_github_blueprint, github

github_blueprint = make_github_blueprint(client_id='a5355a72806cec35befa',
                                         client_secret='ae0d6b12844ebd5780d056f0f8bc1550b9bf1e7d')

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
            with app.app_context():
                rendered = render_template('blog.html', \
                                           name =account_info_json['login'])
                return rendered
            # return '<h1>Your Github name is {}'.format(account_info_json['login'])

    return '<h1>Request failed!</h1>'




if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5002, debug=True)