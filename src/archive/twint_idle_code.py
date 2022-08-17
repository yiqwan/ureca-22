import twint
import pandas

c = twint.Config()

# # # Specify date # # #

#c.Since = "2021-11-01"
c.Until = "2022-01-28"
c.Limit = 200000000000 # multiple of 20 # upper limit of search

c.Search = "covid OR omicron"  # Use "AND OR" in the string to include words in search"
c.Lang = "en"
# c.Verified = False # verified users
c.Count = True

# # # Specify location # # #
#c.Near = "Singapore"
c.Geo = "1.352449,103.795754,13km" # latitude, longitude, radius(km)

c.Show_hashtags = True

# c.Output_csv = True
# c.Output = 'raw_tweets_omicron_20112021-31122021.csv' # It will add onto the file, not replace
c.Pandas = True
# c.Pandas_clean = True
twint.run.Search(c)

df = twint.storage.panda.Tweets_df
df.to_csv("raw_tweets_test4.csv")
