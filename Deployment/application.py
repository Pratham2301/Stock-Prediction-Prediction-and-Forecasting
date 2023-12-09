# Requirements
# pip install streamlit fbprophet yfinance plotly


import streamlit as st
from datetime import date

import yfinance as yf
import prophet
from prophet import Prophet
from prophet.plot  import plot_plotly
from plotly import graph_objs as go
import numpy as np


def app():
	START = "2015-01-01"
	TODAY = date.today().strftime("%Y-%m-%d")

	st.title('Stock Forecast App')
	stocks = ('GOOG', 'AAPL', 'MSFT', 'GME', 'FB','TSLA', 'BTC-USD','AMD', 'SPY')
	selected_stock = st.selectbox('Select dataset for prediction', stocks)

	n_years = st.slider('Years of prediction:', 1, 10)
	period = n_years * 365


	# @st.cache
	@st.cache_data 
	def load_data(ticker):
		data = yf.download(ticker, START, TODAY)
		data.reset_index(inplace=True)
		return data

		
	data_load_state = st.text('Loading data...')
	data = load_data(selected_stock)
	data_load_state.text('Loading data... done!')

	st.subheader('Raw data')
	st.write(data.head())
	st.write(data.tail())

	# Plot raw data
	def plot_raw_data():
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
		fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
		fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
		st.plotly_chart(fig)
		
	plot_raw_data()

	# Predict forecast with Prophet.
	df_train = data[['Date','Close']]
	df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

	m = Prophet()
	m.fit(df_train)
	future = m.make_future_dataframe(periods=period)
	forecast = m.predict(future)

	# Show and plot forecast
	st.subheader('Forecast data')
	# st.write(forecast.head())
	st.write(forecast.tail())
		
	st.write(f'Forecast plot for {n_years} years')
	fig1 = plot_plotly(m, forecast)
	st.plotly_chart(fig1)

	st.write("Forecast components")
	fig2 = m.plot_components(forecast)
	st.write(fig2)


	st.write("Best stock calculation")
	count = 0

	maxx = 0
	best = 'GOOG'

	for i in ('GOOG', 'AAPL', 'MSFT', 'GME','TSLA', 'AMD'):
    
		# count = count + 1
		# if(count==2):
		# 	break

		data1 = load_data(i)
		df_train1 = data1[['Date','Close']]
		df_train1 = df_train1.rename(columns={"Date": "ds", "Close": "y"})

		m1 = Prophet()
		m1.fit(df_train1)
		future1 = m1.make_future_dataframe(periods=10)
		forecast1 = m1.predict(future1)
		arr = np.array(forecast1)
		arr1 = arr[0:1]
		lst = list(arr1)
		st.write(i, lst[0][1])

		if(lst[0][1] > maxx):
			maxx = lst[0][1]
			best = i

	
	st.write("Best stock is: ", i, " with price of: ", maxx)


