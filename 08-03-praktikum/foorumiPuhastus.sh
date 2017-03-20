#! /bin/bash

sed -e '1d' \
| egrep '^"' \
| sed 's/^"\(.*\)";FALSE;.*/\1/g' \
| tr -d '[\r"]' \
| tr -d "'" \
| sed 's/RT @[^:]*: //g' \
| sed 's/https[^ ]*//g' \
| sed 's/#[[:alpha:]]*//g' \
| sed 's/@[[:alpha:]]*//g' \
| sed 's/^ //g' \
| sed 's/ $//g' \
| sed 's/<U+00E3>/ä/g'
