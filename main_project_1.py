import pandas as pd
import streamlit as st
import numpy as np
import snscrape.modules.twitter as sntwitter
import csv

with st.form(key = 'my_form'):
  keyword_input = st.text_input("Enter keyword to scrape : ")
  date1 = st.date_input("Since: ")
  date2 = st.date_input("Uptill: ")
  counter = st.number_input("How many tweets do you want to scrape? : ")
  submit_button = st.form_submit_button("Submit")

tweet_scraped = []

if submit_button:
  for i, tweets in enumerate(sntwitter.TwitterSearchScraper("{} since:{} until:{}".format(keyword_input, date1, date2)).get_items()):
    if i == counter:
      break
    else:
      tweet_scraped.append([tweets.date, tweets.id, tweets.url, tweets.content, tweets.user, tweets.replyCount, tweets.retweetCount, tweets.lang, tweets.source, tweets.likeCount])

df = pd.DataFrame(tweet_scraped, columns = ['date', 'id', 'url', 'tweet content', 'user', 'reply count', 'retweet count', 'language', 'source', 'like count'])
st.dataframe(df)

file1 = df.to_csv(index = False)
st.download_button(label = "Download file as csv", data = file1, file_name = 'twitter_scraped_data.csv')

file2 = df.to_json()
st.download_button(label = "Download file as json", data = file2, file_name = 'twitter_scraped_data.json')



#file1 = df.to_csv("twitter_scraped_data.csv", index = False)