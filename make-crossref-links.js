// node url-encode-titles.js titles.txt > lookup-dois.sh

var fs = require('fs');

var encode = function(str) {
  return encodeURIComponent(str).replace(/%20/g, "+")
}

var titles = fs
    .readFileSync(process.argv[2], 'utf8')
    .split('\n')
    .filter(function(x) { return x.length > 0 })
    .map(function(x) { return 'open "http://search.crossref.org/?q=' + encode(x) + '"' })


console.log(titles.join("\nsleep 2\n"));
