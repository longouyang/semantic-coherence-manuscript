# coding=UTF8
# script for converting Word/Pages-formatted text to LaTeX

text = """
Sentences took the form “M and N” or “P and Q” (see Figure 1). We generated the actual lexical items randomly for each subject. N’s and Q’s were always novel nonsense words and were drawn without replacement from {moke, thite, jiv, pif, dex, wug}. M’s and P’s could be either novel or familiar. Novel M’s were drawn from {feeb, bim, lup} and novel P’s were drawn from {zabe, vap, chuv}. Fa- miliar M’s and P’s obeyed a taxonomic organization – famil- iar M’s were drawn from {hamster, cat, dog} (animal words) and familiar P’s were drawn from {car, bus, truck} (vehi- cle words). To create the audio files, we input the sentences as “X. and. Y.” (e.g., “car. and. chuv.”, including periods) into an American English text-to-speech engine using a fe- male voice. The periods between words introduced substan- tial pauses ranging in length from 150 to 300 ms; piloting revealed that without pauses, it was difficult for participants to distinguish the words. Sentences using only monosyllabic words were around 2 seconds long. Sentences using the sole disyllabic word, hamster, were around 3 seconds long.
The referent assignment task involved visual referents. For the context words, we used 128x128 pixel images of a cat, dog, hamster, car, bus, and truck. For the target words, we used 100x100 pixel images of a horse, rabbit, sheep, bear, goldfish, mouse, boat, van, train, motorcycle, plane, and bi- cycle.
"""

replacements = [
["&", "\&"],
["‘","`"], # open single quote
["’", "'"], # close single quote
['“','``'], # open double quote
['”', "''"], # close double quotes,
['–', '--'] # em dashes
]

for old,new in replacements:
    text = text.replace(old, new)

print text.rstrip().lstrip()

