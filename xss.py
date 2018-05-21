#!/usr/bin/env python3

import core, json, sys

def use_cli(args):
    # actually parse this in future
    if (args[1] == "--help"):
        print("With config.json setup as appropriate ->")
        print("Usage: ./xss.py")
        print("With CLI args (all required) ->")
        print("Usage: ./xss.py -d [domain] -u [username] -p [password] -paths [,seperated path]")
        print("Help screen ->")
        print("Usage: ./xss.py --help")
        sys.exit(0)
    # TODO make this actually parse things
    config = {'domain': 'example.com',
              'auth': {'username': 'admin', 'password': 'admin'},
              'paths': ['/']}
    return config

def main():

    if len(sys.argv) > 1:
        config = use_cli(sys.argv)
    else:
        with open("config.json","r") as r:
            config = json.load(r)

    app = core.Injector(config)
    app.run()

if __name__ == '__main__':
    main()
