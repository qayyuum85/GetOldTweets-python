import got3 as got

search_term = 'malaysia daily spending'
search_timeframe = '2017-01-01'
search_language = 'en'
tweetCriteria =  got.manager.TweetCriteria().setQuerySearch(search_term).setSince(search_timeframe).setLang(search_language)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

filename = 'tweetDailySpending.txt'
with open(file=filename, mode='w', encoding='utf-8') as f:
    for tweet in tweets:
        line = tweet.id + "\t" + str(tweet.date) + "\t" + tweet.text + "\n"
        f.write(line)
