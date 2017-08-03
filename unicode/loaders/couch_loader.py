#!/usr/bin/env python3

import os
import sys
import json
import itertools
import requests
import click

import ucd

DB_ADMIN_USER = os.environ['DB_ADMIN_USER']
DB_ADMIN_PASS = os.environ['DB_ADMIN_PASS']

DB_NAME = 'ucd_name_index'


def fail(msg, url=None):
    print(msg, end='')
    if url:
        print(' URL:\n\t', url)
    sys.exit(1)


class CouchDB():

    def __init__(self, server_url, username, password, check=True):
        self.server_url = server_url
        if check:
            self.connection_check()
        self.auth = username, password

    def connection_check(self):
        resp = requests.get(self.server_url)
        if resp.status_code == 200:
            try:
                msg = resp.json()
            except json.decoder.JSONDecodeError:
                fail('HTTP GET did not return valid JSON.', self.server_url)
            return
        else:
            fail(f'HTTP GET returned status code {resp.status_code}.', self.server_url)

    def create_db(self, db_name, drop=True):
        db_url = self.server_url + '/' + db_name
        if drop:
            resp = requests.delete(db_url, auth=self.auth)
            if resp.status_code == 401:
                fail('Unauthorized: check env vars DB_ADMIN_USER and DB_ADMIN_PASS.',
                     db_url)
        resp = requests.put(db_url, auth=self.auth)
        if resp.status_code == 201:
            print('Database', DB_NAME, 'created. URL:\n\t', db_url)
        else:
            fail(f'HTTP PUT returned status code {resp.status_code}.', db_url)

    def put_document(self, db_name, key, data):
        doc_url = self.server_url + '/' + db_name + '/' + key
        resp = requests.put(doc_url, auth=self.auth, json=data)
        if resp.status_code == 201:
            print('Document', key, 'created. URL:\n\t', doc_url)
        else:
            fail(f'HTTP PUT returned status code {resp.status_code}.', doc_url)



@click.command()
@click.argument('server_url')
@click.argument('rows_to_index', type=click.INT)
def main(server_url, rows_to_index):
    if not all([DB_ADMIN_USER, DB_ADMIN_PASS]):
        print('Both DB_ADMIN_USER and DB_ADMIN_PASS must be set in the environment.')
        sys.exit(1)

    couch = CouchDB(server_url, DB_ADMIN_USER, DB_ADMIN_PASS)
    couch.create_db(DB_NAME)
    data = dict(_id='1', letras=list('ABC'))

    if rows_to_index == 0:
        rows = ucd.parser()
    else:
        rows = itertools.islice(ucd.parser(), rows_to_index)
    inverted_idx = ucd.index(rows)
    for key, value in inverted_idx.items():
        couch.put_document(DB_NAME, key, dict(codes=value))

if __name__ == '__main__':
    main()
