import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" # Simple Stock Price App
Shown are the stock **closing price** and **volume** of the stock""")

tickerSymbol = 'AADI'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='1d', start='2016-5-31', end='2020-5-31')
st.write(""" **Closing price** """)
st.line_chart(tickerDF.Close)
st.write(""" **Volume of stock** """)
st.line_chart(tickerDF.Volume)
st.sidebar.subheader(' **home** ')
st.sidebar.subheader(' **about** ')