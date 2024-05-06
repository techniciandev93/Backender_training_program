import pytest

from send_req import send_get, send_post


@pytest.fixture
def httpbin_url():
    return "https://httpbin.org"


def test_send_get(httpbin_url):
    url = f"{httpbin_url}/get"
    response = send_get(url)
    assert response["url"] == url
    assert response["args"] == {}


def test_send_post(httpbin_url):
    url = f"{httpbin_url}/post"
    post_data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
    response = send_post(url, post_data)
    assert response["url"] == url
    assert response["json"] == post_data
