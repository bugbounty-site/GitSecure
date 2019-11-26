#!/bin/bash

function find_files(){
  files=$(git diff --name-only --diff-filter=AM HEAD~1..HEAD /github/workspace)
  repoName=$(cd /github/workspace && git remote get-url origin)
}

find_files
python3 /analyze.py --files $files --repoloc /github/workspace --repoName $repoName --url $1
