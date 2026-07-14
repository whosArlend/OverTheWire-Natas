# Natas Level 2

## Theory

Web pages often load additional resources such as images, CSS, and JavaScript files. If a web server is misconfigured, directories containing these files may be publicly accessible.

## Analysis

The page suggested there was nothing to see, so I inspected the source code using **F12**. I noticed an image loaded from a directory on the server. After exploring that directory, I found that directory listing was enabled, exposing files that should not have been publicly accessible.

## What I Learned

- Website resources can reveal additional directories.
- Directory listing can expose sensitive files if left enabled.
- Server configuration is just as important as application security.