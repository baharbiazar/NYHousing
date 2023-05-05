![](https://cdn.shopify.com/s/files/1/0902/2046/products/NYC-Rowhouses-final-2000px-w_1200x1200.jpg?v=1661202266)

# NYC Housing Price Prediction & Streamlit App 
The goal of this project is to use regression models in predicting housing prices and to deploy the final model so everyone can have access to it.  
[Click to access Streamlit App](https://baharbiazar-nyhousing-app-3l9e70.streamlit.app/)  
While personally looking for housing, I tried to outline the most important features in determining the price of a property and investigate if there are any other attributes that drive the housing market other than the common knowledge. 
## Data and EDA
Data is from [Kaggle](https://www.kaggle.com/datasets/ericpierce/new-york-housing-zillow-api), which was originally collected on 1/20/21 and consists of 75,629 housing listings on Zillow.com using Zillow's API. Each listing has 1507 attributes that makes data processing and feature selection very time consuming.
Final features used in the model are: number of bedrooms, number of bathrooms, year built, property tax rate, living area, lot size, schools rating, HOA, number of garage spaces, has fireplace, has basement, latitude and longitude.
          

Heads up: This model is based on 2021 and current year predictions require retraining the model with most recent data.

## Models

## Evaluation
![pred](https://user-images.githubusercontent.com/70281148/236564342-86e92752-1539-49f5-8bd6-cfb881c5e336.png)


## App
Please look at app.py for more information or go to Streamlit link to see some predictions.  
[Click to access Streamlit App](https://baharbiazar-nyhousing-app-3l9e70.streamlit.app/) 
## Takeaways
- Knowing the data and preparing the right features are keystone, yet the most time consuming part of of any ML model. 
- Be aware of outliers! Look at what's available and what outliers to take out. Some need domain knowladge and some are detecable simply by looking at the distribution graphs. If you don't see many data points around a certain value it might impact your predictios drastcally. It's better to take those outliers out.
- Make sure to know what you will be predicting for. 
## Next Steps
1- Add more features to the training set  
2- Expand the model to predict current day prices.  
In reality, many factors are involved in this matter and there is a big difference between how much a house is worth and how much it's sold in the market. As I explore more I'll update this repository with my findings.
