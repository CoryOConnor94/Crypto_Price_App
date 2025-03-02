# Crypto Price App

## Overview
The **Crypto Price App** is a Streamlit-based web application that fetches and displays cryptocurrency prices using the CoinMarketCap API. The app provides real-time price data for selected cryptocurrencies and allows users to track price changes over the past 24 hours.

## Features
- Fetches live cryptocurrency data from the CoinMarketCap API.
- Displays selected cryptocurrencies and their price changes.
- Rounds prices dynamically based on value.
- Utilizes Streamlit's interactive sidebar for selecting coins.
- Presents data in a clean, structured table and metric format.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/crypto-price-app.git
   ```
2. Navigate to the project directory:
   ```sh
   cd crypto-price-app
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
To use the CoinMarketCap API, you need an API key. Store your API key securely in Streamlit secrets:

1. Create a `.streamlit/secrets.toml` file:
   ```toml
   [secrets]
   API_KEY = "your_coinmarketcap_api_key"
   ```

## Running the Application
To start the Streamlit app, run the following command:
```sh
streamlit run app.py
```

## Usage
- The app will display cryptocurrency prices and allow selection via the sidebar.
- Metrics will show real-time prices and percentage changes.
- A complete list of cryptocurrency data is displayed at the bottom.

## Dependencies
- `streamlit`
- `requests`
- `pandas`

Install them using:
```sh
pip install streamlit requests pandas
```

## License
This project is licensed under the MIT License.


