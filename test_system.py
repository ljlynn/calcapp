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