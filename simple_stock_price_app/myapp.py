import yfinance as yf
import streamlit as st
import pandas as pd

#write on app
st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Mercado Libre!

""")

# Company's Symbol
tickerSymbol = 'MELI'

tickerData = yf.Ticker(tickerSymbol)

#Get df
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2021-12-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)