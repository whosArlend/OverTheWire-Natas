# Natas Level 5

## Theory

HTTP cookies are used to store session information on the client side. Since cookies are sent with every request, they can be viewed and modified by the client unless protected by proper server-side validation.

## Analysis

The page indicated that I was not logged in. Using **Burp Suite**, I intercepted the request and noticed a cookie named `loggedin` with the value `0`. After changing its value to `1` and forwarding the request, the server treated the session as authenticated.

## What I Learned

- Cookies are stored on the client and can be modified.
- Authentication should always be validated on the server.
- Trusting client-controlled cookies can lead to authorization bypass.