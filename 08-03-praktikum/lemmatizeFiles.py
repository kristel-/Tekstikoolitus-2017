'''
Author: Kristel Uiboaed
11.02.2017
Lemmataize txt-files in the working directory.
Output only the first analysis.
'''

from estnltk import Disambiguator
from estnltk.names import TEXT, ANALYSIS, ROOT, POSTAG, FORM
import re
from operator import itemgetter
import os
import os.path

disamb = Disambiguator() # import Disambiguator
unknowns = [] # unknown lemmas
lemmas = [] # lemmas

'''
A function that creates a list of input files within a working directory. Files with txt-extension will be read in.
'''

def myInput():
    files = os.listdir()
    inputFiles = []
    for file in files:
        if file.endswith(".txt"):
            if os.path.isfile(file):
                inputFiles.append(file)
    return inputFiles

inFiles = myInput()

'''
Process input files. Input files in utf-8.
'''

for file in inFiles:
    with open(file, "r", encoding = "utf-8") as inp:
        with open(os.path.splitext(file)[0] + "_lemmad.txt", "w", encoding = "utf-8") as outp:
            lines = inp.readlines()
            lines = [re.sub('\s+', ' ', i.strip()) for i in lines]
            text = disamb.disambiguate(lines)
            for analysis in text:
                for word in analysis.words:
                    firstAnalysis = word[TEXT], word[ANALYSIS][0][ROOT], word[ANALYSIS][0][POSTAG], word[ANALYSIS][0][FORM] # extract only the first analysis
                    if firstAnalysis[2] == 'V' and firstAnalysis[1] != "ei" and firstAnalysis[1] != "ära": # append -ma to verbs, except ei and ära
                        outp.write(re.sub("[=_]", "", firstAnalysis[1]) + 'ma' + ' ')
                    elif firstAnalysis[2] == 'Y':
                        unknowns.append(firstAnalysis[1]) # collect unknown analyses
                        outp.write(re.sub("[=_]", "", firstAnalysis[1]) + ' ')
                    else:
                        outp.write(re.sub("[=_]", "", firstAnalysis[1]) + ' ')

# Output unknown analyzed words on the screen.						
print("\nTokens with unknown POS tag:\n\n")
print(set(unknowns))
print("\n\n")

