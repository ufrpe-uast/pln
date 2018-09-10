from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def classificar(opinioes, polaridades, frase, modelo=MultinomialNB(), ts=.3):
    # XXX: module cross_validation esta depreciada
    dados_teste, dados_val, pols_teste, pols_val = train_test_split(opinioes, polaridades, test_size=ts)

    bag = CountVectorizer()
    bag_treino = bag.fit_transform(dados_teste)
    bag_val = bag.transform(dados_val)

    modelo.fit(bag_treino.toarray(), pols_teste)

    pols_pred_val = modelo.predict(bag_val.toarray())

    bag_teste = bag.transform(frase)

    pols_pred_teste = modelo.predict(bag_teste.toarray())

    return {'pols_val': pols_val,
            'pols_pred_val': pols_pred_val,
            'pols_teste': pols_teste,
            'pols_pred_teste': pols_pred_teste}
