#!/usr/bin/env python
# NB: remember to source env/bin/activate to fire
# up python

import sys, re, bibtexparser, collections

filename=sys.argv[1]

with open(filename) as bibtex_file:
  bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

for entry in bib_database.entries:
 print(entry["title"])
