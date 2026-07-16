# Natas Level 8

## Theory

Encoding is not the same as encryption. If an application relies on reversible encoding to protect sensitive data, anyone who understands the encoding process can recover the original value.

## Analysis

The page requested a secret and provided access to its source code. After reviewing the PHP logic, I found that the secret was generated using multiple encoding functions. By understanding the encoding sequence and reversing the operations, I was able to recover the original value.

## What I Learned

- Encoding should not be used to protect sensitive information.
- Source code can reveal how application data is processed.
- Reversible transformations do not provide real security.