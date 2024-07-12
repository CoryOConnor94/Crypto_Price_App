import streamlit as st
from requests import Session
import pandas as pd

# Define the URL for the CoinMarketCap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Define the parameters for the API request
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}

# Define the headers, including the API key secrets
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': st.secrets['API_KEY'],  # Replace with your actual API key
}

# Create a session and update its headers
session = Session()
session.headers.update(headers)

# Define the coin dictionary
coin_dict = {
    'Coin 1': 'BTC',
    'Coin 2': 'SOL',
    'Coin 3': 'BNB',
    'Coin 4': 'JUP',
    'Coin 5': 'PEPE',
    'Coin 6': 'DOGE',
    'Coin 7': 'SHIB',
    'Coin 8': 'DOT',
    'Coin 9': 'HBAR',
}


# Define the round_prices function
def round_prices(price):
    if price > 1:
        rounded_price = round(price, 2)
    else:
        rounded_price = round(price, 8)
    return rounded_price


# Make the API request
response = session.get(url, params=parameters)

# Check if the response status is OK 200
response.raise_for_status()

# Load the response data
data = response.json()

# Initialize lists to store data
symbols = []
names = []
prices = []
percent_change_24h = []

# Iterate over each cryptocurrency in the data list
for crypto in data['data']:
    # Extract relevant information and append to lists
    symbols.append(crypto['symbol'])
    names.append(crypto['name'])
    # Use the round_prices function to format the price
    prices.append(round_prices(crypto['quote']['USD']['price']))
    percent_change_24h.append(crypto['quote']['USD']['percent_change_24h'])

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Symbol': symbols,
    'Name': names,
    'Price': prices,
    'Percent_change_24h': percent_change_24h
})

# Streamlit app titles
st.markdown("# **Crypto Price App**")
st.markdown("*Pulling Crypto prices from CoinMarketCap API*")
st.header("**Selected Price**")


column_1, column_2, column_3 = st.columns(3)
# Loop through selected coin dictionary
for i in range(len(coin_dict.keys())):
    # Retrieve the coin label and index for selected cryptos and apply to sidebar
    selected_coin_label = list(coin_dict.keys())[i]
    selected_coin_index = list(df.Symbol).index(coin_dict[selected_coin_label])
    selected_coin = st.sidebar.selectbox(selected_coin_label, df.Symbol, selected_coin_index, key=str(i))

    # Create dataframe of selected coins
    coin_df = df[df.Symbol == selected_coin]
    # Retrieve selected coins price value from dataframe
    if coin_df.Price.iloc[0] > 0.01:
        coin_price = f'${coin_df.Price.iloc[0]:.2f}'
    else:
        coin_price = f'${coin_df.Price.iloc[0]}'
    # Retrieve percent change value of selected coins over the past 24 hours
    coin_percent_change_24hr = f'{coin_df.Percent_change_24h.iloc[0]:.2f}%'

    # Create 3 columns that will display the selected coins values and price change
    if i < 3:
        with column_1:
            st.metric(selected_coin, coin_price, coin_percent_change_24hr)
    # Add next 3 coins selected to column 2 metric
    if 2 < i < 6:
        with column_2:
            st.metric(selected_coin, coin_price, coin_percent_change_24hr)
    # Add last 3 coins selected to column 3 metric
    if i > 5:
        with column_3:
            st.metric(selected_coin, coin_price, coin_percent_change_24hr)

# Display all coin data
st.dataframe(df)
