#!/usr/bin/env python3

def _inject_path(session, url, fields, payloads):
    for p in payloads:
        data = {}
        for f in fields:
            data[f] = p
        session.post(url, data=data)

def inject(session, url, paths, payloads):
    for path in paths:
        inject_path = url + path['path']
        _inject_path(session, inject_path, path['field'], payloads)
