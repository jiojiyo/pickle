from flask import Blueprint, render_template, flash, session, g, request,url_for
from werkzeug.utils import redirect
from .db import Con_DB

con = Con_DB('imdb.db')

from webpickle import db
from webpickle.models import userInfo, movieinfo,preferMovie
from webpickle.forms import UserCreateForm, UserLoginForm,PreferMovieForm

bp = Blueprint('movie',__name__,url_prefix='/movie/')
con = Con_DB('imdb.db')

# @bp.route('/detail/<int:id>/',methods=['POST', 'GET'])
# def detail(id):
#     if request.method=='GET':
#         movie = movieinfo.query.get_or_404(id)
#         actors = movie.actor.split(',')
#         keywords = movie.keywords.split(',')
#         genres = movie.genres.split(',')
#         id = movie.id
#         return render_template('movie/detail2.html', movie=movie,actors=actors,keywords=keywords,genres=genres)

# @bp.route('/moreinfo/<int:id>/')
# def moreinfo(id):
#     movie = movieinfo.query.get_or_404(id)
#     actors = movie.actor.split(',')
#     keywords = movie.keywords.split(',')
#     genres = movie.genres.split(',')
#     return render_template('movie/moreinfo.html', movie=movie,actors=actors,keywords=keywords,genres=genres)

@bp.route('/detail/<int:mno>/',methods=['POST','GET'])
def detail(mno):
    movie_1 = con.img_random()
    movie = movieinfo.query.get(mno)
    video = movie.video
    actors = movie.actor.split(',')
    keywords = movie.keywords.split(',')
    genres = movie.genres.split(',')
    return render_template('movie/detail2.html',movie_1=movie_1,movie=movie,actors=actors,video=video,keywords=keywords,genres=genres)

@bp.route('/pick/<int:mno>/',methods=('POST','GET'))
def pick(mno):
    pick = preferMovie.query.filter_by(uno=g.user.uno, mno=mno, mwish=1).first()
    if not pick:
        pick = preferMovie(uno=g.user.uno,mno=mno, mpref=-1, mwish=1)
        db.session.add(pick)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('movie.detail',mno=mno))
    else:
        pick = preferMovie.query.filter_by(mno=mno, uno=g.user.uno).update({'mwish':1})
        db.session.commit()
        return redirect(url_for('movie.detail',mno=mno))

#디테일 내 영화 선호도 평가> 추
@bp.route('/like/',methods=('POST','GET'))
def like(mno):
    like = preferMovie.query.filter_by(uno=g.user.uno,mno=mno).first()
    if not like:
        form = PreferMovieForm() 
        like = preferMovie(uno=g.user.uno, mno=mno,mpref=form.mpref.data)
        print(like)
        db.session.add(like)
        db.session.commit()
        return redirect(url_for('movie.detail'))
    else:
        prefnum = con.pref()
        print(prefnum)
        return prefnum, redirect(url_for('movie.detail'))

@bp.before_app_request
def load_logged_in_user():
    uno = session.get('uno')
    if uno is None:
        g.user = None
    else:
        g.user = userInfo.query.filter_by(uno=uno).first()
        g.movie = preferMovie.query.filter_by(uno=uno).all()


