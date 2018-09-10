import pandas as pd
import dm.pre_processamento as pp
import dm.classificador as c

from sklearn.metrics import accuracy_score

dataset = pd.read_csv("/home/d/data/opinioes.csv", usecols=['opiniao', 'polaridade'])

dataset['opiniao'] = pp.tokenizar(dataset['opiniao'])

ops =[" ".join(o) for o in dataset['opiniao'].values]

cl = c.classificar(ops, dataset['polaridade'].values, pp.tokenizar_string("este candidato é totalmente despreparado"))

if cl['pols_pred_teste'][0] == 1:
    print('Positivo')
elif cl['pols_pred_teste'][0] == 2:
    print('Negativo')
else:
    print('Invalido')

acc = accuracy_score(cl['pols_val'], cl['pols_pred_val']) * 100
print('Acuracia: {0:.2f} %'.format(acc))
