import streamlit as st
import pandas as pd 
import pickle
import shap
#import sklearn

import pandas as pd
#import seaborn as sn
#import numpy as np
import matplotlib.pyplot as plt

#from pandasql import sqldf
from streamlit_shap import st_shap
#import streamlit.components.v1 as components






st.set_page_config(page_title = "my app" , page_icon = ":tada:", layout="wide")

#-----Header Section-------
with st.container():
    st.subheader("Hi, I am Bahar :wave:")
    st.title("New York Housing Price Prediction App")
    st.write("Here is a housing price prediction app built on NYC Zillow data using CatBoost. Go aheah and input your data on the left to see prediction below.")
    st.write("[checkout my github>](https://github.com/baharbiazar)")

#-------  What I do --------
with st.container():
    st.write("---")



# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters') 


def user_input_features():
    bedrooms = st.sidebar.slider('bedrooms',int(1), int(9), int(3))
    bathrooms = st.sidebar.slider('bathrooms', int(1), int(9), int(2))
    yearBuilt = st.sidebar.slider('yearBuilt', int(1860), int(2020), int(1980))
    property_tax = st.sidebar.slider('propTax', float(0.65), float(0.95), float(0.8))
    living_area = st.sidebar.slider('livingArea', int(400), int(6500), int(2500))
    lot_size_sqft = st.sidebar.slider('lot_size_sqf', int(400), int(10000), int(5000))
    school_rank = st.sidebar.slider('schlRnk', int(1), int(10), int(5))
    hoa = st.sidebar.slider('hoa', int(0), int(1500), int(300), step= 10)
    has_fireplace = st.sidebar.slider('hasFireplace', int(0), int(1), int(1))
    garage_spaces = st.sidebar.slider('garageSpaces', int(0), int(10), int(2))
    has_basement = st.sidebar.slider('basement', int(0), int(1), int(1))
    latitude = st.sidebar.slider('latitude', float(40.49), float(40.91), float(40.6))
    longitude = st.sidebar.slider('longitude', float(-75), float(-73.7), float(-74.1))
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

user_df = user_input_features()

# Print specified input parameters
st.header('Specified Input Parameters')
st.write(user_df)
st.write('---')


#model
filename = "finalized_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))
prediction = loaded_model.predict(user_df)


st.header('Price Prediction')
##st.write(prediction)

# bigger table
pred = pd.DataFrame(
                  prediction,
                  columns=['perdiction'])

st.write(pred)  # Same as st.dataframe(df)

st.write('---')

# SHAP values 


st.subheader('SHAP Values')


#def st_shap(plot, height=None):
    #shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    #components.html(shap_html, height=height)

# compute SHAP values
explainer = shap.Explainer(loaded_model)
shap_values = explainer.shap_values(user_df)

#print(shap_values)

#st.write(shap_values[0][-1])

# Plot the SHAP values
st_shap(shap.force_plot(explainer.expected_value, shap_values, user_df.columns.tolist(), matplotlib=True))

#shap.summary_plot(shap_values, user_df, plot_type="bar")

st.subheader('Summary plot of SHAP values')
#shap.summary_plot(shap_values, user_df)

# Create the summary plot object


fig_summary = shap.summary_plot(shap_values, user_df,  plot_size=(15, 5))

# Display the plot in Streamlit
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig_summary)
