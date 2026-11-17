import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("AB_NYC_2019.csv")

df = load_data()

st.title("AirBnB listings around NYC")

min_price = int(df["price"].min())
max_price = int(df["price"].max())
if max_price > 1000:
    max_price = 1000

price_range = st.slider("Price range ($ per night)", min_value=min_price, max_value=max_price,value=(0, 150))

filtered = df[df["price"].between(price_range[0], price_range[1])]

st.write(f"Showing {len(filtered):,} listings")
st.map(filtered, alt="Airbnb listings in NYC filtered by price")
