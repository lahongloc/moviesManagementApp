from sqlalchemy.orm import relationship

from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, LargeBinary
from enum import Enum as UserEnum
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Tag(BaseModel):
    name = Column(String(50), nullable=False, unique=True)
    note = Column(String(100))
    movie_tags = relationship('MovieTag', backref='tag', lazy=True)

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(1000))
    movie_genres = relationship('MovieGenre', backref='genre', lazy=True)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(500))
    movie_tags = relationship('MovieTag', backref='movie', lazy=True)
    movie_genres = relationship('MovieGenre', backref='movie', lazy=True)

    def __str__(self):
        return self.name


class MovieTag(BaseModel):
    movie_id = Column(Integer, ForeignKey(Movie.id), nullable=False)
    tag_id = Column(Integer, ForeignKey(Tag.id), nullable=False)


class MovieGenre(BaseModel):
    movie_id = Column(Integer, ForeignKey(Movie.id), nullable=False)
    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)


class User(BaseModel, Base, UserMixin):
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    key = Column(LargeBinary)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # t3 = Tag(name='Coming')
        # t2 = Tag(name='Promotion')
        # t1 = Tag(name='Showing')
        # db.session.add_all([t1, t2, t3])
        # db.session.commit()

        # g1 = Genre(name='Action')
        # g2 = Genre(name='Adventure')
        # g3 = Genre(name='Cartoon')
        # g4 = Genre(name='Comedy')
        # g5 = Genre(name='Drama')
        # g6 = Genre(name='Music')
        # g7 = Genre(name='Romantic')
        # db.session.add_all([g1, g2, g3, g4, g5, g6, g7])
        # db.session.commit()

        # m1 = Movie(name='IT’S OKAY TO NOT BE OKAY', price=120000, image='images/p1.png')
        # m2 = Movie(name='SWEET HOME', price=99000, image='images/p2.png')
        # m3 = Movie(name='VAGABOND', price=135000, image='images/p3.png')
        # m4 = Movie(name='CRASH LANDING ON YOU', price=129000, image='images/p4.png')
        # m5 = Movie(name='ROOKIE HISTORIAN GOO HAE RYUNG', price=150000, image='images/p5.png')
        # m6 = Movie(name='WHEN THE CAMELLIA BLOOMS', price=250000, image='images/p6.png')
        # m7 = Movie(name='CHIEF OF STAFF', price=199000, image='images/p7.png')
        # m8 = Movie(name='KINGDOM', price=175000, image='images/p8.png')
        # m9 = Movie(name='ROMANCE IS A BONUS BOOK', price=215000, image='images/p9.png')
        # m10 = Movie(name='MR. SUNSHINE', price=210000, image='images/p10.png')
        # db.session.add_all([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10])
        # db.session.commit()

        # mt1 = MovieTag(movie_id=1, tag_id=1)
        # mt2 = MovieTag(movie_id=2, tag_id=1)
        # mt3 = MovieTag(movie_id=3, tag_id=1)
        # mt4 = MovieTag(movie_id=4, tag_id=1)
        # mt5 = MovieTag(movie_id=5, tag_id=3)
        # mt6 = MovieTag(movie_id=6, tag_id=1)
        # mt7 = MovieTag(movie_id=7, tag_id=1)
        # mt8 = MovieTag(movie_id=8, tag_id=2)
        # mt9 = MovieTag(movie_id=9, tag_id=2)
        # mt10 = MovieTag(movie_id=10, tag_id=1)
        # db.session.add_all([mt1, mt2, mt3, mt4, mt5, mt6, mt7, mt8, mt9, mt10])
        # db.session.commit()

        # mg1 = MovieGenre(movie_id=1, genre_id=7)
        # mg2 = MovieGenre(movie_id=2, genre_id=2)
        # mg3 = MovieGenre(movie_id=3, genre_id=1)
        # mg4 = MovieGenre(movie_id=4, genre_id=5)
        # mg5 = MovieGenre(movie_id=5, genre_id=7)
        # mg6 = MovieGenre(movie_id=6, genre_id=7)
        # mg7 = MovieGenre(movie_id=7, genre_id=1)
        # mg8 = MovieGenre(movie_id=8, genre_id=5)
        # mg9 = MovieGenre(movie_id=9, genre_id=4)
        # mg10 = MovieGenre(movie_id=10, genre_id=5)
        # db.session.add_all([mg1, mg2, mg3, mg4, mg5, mg6, mg7, mg8, mg9, mg10])
        # db.session.commit()
