# Natas Level 1

## Theory

Client-side restrictions are not a security mechanism.

## Analysis

The page disables the right-click context menu, but this only affects the browser interface. I opened the browser's Developer Tools by pressing **F12** to inspect the page instead.

## What I Learned

- Client-side restrictions are easy to bypass.
- Browser Developer Tools can still be accessed even when right-click is disabled.
- Sensitive information should never rely on client-side protection.