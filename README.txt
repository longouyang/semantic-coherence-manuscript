i've successfully compiled this using vanilla mactex on OS X 10.7.

compiling initially didn't work because, due to a PATH problem, i was actually using a different texlive distribution that lived in /opt/local instead of /usr/local (i think the /opt/local version was an anemic macports install that was missing a bunch of packages). adding /usr/texbin to the beginning of $PATH fixed this for textmate and i had to do the relevant (setenv "PATH" ...) in my .emacs file for emacs.

the bibtex file comes from Mekentosj Papers' export-to-bibtex function. i chose to retain its "universal citekeys" (http://web.archive.org/web/20121023113351/http://support.mekentosj.com/kb/read-write-cite/universal-citekey)