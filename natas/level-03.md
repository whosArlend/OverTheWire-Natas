# Natas Level 3

## Theory

The `robots.txt` file tells search engine crawlers which parts of a website should not be indexed. It is not a security feature, as anyone can still access the file and the listed paths.

## Analysis

I inspected the page source using **F12** and found a comment hinting that search engines should not find certain content. This led me to check the `robots.txt` file, which revealed a directory that was still publicly accessible.

## What I Learned

- `robots.txt` is intended for search engine crawlers, not access control.
- Comments in HTML can unintentionally reveal useful information.
- Sensitive resources should never rely on `robots.txt` for protection.