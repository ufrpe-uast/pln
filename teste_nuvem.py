import dm.nuvem_palavras as nu
import dm.pre_processamento as pp
import os

f = open(os.environ['DATADIR'] + '/MarinaSilva.csv', 'r').read()

res = [ r"\w+:(\/?\/?)[^\s]+",
        r"\#.*\b" ]

n = nu.nuvem(pp.rem_stopwords(pp.rem_regexp(res, str(f))))
nu.mostrar_nuvem(n)
