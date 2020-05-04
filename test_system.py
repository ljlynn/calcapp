'''
Unit test code for the calculator app website.
'''

import requests

def test_website_load():
    '''
    Test loads the calcapp website and expects to get an HTTP 200 returned.
    '''
    get_headers = {"Accpet": "text/html"}
    site_resp = requests.get('http://localhost:5000', headers=get_headers)
    assert site_resp.status_code == 200

def test_get_bad_page():
    '''
    Simulate loading a page that doesn't exist
    '''
    get_headers = {"Accpet": "text/html"}
    get_resp = requests.get(
        "http://localhost:5000/bad",
        headers=get_headers
    )
    assert get_resp.status_code == 404

def test_submit_form():
    post_headers = {
        "Accept": "text/html",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    post_resp = requests.post(
        "http://localhost:5000",
        headers=post_headers,
        data="first_number=2&second_number=2"
    )
    assert post_resp.status_code == 200
    assert "The sum of 2 and 2 is 4" in post_resp.text