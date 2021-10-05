from logging import error
from operator import indexOf
from flask import Blueprint, render_template, flash, session, g, request,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from wtforms.validators import Email
import string 
import random, re
from .db import Con_DB
 
from webpickle import db
from webpickle.models import userInfo,movieinfo,preferMovie
from webpickle.forms import UserCreateForm, UserLoginForm, FindIdForm,FindPasswordForm,UpdateInfo

con = Con_DB('imdb.db')
bp=Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/insert/', methods=('GET','POST'))
def insert():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = userInfo.query.filter_by(id=form.id.data).first()
        if not user:
            user = userInfo(id=form.id.data, number=form.number.data, n_name=form.n_name.data,pw=generate_password_hash(form.pw.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/insert.html',form=form)

@bp.route('/login/', methods=('GET','POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = userInfo.query.filter_by(id=form.id.data).first()
        if not user:
            error = "존재하지 않는 사용자 입니다."
        elif not check_password_hash(user.pw,form.pw.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['uno']=user.uno
            return redirect(url_for('main.main'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.route('/update/',methods =("GET","POST"))
def update():
    form = UpdateInfo()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = userInfo.query.filter_by(uno=session['uno']).first()
        if not check_password_hash(user.pw,form.pw.data):
            error = "존재하지 않는 사용자 입니다."
        else:
            user = userInfo.query.filter_by(id=g.user.id).update({'n_name':form.n_name.data, 'pw':generate_password_hash(form.pw1.data)})
            db.session.commit()
            alert = "수정이 완료되었습니다."
            return redirect(url_for('auth.mypage'))
    return render_template('auth/user_update.html',form=form)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@bp.route('/find_id', methods=('GET','POST'))
def find_id():
    form = FindIdForm()
    if request.method =='POST' and form.validate_on_submit():
        error = None
        user = userInfo.query.filter_by(number=form.number.data).first()
        if not user:
            error = '존재하지 않는 사용자 입니다.'
        else:
            error = '당신의 아이디는 {} 입니다.'.format(user.id)
        flash(error)
    return render_template("auth/find_id.html", form=form)

@bp.route('/find_pw',methods=("GET","POST"))
def find_pw():
    form = FindPasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = userInfo.query.filter_by(id=form.id.data, number=form.number.data).first()
        if not user:
            error = "존재하지 않는 사용자 입니다."
            flash(error)
        else:
            password=string.ascii_letters + string.digits
            result=""
            for i in range(8):
                result +=random.choice(password)
            alert = '당신의 비밀번호는 {}입니다.'.format(result)
            user = userInfo.query.filter_by(id=user.id).update({'pw':generate_password_hash(result)})
            db.session.commit()
        flash(alert)
    return render_template('auth/find_pw.html',form=form)

# 마이페이지
@bp.route('/mypage',methods=["GET","POST"])
def mypage():
    wishmovie=con.wish(g.user.uno)
    wishmovienum=re.findall(r'\d+', str(wishmovie))
    movielist=[]
    for i in wishmovienum:
        movie=con.movieinfo(i)
        movielist.append(movie)
    preflist = con.preflist(g.user.uno)
    prefmovielist=[]
    for i in range(len(preflist)):
        movienum = preflist[i][0]
        movie=con.movieinfo(movienum)
        prefer = (((str(preflist[i][1])).replace("1","좋아요")).replace("0","싫어요"))
        prefmovielist.append([movie,prefer])
    return render_template("auth/user.html",movielist=movielist,prefmovielist=prefmovielist)

@bp.before_app_request
def load_logged_in_user():
    uno = session.get('uno')
    if uno is None:
        g.user = None
    else:
        g.user = userInfo.query.filter_by(uno=uno).first()
        g.movie = preferMovie.query.filter_by(uno=uno).all()
