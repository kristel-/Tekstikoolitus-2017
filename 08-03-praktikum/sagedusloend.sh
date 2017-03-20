#!/bin/bash

tr '[:upper:]' '[:lower:]' \
| tr -d '[\.\?\!,\":;\)\(-]' | tr ' ' '\n' \
| grep -v '^$' \
| grep -vwf "stoppsonad.csv" \
| sort |  uniq -c | sort -nr \
| sed 's/ *\([0-9]*\) \(.*\)/\2;\1/' \
| sed '1s/^/Lemma;Sagedus\n/'

