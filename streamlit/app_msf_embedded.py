import streamlit as st
import mlflow
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import streamlit.components.v1 as stc
from PIL import Image
import altair as alt
import numpy as np

mlflow.set_tracking_uri('http://localhost:5000')

############################################
# Cargar modelo en Producción desde mlflow #
############################################
def load_model():
    return mlflow.pyfunc.load_model(
        #model_uri=f"models:/msf-quote-increase-dnn-potencial/Production"
        model_uri = f"runs:/3f6294ea4a774e9f993bc7a620b72446/msf-quote-increase-dnn-potencial"
    )

@st.cache_data
def load_data():
    #return pd.read_csv("data/feature_store_clean.csv")
    return pd.read_csv("data/merge_3_feature_store.csv") 


@st.cache_data
def load_data_ranking():
    return pd.read_csv("data/merge_3_feature_store_predictions.csv")

model = load_model()
data = load_data()
data_ranking = load_data_ranking()

# Display the logo using HTML
image = Image.open('images/logo_msf.png')
st.image(image)

col1, col2 = st.columns(2)
with col1:

    "## MSF Quota Increase Predictor"

    contact_id = st.text_input("Enter Contact ID:")

    if st.button("Predict"):
        features = data.loc[data['whoid'] == contact_id]
        #features.drop(columns=['Unnamed: 0','whoid'], inplace=True)
        features.drop(columns=['whoid'], inplace=True)
        features = features.astype(np.float32)

        print(features.values)

        prediction  = model.predict(features.values)
        print(prediction)

        if prediction[0] > 0.7:
            st.write("This customer is likely to increase their recurring quota, the probability is {:.2%}".format(prediction[0][0]))
        else:
            st.write("This customer is unlikely to increase their recurring quota, the probability is {:.2%}".format(prediction[0][0]))

    "## #contacts per range of probabilities"

    # Bin the probability values
    bins = [0, 0.20, 0.40, 0.60, 0.80, 1]
    labels = ['0-0.20', '0.21-0.40', '0.41-0.60', '0.61-0.80', '0.81-1']
    data_ranking['range'] = pd.cut(data_ranking['prediction'], bins=bins, labels=labels, right=False)

    # Count the number of rows within each range
    df_counts = data_ranking['range'].value_counts().reset_index()
    df_counts.columns = ['range', 'Count']

    # Plotting in Streamlit using Altair
    chart = alt.Chart(df_counts).mark_bar().encode(
        x='range:N',
        y='Count:Q',
        color='range:N',
        tooltip=['range', 'Count']
    )#.properties(title='Number of Contacts within Probability Ranges')

    st.write(chart)            

    ###################################################################################
with col2:    

    "## Contacts most likely to increase quota"

    # Drop unwanted columns
    # data_ranking.drop(columns=['Unnamed: 0'], inplace=True)

    # Add a search field for the user to input an ID
    search_id = st.text_input("Search by contact ID:")

    if search_id:
        # Filter the dataframe based on the searched ID
        data_searched = data_ranking[data_ranking['whoid'] == search_id]
        st.write(data_searched.style.hide_index())
    else:
        # If no ID is entered, display the top 20 by default
        data_ranking2 = data_ranking.sort_values(by='prediction', ascending=False).head(30)
        st.write(data_ranking2.style.hide_index())

###################################################################################