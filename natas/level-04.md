# Natas Level 4

## Theory

HTTP requests include headers that provide additional information to the server. One of these is the `Referer` header, which indicates the page from which the request originated. Since request headers can be modified by the client, they should not be trusted as a security mechanism.

## Analysis

The page indicated that access depended on the request's origin. I intercepted the request using **Burp Suite**, modified the `Referer` header to the expected value, and forwarded the request. The server accepted the modified header and granted access.

## What I Learned

- HTTP request headers can be modified by the client.
- The `Referer` header should not be used for authorization.
- Burp Suite is useful for inspecting and modifying HTTP requests.