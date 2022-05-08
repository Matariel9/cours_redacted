import app,pytest
from requests import get

def test_posts_api():
    response=app.api_posts.get('/api/posts')
    assert type(response) == list, "Not a list"

def test_post_api():
    response=app.api_post_one.get('/api/1')
    assert type(response) == dict