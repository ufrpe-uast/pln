import pandas as pd
import dm.stopwords as sw
import dm.pre_processamento as pp
import dm.classificador as cl

from nltk.util import bigrams
from nltk.tokenize import word_tokenize, RegexpTokenizer

from sklearn.metrics import accuracy_score

dataset = pd.read_csv('/home/d/data/opinioes.csv', usecols=['opiniao', 'polaridade'])

opinioes = dataset['opiniao'].values
polaridades = dataset['polaridade'].values

# 1
opinioespp = [pp.rem_stopwords(pp.rem_regexp(pp.regexes, pp.rem_emojis(o)), blacklist=sw.portugues) for o in opinioes]

t = RegexpTokenizer('[\w]+')
opinioespp = [' '.join(pp.tokenizar_string(o, t)).lower() for o in opinioespp]

# 2
# ngram (bigram)
bigrms = [list(bigrams(word_tokenize(o))) for o in opinioespp]

# stemming
stem = [' '.join(pp.stemming(o)) for o in opinioespp]

# word token
tokens = [word_tokenize(o) for o in opinioespp]

ops_teste = pd.read_csv('/home/d/data/coleta/marina.csv', sep='|')

ops_teste = ops_teste['opiniao'].values

print(ops_teste)

for op in ops_teste:
    pre_pro = pp.stemming(pp.rem_regexp(pp.regexes, pp.rem_emojis(op)))
    if len(pre_pro) > 1:
        res = cl.classificar(stem, polaridades, pre_pro)

        acc = accuracy_score(res['pols_val'], res['pols_pred_val']) * 100

        if res['pols_pred_teste'][0] == 1:
            print('{0:.2f}% - Positivo: {1}'.format(acc, op))
        elif res['pols_pred_teste'][0] == 2:
            print('{0:.2f}% - Negativo: {1}'.format(acc, op))
        else:
            print('Invalido')
