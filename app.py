from flask import Flask, render_template, redirect, request, session,url_for,flash,send_file
from flask_sqlalchemy import SQLAlchemy
import os
from database import db

import config
from model import User




app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'secretkey'

app.config['SQLALCHEMY_DATABASE_URL']=config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)





"""
检查登录，路由后加@auth
from functools import wraps  
def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        username = session.get('username')
        if not username:
            return redirect('/')
        return func(*args,**kwargs)
    return inner"""


@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        user_info=User.query.filter_by(username=username).first()
        avatar=user_info.avatar
    else:
        avatar = 'static\img\profilephoto.png'
        username='欢迎'
    return render_template('index.html',logged_in='logged_in' in session,name=username,profilePic=avatar)

@app.route('/login_page')
def login_page():
    return render_template('login.html')



@app.route('/note')
def note():
    return render_template('note.html')

@app.route("/login_page/login",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username,password=password).first()
        if user:
            session['username'] = username
            session['logged_in'] = True
            flash(u'登录成功，欢迎回来！', 'info')
            return redirect('/')
        elif not all([username,password]):
            flash(u'用户名或密码不能为空')
        else:
            flash(u'用户名或密码错误')

    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username=request.form.get('username')
        password1=request.form.get('password1')
        password2 = request.form.get('password2')
        email=request.form.get('email')
        if not all([username,password1,password2,email]):
            flash(u'参数不完整')
        elif password1!=password2:
            flash(u'两次密码不一致，请重新输入')
        elif User.query.filter_by(username=username).first():
            flash(u'ah-oh!用户名已经被抢先注册了')
        else:
            user = User(username=username, password=password2,email=email)
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            #
            return redirect('/')
    return render_template('login.html')



@app.route("/logout")
def logout():
    """退出登录"""
    # 清除session数据
    session.clear()
    session.pop('logged_in', None)
    return redirect('/')

@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static/uploads', f.filename)
        f.save(upload_path)
        return redirect(url_for('download'))
    return render_template('upload.php')



if __name__ == "__main__":

    app.run(debug=True, host="127.0.0.1", port=18080)
