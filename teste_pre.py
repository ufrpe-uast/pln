import dm.pre_processamento as pp
from nltk.tokenize import RegexpTokenizer

t = RegexpTokenizer('[a-zA-Z]+')

print(pp.tokenizar(["ola mundo", "bora ver no que da", "77777"], t))
print(pp.tokenizar(["ola mundo", "bora ver no que da", "77777"]))
