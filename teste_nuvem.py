import dm.nuvem_palavras as nu
import dm.pre_processamento as pp
import dm.stopwords as sw
import os

f = open(os.environ['DATADIR'] + '/jairbolsonaro.csv', 'r').read()

res = [ r"\w+:(\/?\/?)[^\s]+",
        r"\#.*\b" ]

stopwords = sw.portugues + ["RT", "rt"]

n = nu.nuvem(pp.rem_stopwords(pp.rem_regexp(res, str(f)), stopwords))
nu.mostrar_nuvem(n)
