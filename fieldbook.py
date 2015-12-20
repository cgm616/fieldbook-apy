import json
import requests

global url
url = 'https://api.fieldbook.com/v1/'
global headers
headers = {'content-type': 'application/json', 'accept':'application/json'}

def get(api_key, book_id, table, row):
    global url
    global headers
    if not row:
        final_url = url + book_id + '/' + table
    else:
        final_url = url + book_id + '/' + table + '/' + str(row)
    r = requests.get(final_url, headers = headers, auth = api_key)
    return r


def update(api_key, book_id, table, row, value):
    global url
    global headers
    final_url = url + book_id + '/' + table + '/' + str(row)
    r = requests.patch(final_url, json.dumps(value),
                       headers = headers, auth = api_key)
    return r


def delete(api_key, book_id, table, row):
    global url
    headers = {'accept':'application/json'}
    final_url = url + book_id + '/' + table + '/' + str(row)
    r = requests.delete(final_url, headers = headers, auth = api_key)
    return r


def create(api_key, book_id, table, value):
    global url
    global headers
    final_url = url + book_id + '/' + table
    r = requests.post(final_url, json.dumps(value), headers = headers,
                      auth = api_key)
    return r
