import dm.pre_processamento as pp
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

t = RegexpTokenizer('[a-zA-Z]+')

print(pp.tokenizar(["ola mundo", "bora ver no que da", "77777"], t))
print(pp.tokenizar(["ola mundo", "bora ver no que da", "77777"]))

print(pp.rem_stopwords("esta frase esteja e um teste não maria"))

sw = stopwords.words('portuguese')
sw.append('maria')
print(pp.rem_stopwords("esta frase esteja e um teste não maria", sw))

print(pp.rem_acentos("olá são às êvõras dizíamos caça única do herói"))

print(pp.stemming("E teile" +
" Quicadinha" +
" E zaga" +
" Jogou" +
" E Teile" +
" Dança do Pombo" +
" Trocada de Braço" +
" Quicada Lateral" +
" E zaga"))

print(pp.rem_emojis("hello world 😡😂🙎🏾🤖🦓"))

print(pp.rem_regexp(pp.regexes, "hahah @maria olha isso. @joao11, @nutello__"))
print(pp.rem_regexp(pp.regexes, "#. #Parliament #Flash_Light #SimpleAssim #2018"))
print(pp.rem_regexp(pp.regexes, "urls https://www.google.com/ https://www.youtube.com/watch?v=istJXUJJP0g https://avatars0.githubusercontent.com/u/6243723?s=400&v=4"))

poema = "Eu não tinha este rosto de hoje, assim calmo, assim triste, assim magro, nem estes olhos tão vazios, nem o lábio amargo."

print(" ".join(pp.stemming(poema)))
