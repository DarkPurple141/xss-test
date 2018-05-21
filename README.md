# XSS-Tester
Automatically tests whether a user provided domain and subpaths within a domain has XSS vulnerabilities. Form fields are required for all paths. Configuration via the config.json file.

## Requirements
* python3+
* requests module

## Usage
```bash
# tbh please just use the json as explained below
./xss.py -d [domain] -u [username] -p [password] -paths [,seperated path]

# or default requires auth, domain to be in json file
./xss.py
```

## config.json

Probably the best way to use this as the CLI isn't fully implemented.

Field | Description | Type
-----|--------|-----
`domain` | The domain being targeted, include `https://` or `http://` | String
`auth` | An object including a login path and fields required for login -- important for session persistence and form abuse on most sites | Object
`auth.path` | The login path | String
`auth.creds` | As above, these are in whatever form is required for login. Fieldnames can be altered if needed, eg. `username` => `user` if that's what site requires | Object
`post` | The form destination path(s) and field(s) for the test. You can have multiple fields in a form on any single path. This is an array to include multiple different possible paths. | Array
`get` | Simpler than post, only requires a path string for each corresponding post path, eg. if there are 10 paths being tested in 'post' there must be 10 paths in 'get' | Array

An example config.json is provided in the repo and as below.

```json
// injection and paths arrays must be same size
// keys for auth are whatever is required for auth on example.com
{
   "domain": "http://example.com",
   "auth"  : {
      "path": "login",
      "creds": {
         "username": "admin",
         "password": "admin"
      }
   },
   "post": [
      {
         "field": ["post"],
         "path" : "/"
      }
   ],
   "get": [""]
}
```
