import csv
from tweepy import *

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

# salvar_tweets_csv : string -> int -> ()
def salvar_tweets_csv(usuario, quantidade=10):
    tweets = api.user_timeline(screen_name = usuario, count = quantidade, tweet_mode="extended")

    for tweet in tweets:
        try:
            arquivo = open(usuario + '.csv', mode='a', encoding='utf-8')
            writer = csv.writer(arquivo)

            writer.writerow([tweet.full_text])

            arquivo.close()
        except OSError as e:
            print(e)

qtd = 100
salvar_tweets_csv('cirogomes', qtd)
salvar_tweets_csv('geraldoalckmin', qtd)
salvar_tweets_csv('jairbolsonaro', qtd)
salvar_tweets_csv('MarinaSilva', qtd)
salvar_tweets_csv('Haddad_Fernando', qtd)
