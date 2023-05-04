![](https://cdn.shopify.com/s/files/1/0902/2046/products/NYC-Rowhouses-final-2000px-w_1200x1200.jpg?v=1661202266)

# NYC Housing Price Prediction & Streamlit App 
The goal of this project is to use regression models in predicting housing prices and to deploy the final model so everyone can have access to it.  
[Click to access App](https://baharbiazar-nyhousing-app-3l9e70.streamlit.app/)
## Data
Data is from [Kaggle](https://www.kaggle.com/datasets/ericpierce/new-york-housing-zillow-api), which was originally collected on 1/20/21 and consists of 75,629 housing listings on Zillow.com using Zillow's API. Each listing has 1507 attributes that makes data processing and feature selection very time consuming.
Final columns used in the model are:    
Heads up: This model is based on 2021 and current year predictions require retraining the model with most recent data.
## Models
## Performance

## App
Please look at app.py for more information or go to Streamlit link to see some predictions.
## Takeaways
- Knowing the data and preparing the right features are keystone, yet the most time consuming part of of any ML model. 
- Be aware of outliers! Look at what's available and what outliers to take out. Some need domain knowladge and some are some are detecable by simpl looking at the distribution graphs. If you don't see many data points around a certain value it might impact your predictios drastcally. It's better to take those outliers out.
- Make sure to know what you will be predicting for. 
## Next Steps
