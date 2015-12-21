"""
Simple module to interact with Fieldbook (fieldbook.com)

Every function needs 3 standard args, an api key, a book id to work with, and a
table to work with. They are the first three args in that order. From there,
each function has different args.

:function get: Get data from Fieldbook
:function update: Change data in Fieldbook
:function delete: Delete data from Fieldbook
:function create: Add new data to Fieldbook
"""

import json
import requests



global url
url = 'https://api.fieldbook.com/v1/'
global headers
headers = {'content-type': 'application/json', 'accept':'application/json'}

def get(api_key, book_id, table, row):
    """
    Get data stored in Fieldbook table or row.

    :arg api_key: A tuple with authentication, ex ('key1', '7f7d7s738858f7g')
    :arg book_id: A string with the Fieldbook book id, ex '7s87tt466rg86drg8'
    :arg table: A string with the table from the book, ex 'assignments'
    :arg row: Row number to retrieve, if not positive real no row assumed, ex 1

    :return: Requests object containing request information and json.
    """
    global url
    global headers
    if row < 1:
        final_url = url + book_id + '/' + table
    else:
        final_url = url + book_id + '/' + table + '/' + str(row)
    r = requests.get(final_url, headers = headers, auth = api_key)
    return r


def update(api_key, book_id, table, row, value):
    """
    Update data stored in Fieldbook table to new values.

    :arg api_key: A tuple with authentication, ex ('key1', '7f7d7s738858f7g')
    :arg book_id: A string with the Fieldbook book id, ex '7s87tt466rg86drg8'
    :arg table: A string with the table from the book, ex 'assignments'
    :arg row: Row number to update, ex 1
    :arg value: Dict containing values to be updated in column:value form,
        ex {'task':'Clean', 'length':'10 minutes'}

    :return: Requests object containing request information and json.
    """
    global url
    global headers
    final_url = url + book_id + '/' + table + '/' + str(row)
    r = requests.patch(final_url, json.dumps(value),
                       headers = headers, auth = api_key)
    return r


def delete(api_key, book_id, table, row):
    """
    Delete data stored in Fieldbook table.

    :arg api_key: A tuple with authentication, ex ('key1', '7f7d7s738858f7g')
    :arg book_id: A string with the Fieldbook book id, ex '7s87tt466rg86drg8'
    :arg table: A string with the table from the book, ex 'assignments'
    :arg row: Row number to delete, ex 1

    :return: Requests object containing request information and json.
    """
    global url
    headers = {'accept':'application/json'}
    final_url = url + book_id + '/' + table + '/' + str(row)
    r = requests.delete(final_url, headers = headers, auth = api_key)
    return r


def create(api_key, book_id, table, value):
    """
    Create new row in Fieldbook table.

    :arg api_key: A tuple with authentication, ex ('key1', '7f7d7s738858f7g')
    :arg book_id: A string with the Fieldbook book id, ex '7s87tt466rg86drg8'
    :arg table: A string with the table from the book, ex 'assignments'
    :arg value: Dict containing values for new row in column:value form,
        ex {'task':'Clean', 'length':'10 minutes'}

    :return: Requests object containing request information and json.
    """
    global url
    global headers
    final_url = url + book_id + '/' + table
    r = requests.post(final_url, json.dumps(value), headers = headers,
                      auth = api_key)
    return r
