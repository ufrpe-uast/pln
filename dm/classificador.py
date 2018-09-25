from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# classificar : [string] -> [string] -> [string] -> ?modelo -> ?vec -> float -> {}
def classificar(opinioes, polaridades, frase, modelo=MultinomialNB(), vec=TfidfVectorizer(), ts=.3):
    dados_teste, dados_val, pols_teste, pols_val = train_test_split(opinioes, polaridades, test_size=ts)

    bag_treino = vec.fit_transform(dados_teste)
    bag_val = vec.transform(dados_val)

    modelo.fit(bag_treino.toarray(), pols_teste)

    pols_pred_val = modelo.predict(bag_val.toarray())

    bag_teste = vec.transform(frase)

    pols_pred_teste = modelo.predict(bag_teste.toarray())

    return {'pols_val': pols_val,
            'pols_pred_val': pols_pred_val,
            'pols_teste': pols_teste,
            'pols_pred_teste': pols_pred_teste}
