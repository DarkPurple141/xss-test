#!/usr/bin/env python3

import requests, verify

PAYLOADS="<script>"

class Injector(object):
    """Attemps to inject toy malicious payloads in website {domain}."""
    def __init__(self, config, payloads=PAYLOADS):
        super(Injector, self).__init__()
        self.domain     = config['domain']

        # paths for injections
        self.post_paths = config['post']

        # paths for checking injections -- must match in length
        # don't need to be different
        self.get_paths  = config['get']

        # creates the session
        self.session = Injector.authenticate(
                        self.domain,
                        config['auth']['path'],
                        config['auth']['creds']
                       )

    def run(self):
        for path in self.get_paths:
            verify.check(self.url, path, payloads)
        print("hello")

    @staticmethod
    def authenticate(path, creds):
        session = requests.Session()
        session.post(path, data=creds)

        return session
