import dm.pre_processamento as pp
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

t = RegexpTokenizer('[a-zA-Z]+')

print(pp.tokenizar(["ola mundo", "bora ver no que da", "77777"], t))
print(pp.tokenizar(["ola mundo", "bora ver no que da", "77777"]))

print(pp.rem_stopwords("esta frase esteja e um teste não maria"))

sw = stopwords.words('portuguese')
sw.append('maria')
print(pp.rem_stopwords("esta frase esteja e um teste não maria", sw))
