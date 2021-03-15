import os
from config import app
from api import api
from api.Login import Login
from api.Authenticate import Authenticate
from flask import url_for,redirect, render_template,session, request ,make_response, jsonify
from flask_dance.contrib.github import make_github_blueprint, github
import database
import generate_token
import jwt, json
from http import HTTPStatus

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
            print("account info json",account_info_json)
            with app.app_context():
                user={
                    "username":"pratiksha",
                     "email": "pratikshapshelke@gmail.com",
                    "login":account_info_json['login'],
                    "location":account_info_json['location'],
                    "roleid":""
                }

                db=database.createUser(user)
                print("user in db is...",db)
                if db:
                    role = database.getRole(db['roleid'])
                    if role:
                        # token=generate_token.generateToken(account_info_json['name'],role['role'])
                        token = generate_token.generateToken(db['username'], role['role'])
                        print("token is...",token)
                        session['bearerToken'] = token
                        session['username'] = account_info_json['login']
                        rendered = render_template('blog.html', \
                                                   session=session)
                        return rendered
            # return '<h1>Your Github name is {}'.format(account_info_json['login'])

    return '<h1>Request failed!</h1>'

@app.route('/authorize',methods = ['POST'])
def authorize():
        try:
            action = request.headers['operation']
            print("action.....",action)
            token = request.headers['X_ACCESS_TOKEN']
            print("token.....",token)

            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            data = database.validatePermission(action,decoded_token['role'])
            if data:
               return data
            return None

        except Exception as e:
            return make_response(jsonify(
                {
                    "title": "Error occcured",
                    "status": HTTPStatus.BAD_REQUEST,
                }
            ),
                HTTPStatus.BAD_REQUEST
            )
if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5002, debug=True)