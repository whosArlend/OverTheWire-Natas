# Natas Level 6

## Theory

PHP can include code from other files using statements such as `include` or `require`. If sensitive files are directly accessible, they may expose information that should remain private.

## Analysis

The page provided a link to view the source code. While reviewing the PHP code, I noticed that it included another file containing a secret value. I accessed the included file and inspected its source to understand how the application validated the input.

## What I Learned

- PHP applications may load data from external files.
- Included files should not be publicly accessible if they contain sensitive information.
- Reviewing application source code can reveal implementation details that affect security.