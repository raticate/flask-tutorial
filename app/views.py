from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Cate'}  # fake user
    posts = [{'author': {'nickname':'John'},'body': {'Beautiful day!!'}},{'author': {'nickname': 'Susan'}, 'body': 'Zootopia was so cool!'}]
    return render_template('index.html', user = user,)
