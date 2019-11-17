#!/bin/bash


function download_regex() {
  curl -o /tmp/regex.json https://raw.githubusercontent.com/dxa4481/truffleHogRegexes/master/truffleHogRegexes/regexes.json
}

function find_files(){
  files=$(git diff --name-only --diff-filter=AM HEAD~1..HEAD .)
}

download_regex
find_files
python3 /analyze.py $files
