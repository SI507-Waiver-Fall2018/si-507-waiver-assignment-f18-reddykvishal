# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

consumer_key = '19nkOPmmXlNwx4ZOFaoyIzdcE'
consumer_secret = 'OA0tEEqw1G56nFPDgKGQLOHgj5tTUnzOiadg3wyxhil2Hbf9Rz'
access_token = '2954313552-KGwTHTSSJxnNwldCSgUICLAYpEuzNvDtut26fMH'
access_token_secret = '2fIiq0jlrykxNjrhvCE7IU1xXwA5VdUWpsLVctVGoXdoY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweetUser = sys.argv[1]
tweetLimit = int(sys.argv[2])
noOfFavs = 0
noOfRetweets = 0

tweets = api.user_timeline(screen_name = tweetUser, include_rts = False, count=tweetLimit )
noOfOriginalTweets = len(tweets)

validTokens = []
stopwords = ["RT", "http", "https"]

for tweet in tweets:
	tweetTokens = nltk.word_tokenize(tweet.text)
	for word in tweetTokens:
		if(word[0].isalpha() and (word not in stopwords)):
			validTokens.append(word)
	noOfRetweets = noOfRetweets + tweet.retweet_count
	noOfFavs = noOfFavs + tweet.favorite_count


verbs = []
adjectives = []
nouns = []


for word,t in nltk.pos_tag(validTokens):
	if(t[0] == "N" and t[1] == "N"):
		nouns.append(word)
	elif(t[0] == "V" and t[1] == "B"):
		verbs.append(word)
	elif(t[0] == "J" and t[1] =="J"):
		adjectives.append(word)


verb_dict = {}
for verb in verbs:
	if verb in verb_dict.keys():
		verb_dict[verb]+=1
	else:
		verb_dict[verb] = 1

adj_dict = {}
for adj in adjectives:
	if adj in adj_dict.keys():
		adj_dict[adj]+=1
	else:
		adj_dict[adj] = 1

noun_dict = {}
for noun in nouns:
	if noun in noun_dict.keys():
		noun_dict[noun]+=1
	else:
		noun_dict[noun] = 1

noun_sorted = sorted(noun_dict.items(), key=lambda kv: kv[1], reverse=True)
verb_sorted = sorted(verb_dict.items(), key=lambda kv: kv[1], reverse=True)
adjective_sorted = sorted(adj_dict.items(), key=lambda kv: kv[1], reverse=True)

commonNouns = noun_sorted[:5]
commonVerbs = verb_sorted[:5]
commonAdjectives = adjective_sorted[:5]
file = open("noun_data.csv", "w")
file.write("Noun,Number\n")
print("USER: " + tweetUser + "\n" + "TWEETS ANALYZED: " + str(tweetLimit))
print("VERBS: ", end=" ")
for item in commonVerbs:
	print(item[0] + "(" + str(item[1]) + ")", end=" ")
print("")
print("NOUNS: ", end=" ")
for item in commonNouns:
	print(item[0] + "(" + str(item[1]) + ")", end=" ")
	file.write(item[0] + ", " + str(item[1]) + "\n")
print("")

print("ADJECTIVES: ", end=" ")
for item in commonAdjectives:
	print(item[0] + "(" + str(item[1]) + ")", end=" ")
print("")
print("ORIGINAL TWEETS: " + str(noOfOriginalTweets))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): " + str(noOfFavs))
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): " + str(noOfRetweets))


file.close()
