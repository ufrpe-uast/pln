import re
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# regexes uteis
regexes = [ r"@[\w]+" # mentions
          , r"#[\w]+" # hashtags
          , r"\w+:(\/?\/?)[^\s]+" # urls
          ]

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
def stemming(string, stemmer=PorterStemmer()):
    tokens = word_tokenize(string)

    return [stemmer.stem(t) for t in tokens]

# rem_regexp : [regexp] -> string -> string
def rem_regexp(regexps, texto):
    for r in regexps:
        texto = re.sub(r, "", texto)

    return texto

def rem_emojis(texto):
    # https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
    # XXX: Nem todos os emojis são removidos. Isso pq esses ranges são de versões mais antigas. Adicionar mais ranges.
    # https://www.unicode.org/emoji/charts-11.0/emoji-list.html
    emoji_pattern = re.compile("["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', texto)
