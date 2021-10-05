from sqlalchemy.orm import backref
from webpickle import db

class userInfo(db.Model):
    __tablename__='userInfo'
    __table_args__ = {'extend_existing': True}
    uno = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(120),unique=True, nullable=True)
    pw = db.Column(db.String(200),nullable=True)
    n_name = db.Column(db.String(150), nullable=True)
    uimg = db.Column(db.Text, nullable=True)
    number = db.Column(db.String(200),unique=True)

class movieinfo(db.Model):
    __tablename__='movieinfo'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer)
    mno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    director = db.Column(db.Text)
    actor = db.Column(db.Text)
    country = db.Column(db.Text)
    release = db.Column(db.Text)
    runtime = db.Column(db.Text)
    overview = db.Column(db.Text)
    keywords = db.Column(db.Text)
    genres = db.Column(db.Text)
    img1 = db.Column(db.Text)
    img2 = db.Column(db.Text)
    video = db.Column(db.Text)

class preferMovie(db.Model):
    __tablename__ ='preferMovie'
    __table_args__ = {'extend_existing': True}
    uno = db.Column(db.Integer, db.ForeignKey('userInfo.uno', ondelete='CASCADE'),primary_key=True, nullable=False)
    mno = db.Column(db.Integer, db.ForeignKey('movieinfo.mno', ondelete='CASCADE'),nullable=False)
    mpref = db.Column(db.Integer, nullable=True)
    mwish = db.Column(db.Integer, default='0') 
