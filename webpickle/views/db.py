import sqlite3
import datetime
from flask import render_template
class Con_DB:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname, check_same_thread=False)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    # 메인
    def img_random(self):
        sql = 'select mno, title, img1, img2, video, release, country from movieinfo ORDER by random() LIMIT 20;'
        self.cur.execute(sql)
        movie= self.cur.fetchall()
        return movie

    # 검색 
    def search(self,m_search):
        sql = 'select mno, title, img1 , release, keywords from movieinfo where title like "%{}%";'.format(m_search)
        self.cur.execute(sql)
        s_movie = self.cur.fetchall()
        movie_count = len(s_movie)
        print(s_movie)
        return s_movie, movie_count, m_search
    
    # 찜 함수 시 찜 
    def wish(self,uno):
        sql = 'select mno from preferMovie where uno={};'.format(uno)
        self.cur.execute(sql)
        wishmovie = self.cur.fetchall()
        return wishmovie

    def mainwish(self):
        sql = 'select mno, title, img1, release, keywords from movieinfo where mno=1 or mno=2 or mno=3 or mno=4 or mno=5 or mno=6 or mno=7 or mno=8 or mno=9 or mno=10 or mno=11 or mno=12 or mno=13 or mno=14 or mno=15 or mno=16 or mno=17;'
        self.cur.execute(sql)
        mainwish =self.cur.fetchall()
        return mainwish

    #  마이페이지내 찜 영화 확인 
    def movieinfo(self,mno):
        sql='select title, img1,img2 from movieinfo where mno={};'.format(mno)
        self.cur.execute(sql)
        wishmovieinfo=self.cur.fetchall()
        return wishmovieinfo

    #  선호도
    def pref(self,uno, mno):
        sql = 'select mpref from preferMovie where uno={} and mno={};'.format(uno,mno)
        self.cur.execute(sql)
        prefnum= self.cur.fetchall()
        return prefnum

    #마이페이지내 선호도 
    def preflist(self,uno):
        sql ='select mno,mpref from preferMovie where uno={} and (mpref=0 or mpref=1);'.format(uno)
        self.cur.execute(sql)
        preflist = self.cur.fetchall()
        return preflist
    
    def mprefinfo(self,mno):
        sql='select title, img1,img2 from movieinfo where mno={};'.format(mno)
        self.cur.execute(sql)
        mprefinfo = self.cur.fetchall()
        return mprefinfo

        #선호도 페이지 
    def like_img(self):
        sql = 'select mno, title, img1, release, country from movieinfo ORDER by random() LIMIT 150;'
        self.cur.execute(sql)
        movie= self.cur.fetchall()
        return movie

    def like_insert(self,uno,mno,mpref):
        sql_insert = 'insert into preferMovie(uno,mno, mpref) VALUES ({}, {}, {});'.format(uno,mno,mpref)
        self.cur.execute(sql_insert)
        like_insert= self.cur.fetchall()
        return like_insert

    # 메인 내 찜 
    def mainpick(self,uno):
        sql = 'select mno from prefermovie where uno={} and mwish=1;'.format(uno)
        self.cur.execute(sql)
        mainpick=self.cur.fetchall()
        return mainpick