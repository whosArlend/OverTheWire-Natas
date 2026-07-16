# Natas Level 10

## Theory

Blacklisting specific characters is not a reliable way to prevent command injection. Attackers may still find alternative inputs that bypass the filter.

## Analysis

This level was similar to the previous one, but several special characters commonly used for command injection were filtered. After reviewing the source code, I observed that the filtering relied on a blacklist rather than securely handling user input. By testing alternative input patterns, I confirmed that the filter could still be bypassed.

## What I Learned

- Blacklist-based filtering is not sufficient to prevent command injection.
- Input validation should use safer approaches instead of blocking only selected characters.
- Understanding how an application processes input is essential when evaluating its security.