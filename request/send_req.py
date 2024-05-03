import httpx


def send_get(url):
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


def send_post(url, post_data):
    response = httpx.post(url, json=post_data)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    get_url = 'https://httpbin.org/get'
    post_url = 'https://httpbin.org/post'
    post_data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}

    get_response = send_get(get_url)
    post_response = send_post(post_url, post_data)

    print(get_response)
    print(post_response)
