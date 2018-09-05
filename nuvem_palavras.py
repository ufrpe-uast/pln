from wordcloud import WordCloud
import matplotlib.pyplot as plt

# nuvem : [string] -> WordCloud
def nuvem(words):
    n = WordCloud(width=1280, height=720).generate(words)
    return n

# mostrar_nuvem : WordCloud -> ()
def mostrar_nuvem(n):
    plt.figure(figsize=(16,9))
    plt.imshow(n)
    plt.show()
