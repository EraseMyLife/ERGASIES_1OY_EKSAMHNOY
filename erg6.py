import tweepy

Access_Token = 
Access_Secret = 
Consumer_Key =  
Consumer_Secret =  

#Establish Authentication 
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Secret)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

#Asking for user's account, looks for the 10 most recent tweets
user = input("User:")
word_list=[]
persontweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in persontweets:
    word_list.append(tweet.text)
words=[]

#Creating the array
for tweet in word_list:
    splited = tweet.split()
    words = words + splited

#Sorting the array based on length
def SortWords(words):
  words.sort(key=len)
  return words

SortedWords = SortWords(words)

#Printing the results
for k in range(5):
  print(SortedWords[k])

for i in range((len(words)-5), len(words)):
  print(SortedWords[i])


