# XSS-Tester

## Requirements
* Python3+
* requests module

## Usage
```bash

python3 xss -d "example.com" -auth

# or
chmod -x xss
./xss.py -d "example.com" -auth

# or default requires auth, domain to be in json file
./xss.py
```

## Config

Probably the best way to use this as the CLI isn't fully implemented.

```js
// injection and paths arrays must be same size
// keys for auth are whatever is required for auth on example.com
{
   "domain": "example.com",
   "login":  "/login",
   "auth"  : {
      "username": "admin",
      "password": "admin"
   },
   "injection": ["/posts"],
   "paths": ["/posts"]
}
```
