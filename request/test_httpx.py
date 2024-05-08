import pytest
from pytest_httpx import HTTPXMock

from send_req import send_get, send_post


@pytest.fixture
def httpbin_url():
    return "https://httpbin.org"


def test_send_get(httpbin_url, httpx_mock: HTTPXMock):
    url = f"{httpbin_url}/get"
    expected_response = {"url": url, "args": {}}

    httpx_mock.add_response(url=url, json=expected_response)
    response = send_get(url)

    assert response == expected_response


def test_send_post(httpbin_url, httpx_mock: HTTPXMock):
    url = f"{httpbin_url}/post"
    post_data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
    expected_response = {"url": url, "json": post_data}

    httpx_mock.add_response(url=url, json=expected_response)
    response = send_post(url, post_data)

    assert response == expected_response
