from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import stopwords

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
