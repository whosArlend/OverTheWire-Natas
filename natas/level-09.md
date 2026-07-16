# Natas Level 9

## Theory

Command Injection occurs when user input is passed directly to a system command without proper validation or sanitization. This can allow unintended commands to be executed on the server.

## Analysis

The page provided a search feature. After reviewing the source code, I found that the search input was passed directly into a system command without proper sanitization. By testing the input, I confirmed that it was vulnerable to command injection.

## What I Learned

- User input should never be passed directly to system commands.
- Command Injection can lead to unauthorized command execution.
- Proper input validation or safe APIs should be used to prevent this vulnerability.