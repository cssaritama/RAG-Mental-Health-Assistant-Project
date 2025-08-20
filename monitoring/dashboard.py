#**Author:** Carlos Stalin Saritama Atopo  
#**Email:** cssaritama@gmail.com  
#**Area of Specialization:** Analytics, Advanced Analytics, and Artificial Intelligence  
#**Date:** August 2025 

"""
Monitoring dashboard with 5 concrete charts based on feedback CSV.
CSV expected columns: query,response,feedback,ts,rating,source_snippet
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

st.set_page_config(page_title='Monitoring Dashboard', layout='wide')
st.title('📊 Monitoring Dashboard (Feedback Analytics)')

# Load sample or real feedback data
try:
    df = pd.read_csv('monitoring/user_feedback.csv')
except FileNotFoundError:
    # Create a sample dataframe for demo purposes
    data = [
        ['signs of depression','Answer A','Yes','2025-01-01T12:00:00','5','Depression is common'],
        ['how to manage anxiety','Answer B','Yes','2025-01-02T13:00:00','4','breathing exercises'],
        ['support a friend','Answer C','No','2025-01-03T14:00:00','3','seek professional help'],
        ['sleep problems','Answer D','Yes','2025-01-04T15:00:00','5','sleep hygiene'],
        ['panic attack','Answer E','No','2025-01-05T16:00:00','2','grounding techniques']
    ]
    df = pd.DataFrame(data, columns=['query','response','feedback','ts','rating','source_snippet'])

# Ensure correct types
df['ts'] = pd.to_datetime(df['ts'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0)

# KPI cards
col1, col2, col3 = st.columns(3)
col1.metric('Total feedback', len(df))
col2.metric('Positive feedback count', int((df['feedback']=='Yes').sum()))
col3.metric('Avg rating', round(df['rating'].mean(),2))

# Chart 1: Feedback distribution (Yes/No)
st.subheader('1) Feedback distribution')
fig1, ax1 = plt.subplots()
df['feedback'].value_counts().plot(kind='bar', ax=ax1)
st.pyplot(fig1, use_container_width=True)

# Chart 2: Queries over time (daily counts)
st.subheader('2) Queries over time')
fig2, ax2 = plt.subplots()
if not df['ts'].isna().all():
    daily = df.groupby(df['ts'].dt.date).size()
    daily.plot(ax=ax2)
else:
    ax2.text(0.5, 0.5, 'No timestamped data', ha='center')
st.pyplot(fig2, use_container_width=True)

# Chart 3: Average rating by query (top 5)
st.subheader('3) Average rating by top queries')
top_queries = df.groupby('query')['rating'].mean().sort_values(ascending=False).head(5)
fig3, ax3 = plt.subplots()
top_queries.plot(kind='bar', ax=ax3)
st.pyplot(fig3, use_container_width=True)

# Chart 4: Top source snippets frequency
st.subheader('4) Top source snippets (frequency)')
source_counts = df['source_snippet'].value_counts().head(10)
fig4, ax4 = plt.subplots(figsize=(6,3))
source_counts.plot(kind='barh', ax=ax4)
st.pyplot(fig4, use_container_width=True)

# Chart 5: Sentiment-like proxy: length of response vs rating
st.subheader('5) Response length vs rating (proxy for depth vs helpfulness)')
df['response_len'] = df['response'].apply(lambda x: len(str(x).split()))
fig5, ax5 = plt.subplots()
ax5.scatter(df['response_len'], df['rating'])
ax5.set_xlabel('Response length (words)')
ax5.set_ylabel('Rating (1-5)')
st.pyplot(fig5, use_container_width=True)

st.markdown('**Notes:** For production, connect feedback collection to a DB, add timestamps at ingestion, and include user IDs/hashed identifiers for analysis.')
