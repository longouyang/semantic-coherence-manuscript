 LaTeX files for the scientific report by Long Ouyang, Lera Boroditsky, & Michael C. Frank: "Semantic coherence facilitates learning word meanings through contextual co-occurrence".

# BibTeX

The BibTeX file is exported from Long's library in Papers.app. I chose to retain its [universal citekeys](http://web.archive.org/web/20121023113351/http://support.mekentosj.com/kb/read-write-cite/universal-citekey)

These are not so easy to type while editing, though, so I use the following Emacs regexp to convert those citekeys to more usable ones:

-- replace: `@\([a-z]+\){\([^:]+\):\([0-9]+\).+`

-- with: `@\1{\,(downcase \2)\3,`

(HT [StackOverflow](http://stackoverflow.com/a/677033/351392) for the downcase syntax).

This involves a little bit of manual work, as it makes the two Saffran references have the same citekey.

# Converting to Word

## pdftoword.com

This seemed to have the best tradeoff between quality and ease.

Apparently Acrobat Pro can also export to doc, so that might be worth trying.

## tex -> html -> word (htlatex)

Idea is to use htlatex to convert tex to html: `htlatex report.tex "0,fn-in"`

(HT http://tug.org/pipermail/tex4ht/2011q1/000250.html for the "fn-in" syntax)

This approach doesn't work with PDFs, but EPS files will work: `pstopdf -eps foo.pdf`

And then open your html file in word, save as a doc. The resulting doc file doesn't look as good as the pdftoword.com version, though.

## tex -> html -> word (latex2html)

haven't tried this yet, but see: http://askubuntu.com/a/239332