import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      country_data = data[0]
      name = country_data['name']['common']
      capital = country_data['capital'][0]
      population = country_data['population']
      region = country_data['region']
      area = country_data['area']
      currencies = country_data['currencies']
      currency_code = list(currencies.keys())[0]  # Get the first currency code
      currency = currencies[currency_code]['name']  # Get the name of that currency
      
      flag = country_data['flags']['png']
      return name, capital, population, area, currency, region, flag
    else:
        return None

def main():
    st.set_page_config(page_title="Country Data Cards App Of Haider", page_icon="🌍", layout="wide")
    st.title("Country Data Cards")
    country_name = st.text_input("Enter the name of a country")
    st.button("Get Data")
    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region, flag = country_info
            st.subheader("Country Data")
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area}")
            st.write(f"Currency: {currency}")
            st.write(f"Region: {region}")
            st.image(flag)
        else:
            st.error("Country not found")
if __name__ == "__main__":
    main()