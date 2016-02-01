#!/usr/bin/env python
# NB: remember to source env/bin/activate to fire
# up python

import sys, re, bibtexparser, collections, csv

bib_filename=sys.argv[1]
csv_filename=sys.argv[2]

with open(bib_filename) as bibtex_file:
  bibtex_str = bibtex_file.read()

def convert_csv(filename):
  f = open(filename, 'rb')
  rows = []
  for row in csv.DictReader(f):
    rows.append(row)
  return rows

# convert list of dict into a dictionary
# with bibtex ids as keys and dois as values
dois = {}
for row in convert_csv(csv_filename):
  dois[ row["id"] ] = row["doi"]

bib_database = bibtexparser.loads(bibtex_str)

for entry in bib_database.entries:
  # handle capitalized (bibdesk) and noncapitalized (papers) keys
  if ("ID" in entry):
    _id = entry["ID"]
  else:
    _id = entry["id"]

  doi = dois[_id].strip()
  if len(doi) > 0:
     entry["DOI"] = doi

print(bibtexparser.dumps(bib_database).encode('utf-8'))
