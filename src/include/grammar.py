'''
Default grammar.
Based on the STTS (https://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/germantagsets/).
'''
LEXIS = {"N": "Noun", "V": "Verb", "ADJ": "Adjective"}
GENUS = {"MASC": "Masculine", "FEM": "Feminine", "NEUT": "Neuter"}
NUMBER = {"SG": "Singular", "PL": "Plural"}
CASES = {"NOM": "Nominative", "GEN": "Genitive", "ACC": "Accusative", "DAT": "Dative"}
MOOD = {"IND": "Indicative", "SBJV": "Subjunctive", "IMP": "Imperative"}
TENSE = {"PST": "Past", "PRES": "Present"}
PERSON = {"1": "First", "2": "Second", "3": "Third"}

GRAMMAR = {"Lexis": LEXIS, "Number": NUMBER, "Cases": CASES, "Mood": MOOD, "Tense": TENSE, "Person": PERSON}