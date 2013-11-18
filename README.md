LaTeX files for the scientific report:

**Semantic coherence facilitates learning word meanings through contextual co-occurrence**

by Long Ouyang, Lera Boroditsky, and Michael C. Frank

# BibTeX

The BibTeX file is exported from Long's library in Papers.app. I chose to retain its [universal citekeys](http://web.archive.org/web/20121023113351/http://support.mekentosj.com/kb/read-write-cite/universal-citekey)

These are not so easy to type while editing, though, so I use the following Emacs regexp to convert those citekeys to more usable ones:

-- replace: `@\([a-z]+\){\([^:]+\):\([0-9]+\).+`

-- with: `@\1{\,(downcase \2)\3,`

(HT [StackOverflow](http://stackoverflow.com/a/677033/351392) for the downcase syntax).

This involves a little bit of manual work, as it makes the two Saffran references have the same citekey.

# Converting to Word

Lera preferred to give edits / comments in a Word file.

## pdftoword.com

This seemed to have the best tradeoff between quality and ease.

Apparently Acrobat Pro can also export to doc, so that might be worth trying.

## htlatex (tex -> html -> word)

Idea is to use htlatex to convert tex to html: `htlatex report.tex "0,fn-in"`

(HT http://tug.org/pipermail/tex4ht/2011q1/000250.html for the "fn-in" syntax)

This approach doesn't work with PDFs, but EPS files will work: `pstopdf -eps foo.pdf`

And then open your html file in word, save as a doc. The resulting doc file doesn't look as good as the pdftoword.com version, though.

## latex2html (tex -> html -> word)

Made a small attempt at the approach advocated at http://askubuntu.com/a/239332

Couldn't get this to work on my laptop, probably due to MacPorts versus MacTeX issues.

A little more success on an Ubuntu machine, but made complaints like:

    pstoimg: Error: "/usr/bin/pnmcrop -verbose  < /tmp/l2h10159/p10237.pnm | /usr/bin/pnmcrop -verbose  -bot -sides  -sides  | /usr/bin/pnmcrop -verbose  -l -sides  -sides   > /tmp/l2h10159/p10237.t00" failed: Illegal seek
    
and:

    No implementation found for style `apa6'
    No implementation found for style `graphicx'
    No implementation found for style `geometry'
    No implementation found for style `hyperref'
    No implementation found for style `apacite'
    No implementation found for style `multirow'
    
## tex4ht

## oolatex

## pandoc

Converted .tex to .odt, opened in LibreOffice 4.1:

    pandoc --read latex --write odt --bibliography references.bib --output report.odt report.tex

Looked decent, but:

- `\label` references didn't work
- pandoc complained about missing images
- tables didn't work
- no abstract, front matter, or running head
