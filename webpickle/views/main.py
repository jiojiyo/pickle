from flask import Blueprint, render_template, flash, session, g, request,url_for,redirect
from flask import current_app as app
from .db import Con_DB
from webpickle import db
from webpickle.models import userInfo, movieinfo,preferMovie
from webpickle.forms import UserCreateForm, UserLoginForm,PreferMovieForm

bp=Blueprint('main', __name__, url_prefix='/')
@bp.route('/')
def index():
    return render_template('index.html')

con = Con_DB('imdb.db')
# 추가할 모듈이 있다면 추가

# 메인 
@bp.route('/main/')
def main():
    movie = con.mainwish()
    movie_1 = con.img_random()
    mainmnolist=[]
    # 쿼리문으로 들고온 movieinfo table의 mno list mainmnolist에 추가(모델 붙일 시 여기 수정)
    for movi in movie:
        mainmno=movi[0]
        mainmnolist.append(mainmno)
    for movie_ in movie_1:
        mainmno_=movie_[0]
        mainmnolist.append(mainmno_)
    print(mainmnolist)
    # prefertable의 찜한 영화 쿼리문으로 mno만 남게 list에 추가 
    mainpicks =con.mainpick(g.user.uno)
    mainpicklist=[]
    for mainpick in mainpicks:
        maini=mainpick[0]
        mainpicklist.append(maini)
    print("mainpicklist:",mainpicklist)
    # 메인에 찍어진 영화와 같은 mno가 있으면 samenolist에 추가 >html template tag로 mno와 비교 
    samemnolist=[]
    for mainpick in mainpicklist:
        print("mainpick:",mainpick)
        if mainpick in mainmnolist:
            samemnolist.append(mainpick)
            print(samemnolist)
    return render_template('/main.html',  movie=movie, movie_1=movie_1, samemnolist=samemnolist)

#검색
@bp.route('/search', methods=['POST', 'GET'])
def search():
    print(request.method)
    if request.method=='GET':
        search_m = request.args.get('search_m')
        search = con.search(search_m)
        return render_template('/search.html', s_movie=search[0], movie_count=search[1], search_m =search_m )
    return render_template('/search.html', movie_count =0)

# 선호도 평가?? 
@bp.route('/movie_like/')
def movie_like():
    # global moviemm
    moviemm = con.like_img()
    return render_template('movie/movie_like.html', moviemm=moviemm)

#선호도 평가
@bp.route('/movie_insert',methods=("GET","POST"))
def movie_insert():
    form = PreferMovieForm()
    if request.method == 'POST':
        movie_insert = preferMovie(uno=g.user.uno, mno=form.mno.data, mpref=form.mpref.data)
        print(movie_insert)
        db.session.add(movie_insert)
        db.session.commit()
        return redirect(url_for('main.main'))
