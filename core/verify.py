#!/usr/bin/env python3

def check(session, url, path, payloads):

    request = session.get("{}/{}", url, path)

    def check_payload(payload):
        if payload in request:
            print("XSS vuln detected for {}/{}", url, path)
            print("Payload: ", payload)

    for p in payloads:
        check_payload(p)
