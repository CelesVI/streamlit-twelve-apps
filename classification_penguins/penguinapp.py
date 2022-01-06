from json import load
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin prediction App

This app predicts the **Palmer Penguin**

""")

st.sidebar.header('User input features')

uploaded_file = st.sidebar.file_uploader('Upload your csv')
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.1, 43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.2, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.1)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0, 6300.0, 4000.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g':body_mass_g,
                'sex':sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# combines user input features with entire penguins deataset.
# This will be useful for the encoding phase.
penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df,penguins], axis=0)

# encoding the original features.
encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1]

st.subheader('User input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awating to csv file...')
    st.write(df)

# Read the saved pickle.
load_classification = pickle.load(open('penguins_clf.pkl', 'rb'))

# Apply model to mak predictions.
prediction = load_classification.predict(df)
prediction_probability = load_classification.predict_proba(df)

st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader("Prediction probability")
st.write(prediction_probability)
