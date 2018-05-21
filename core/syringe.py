#!/usr/bin/env python3

def _inject_path(session, url, payloads):
    for p in payloads:
        session.post(url, data=p)

def inject(session, url, paths, payloads):
    for path in paths:
        inject_path = url + path
        _inject_path(session, inject_path, payloads)
