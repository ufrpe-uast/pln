import pandas as pd
import dm.stopwords as sw
import dm.pre_processamento as pp

from nltk.util import bigrams
from nltk.tokenize import word_tokenize

dataset = pd.read_csv('/home/d/data/coleta/ciro.csv', sep='|', usecols=['opiniao', 'polaridade'])

opinioes = dataset['opiniao'].values
polaridades = dataset['polaridade'].values

# 1
opinioespp = [pp.rem_stopwords(pp.rem_regexp(pp.regexes, pp.rem_emojis(o)), blacklist=sw.portugues) for o in opinioes]

# 2
# ngram (bigram)
bigrms = [list(bigrams(word_tokenize(o))) for o in opinioespp]

# stemming
stem = [' '.join(pp.stemming(o)) for o in opinioespp]

# word token
tokens = [word_tokenize(o) for o in opinioespp]
