from wordcloud import WordCloud
import matplotlib.pyplot as plt

# nuvem : string|bytes -> WordCloud
def nuvem(words):
    n = WordCloud(width=1920, height=1080).generate(words)
    return n

# mostrar_nuvem : WordCloud -> ()
def mostrar_nuvem(n):
    plt.figure()
    plt.imshow(n)
    plt.axis("off")
    plt.show()
