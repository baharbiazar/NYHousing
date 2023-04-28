import streamlit as st
import pandas as pd 
import pickle
#import sklearn

import pandas as pd
#import seaborn as sn
#import numpy as np
#import matplotlib.pyplot as plt

#from pandasql import sqldf






st.set_page_config(page_title = "my app" , page_icon = ":tada:", layout="wide")

#-----Header Section-------
with st.container():
    st.subheader("Hi, I am Bahar :wave:")
    st.title("New York Housing Price Prediction App")
    st.write("Here to deploy a housing price prediction app built on NYC Zillow data")
    st.write("[checkout my github>](https://github.com/baharbiazar)")

#-------  What I do --------
with st.container():
    st.write("---")



# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters') 


def user_input_features():
    bedrooms = st.sidebar.slider('bedrooms',float(0), float(20), float(3))
    bathrooms = st.sidebar.slider('bathrooms', float(0), float(20), float(2))
    yearBuilt = st.sidebar.slider('yearBuilt', float(1800), float(2023), float(1980))
    property_tax = st.sidebar.slider('propTax', float(0.5), float(1), float(0.8))
    living_area = st.sidebar.slider('livingArea', float(100), float(8000), float(2500))
    lot_size_sqft = st.sidebar.slider('lot_size_sqf', float(0), float(10000), float(5000))
    school_rank = st.sidebar.slider('schlRnk', float(0), float(10), float(5))
    hoa = st.sidebar.slider('hoa', float(0), float(2000), float(300))
    has_fireplace = st.sidebar.slider('hasFireplace', float(0), float(1), float(1))
    garage_spaces = st.sidebar.slider('garageSpaces', float(0), float(10), float(2))
    has_basement = st.sidebar.slider('basement', float(0), float(1), float(1))
    latitude = st.sidebar.slider('latitude', float(40), float(50), float(40.6))
    longitude = st.sidebar.slider('longitude', float(-75), float(-73), float(-74.1))
    data = {'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'yearBuilt': yearBuilt,
            'propTax': property_tax,
            'livingArea': living_area,
            'lot_size_sqf': lot_size_sqft,
            'schlRnk': school_rank,
            'hoa': hoa,
            'garageSpaces': garage_spaces,
            'hasFireplace': has_fireplace,
            'basement': has_basement,
            'latitude': latitude,
            'longitude': longitude}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


# Print specified input parameters
st.header('Specified Input Parameters')
st.write(df)
st.write('---')


#model
filename = "finalized_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))
prediction = loaded_model.predict(df)

print(prediction)

st.header('Price Prediction')
st.write(prediction)
st.write('---')




