#!/usr/bin/env python3.5

"""
This piece of garbage is for demo testing purposes only
"""

import json
from flask import Flask, request, redirect, session, render_template

app = Flask(__name__)

def read_posts():
    posts = []
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    return posts

def write_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f)

def get_home():
    user = "Welcome"
    if 'username' in session:
        user = session['username']

    posts = read_posts()
    return render_template('base.html', posts=posts, user=user)

def post_home():
    post = request.form.get('post')
    posts = read_posts()
    posts.append(post)
    write_posts(posts)

    return get_home()

# serve 'meta' fil
@app.route('/', methods=["GET", "POST"])
def serve_home():
    if request.method == "GET":
        return get_home()
    else:
        return post_home()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('username')
        session['username'] = user
        return redirect('/')

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(port=9447, debug=True, host='0.0.0.0')
