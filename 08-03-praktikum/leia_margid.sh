#! /bin/bash

# Kristel Uiboaed
# 26.10.2016


# Create the frequency list of all the characters and exclude:
# English alphabet,
# numbers,
# punctuation.

tr -d '[a-z]' \
| tr -d '[A-Z]' \
| tr -d '[0-9]' \
| tr -d ' ,;.:<>()!?' \
| sed 's/./& /g' \
| tr ' ' '\012'  \
| sort | uniq -c | sort -n


