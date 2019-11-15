#!/bin/sh -l

git diff --name-only --diff-filter=AM HEAD~1..HEAD /github/workspace
