### Torwali Morphological Analyzer and Tokenizer
### Overview
This is a repository for **NPFL128** course project. The files in this repository processes **Torwali** texts for Morphological Analysis and Tokenization. **Torwali** is an endangered language spoken in north of Pakistan, written in Perso-Arabic script and have very limited resources and computational support. 

### Tokenization
This project is based on data from a Toolbox file which contains database of the first ever Torwali dictionary, The files contain a python script, which extracts lexical entries from **\lc** fields and the corresponding POS tags from **\ps** fields and stored in a dictionary. Since Arabic script do not use white spaces as boundary markers, the script tokenizes the lexical entries using a max-match algorithm against a given dictionary and prints each tokenized word along with its POS tag. The tokenized results are also saved to a text file. Additionally, the script allows interactive tokenization of input sentences, displaying tokens with their POS tags if available. 

### Morphological Analysis

There are two files used to implement the morphological analysis of Torwali: naeem-trw.trw.lexc file (LEXC) and  naeem-trw.trw.foma file (TWOL). The LEXC file is a morphotactic dictionary that defines root words, morpheme combinations, continuation classes, and weights through Lexicon sections. The TWOL file contains phonological or morphophonological rules that map underlying morphemes to surface forms, accounting for alternations. As Torwali is minimally studied, few phonological rules have been identified, and most of the implementation is handled in the LEXC file. To build the lexicon, a collection of example sentences was tokenized and POS-tagged using a Python script, and the resulting words and tags were added to the LEXC file.

The analyzer covers Nouns for inflection classes like gender (Male, Female and Neuter) and Number (Singular and plural), Adjectives for gender and Number and Verbs for different verb forms and gender as well. Most of the inflection classes which involves attaching a suffix are handled in the lexicon (continuation classes) and nouns which include stem changes are handled through twol rules. Nouns in which the stem changes to mark plurality i-e Torwali masculine nouns become feminine nouns when pluralized and a change in the stem occurs. 

### Future work

The analyser works well for verbs which is the largest category in Torwali when it comes to inflecting, the analyzer also covers Nouns, Adverbs and adjective. The future direction or extension of this work could be addressing the random changes in the stem and the identification of tonal variations (in Nouns) and the distinct behavior of vowel-ending verbs and nouns. Also, there are some nouns which fall under different gender categories but are written in the same way(homonyms), the only difference is tone, which creates ambiguity. 

### Requirements

- Python 3.0
- No external libraries required (only standard Python re module).
- Foma
- Script to invoke Foma:<br> 
   _Open foma and use the following commands to analyze all the words in the input lexc file_<br>
Foma[0]:source D:/naeem-trw.trw.foma<br>
Foma[1]:source D:/naeem-trw.trw.lexc<br>
Foma[2]:read lexc D:/naeem-trw.trw.lexc<br>
Foma[3]:print lower-words>D:/naeem.text

### Files and data







