# from flask.testing import FlaskClient

# from src.models import Movie
# from tests.utils import create_movie, refresh_db


# def test_get_all_movies(test_app: FlaskClient):

#     refresh_db()
#     test_movie = create_movie()

#     res = test_app.get('/movies')
#     page_data: str = res.data.decode()

#     assert res.status_code == 200
#     assert f'<td><a href="/movies/{test_movie.movie_id}">The Dark Knight</a></td>' in page_data
#     assert '<td>Christopher Nolan</td>' in page_data
#     assert '<td>5</td>' in page_data
