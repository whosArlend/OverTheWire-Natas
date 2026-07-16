# Natas Level 7

## Theory

Directory Traversal (Path Traversal) occurs when an application accepts file paths from user input without proper validation, allowing access to unintended files on the server.

## Analysis

The application loaded different pages based on a URL parameter. After inspecting the page source using **F12**, I found a hint indicating that the page parameter was responsible for including files. By testing the parameter, I confirmed that it was vulnerable to directory traversal, allowing files outside the intended directory to be accessed.

## What I Learned

- User-controlled file paths should always be validated.
- Directory Traversal can expose sensitive files on the server.
- Input used for file inclusion should be properly restricted.