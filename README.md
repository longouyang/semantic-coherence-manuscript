LaTeX files for the scientific report by Long Ouyang, Lera Boroditsky, & Michael C. Frank: "Semantic coherence facilitates learning word meanings through contextual co-occurrence".

# BibTeX

The BibTeX file is exported from Long's library in Papers.app. I chose to retain its [universal citekeys](http://web.archive.org/web/20121023113351/http://support.mekentosj.com/kb/read-write-cite/universal-citekey)

These are not so easy to type while editing, though, so I use the following Emacs regexp to convert those citekeys to more usable ones:

replace:

`@\([a-z]+\){\([^:]+\):\([0-9]+\).+`

with:
`@\1{\,(downcase \2)\3,`

(HT [StackOverflow](http://stackoverflow.com/a/677033/351392) for the downcase syntax).

This involves a little bit of manual work, as it makes the two Saffran references have the same citekey.
