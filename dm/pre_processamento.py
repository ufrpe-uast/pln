import re
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

# tokenizar_string : string -> function -> [string]
def tokenizar_string(string, tokenizer=TreebankWordTokenizer()):
    return tokenizer.tokenize(string)

# tokenizar : [string] -> function -> [[string]]
def tokenizar(lst, tokenizer=TreebankWordTokenizer()):
    return [tokenizar_string(x, tokenizer) for x in lst]

# rem_stopwords : string -> [string] -> string
def rem_stopwords(string, blacklist=stopwords.words('portuguese')):
    tokens = tokenizar_string(string)

    filtrados = []
    for t in tokens:
        if t.lower() not in blacklist:
            filtrados.append(t)

    return " ".join(filtrados)

# rem_acentos : string -> string
def rem_acentos(string):
    # ¯\_(ツ)_/¯
    string = re.sub(r"([áàâã])", r"a", string)
    string = re.sub(r"([éèêẽ])", r"e", string)
    string = re.sub(r"([íìîĩ])", r"i", string)
    string = re.sub(r"([óòôõ])", r"o", string)
    string = re.sub(r"([úùûũ])", r"u", string)
    string = re.sub(r"(ç)", r"c", string)

    return string

# stemming : string -> function -> [string]
def stemming(string, stemmer=RSLPStemmer()):
    tokens = tokenizar_string(string)

    return [stemmer.stem(t) for t in tokens]
