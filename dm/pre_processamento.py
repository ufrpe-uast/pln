from nltk.tokenize.treebank import TreebankWordTokenizer

# tokenizar : [string] -> function -> [[string]]
def tokenizar(lst, tokenizer=TreebankWordTokenizer()):
    return [tokenizer.tokenize(x) for x in lst]
