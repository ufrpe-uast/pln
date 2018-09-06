import dm.nuvem_palavras as nu
import os

f = open(os.environ['DATADIR'] + '/ops-list.txt', 'r').read()
n = nu.nuvem(f)
nu.mostrar_nuvem(n)
