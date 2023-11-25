from app.models import Genre, Tag, Movie, MovieTag, MovieGenre, User
from app import app, db
from app.encode import blowfish


def load_tags():
    return Tag.query.all()


def load_genres():
    return Genre.query.all()


def load_movies(tag_id=None, genre_id=None, page=None):
    movies = Movie.query

    if tag_id:
        movies = Movie.query.join(MovieTag).filter(MovieTag.tag_id.__eq__(tag_id))
    if genre_id:
        movies = Movie.query.join(MovieGenre).filter(MovieGenre.genre_id.__eq__(genre_id))
    if page:
        page_size = app.config['PAGE_SIZE']
        start = page * page_size - page_size
        end = start + page_size

    return movies.slice(start, end).all()


def count_movie():
    return Movie.query.count()


def check_user_existence(email=None, username=None):
    if email:
        user = User.query.filter(User.email.__eq__(email.strip())).first()
        if user:
            return False
    if username:
        user = User.query.filter(User.username.__eq__(username.strip())).first()
        if user:
            return False

    return True


def add_user(full_name=None, email=None, username=None, password=None, key=None):
    if full_name and email and username and password and key:
        password = blowfish.encrypt(password.strip(), key)
        with app.app_context():
            user = User(full_name=full_name,
                        email=email,
                        username=username,
                        password=password,
                        key=key)

            db.session.add(user)
            db.session.commit()


def get_user_by_id(user_id):
    with app.app_context():
        return User.query.get(user_id)


def check_user_valid(username=None, password=None):
    if username and password:
        with app.app_context():
            user = User.query.filter(User.username.__eq__(username.strip())).first()
            # print(blowfish.encrypt(password.strip(), user.key))
            if blowfish.encrypt(password.strip(), user.key).__eq__(user.password):
                print('here')
                return user

# print(blowfish.decrypt(get_user_by_id(2).password, get_user_by_id(2).key))

# check_user_valid(username='nhung', password='12214567')
