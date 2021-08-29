from flask import render_template

from app import app

#两个路由
@app.route('/')
@app.route('/index')
#1个视图函数
def index():
    user = {'username': '汪洋'}

    posts = [
        {
            'author': {'username':'john'},
            'body': 'Beautiful day in Portlad'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)