---
word_document: default
author: "Kristel Uiboaed"
date: "25. jaanuar 2017"
output:
  html_document: default
  pdf_document: default
  word_document: default
title: "Sagedusloendid kolmes keeles"
---

## Unix 
``` bash
#!/bin/bash

cat *.txt \
| tr '[:upper:]' '[:lower:]' \
| tr -d '[\.\?!,\":;\)\(]' | tr ' ' '\n' \
| grep -v '^$' \
| sort |  uniq -c | sort -nr \
| sed 's/ *\([0-9]*\) \(.*\)/\2;\1/' > sonavormide-sagedusloend.txt
```
<br><br>
<img src="pythonLogo.png" width="200">

``` python
import re
from operator import itemgetter
import os

failid = [f for f in os.listdir() if f.endswith('.txt')]
sonad = []
sagedused = {}
punkt = re.compile('[.?!,":;)(]')

for fail in failid:
    with open (fail, "r", encoding="utf-8") as sisend:     
            for rida in sisend:
                lause=rida.split()
            for sona in lause:
                sonad.append(punkt.sub("", (sona.lower()).strip()))

for sona in sonad:
    sagedused[sona] = sagedused.get(sona, 0) + 1

with open("sagedusloendPython.csv", "w") as valjund:
    valjund.write("Sona;Sagedus" + "\n")
    for i in sorted(sagedused.items(), key=itemgetter(1), reverse=True):
        valjund.write(i[0] + ";" + str(i[1]) + "\n")
```
<br><br>
<img src="Rlogo.png" width="70">
``` r
sagedusloend <- vector()

korpusefailid <- list.files(pattern="\\.txt")
korpusefailid

for (i in korpusefailid) {
          praeguneFail <- scan(i, what="char", sep="\n", quiet=T, fileEncoding="UTF-8")
          sonad <- unlist(strsplit(praeguneFail, " "))
          eemaldaPunkt <- tolower(gsub("[\\.\\?\\!,\":;\\)\\(]", "", sonad, perl=T))
          sagedusloend <- append(sagedusloend, eemaldaPunkt)
}

sorteeritudTabel <- sort(table(sagedusloend), decreasing=T)
valjundTabel <- paste(names(sorteeritudTabel), sorteeritudTabel, sep=";")

cat("Sona;Sagedus", valjundTabel, file="sagedusLoendR.csv", sep="\n")
```
