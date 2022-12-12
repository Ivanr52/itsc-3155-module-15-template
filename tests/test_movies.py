from turtle import title
from flask.testing import FlaskClient
from src.models import Movie, db
from app import app


def test_get_all_movies(test_app):
    with app.app_context():

        # Setup
        test_movie = Movie(title='The Dark Knight',
                           director='Christopher Nolan', rating=5)
        db.session.add(test_movie)
        db.session.commit()

        res = test_app.get('/movies')
        page_data = res.data.decode()

        assert f'<td><a href="/movies/{ test_movie.movie_id }">The Dark Knight</a></td>' in page_data
        assert '<td>Christopher Nolan</td>'
