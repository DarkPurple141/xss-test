#!/usr/bin/env python3

def _check_path(session, url, payloads):
    response = session.get(url)
    assert (response.status_code == 200)

    def check_payload(payload):
        if payload in response.text:
            print("XSS vuln detected for {}".format(url))
            print("Payload: ", payload)

    for p in payloads:
        check_payload(p)

def check(session, url, paths, payloads):
    for path in paths:
        request_path = url + "/" + path
        _check_path(session, request_path, payloads)
