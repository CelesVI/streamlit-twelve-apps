import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple  iris flower prediction app

This app predicts the **Iris flower** type 
""")

st.sidebar.header('User input parameters')

#buiding dataframe.
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 4.3, 7.9, 5.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width':petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User inputs parameters')
st.write(df)

# Loading iris dataset for classification.
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# meta estimador averanging the multiples predictions.
classifier = RandomForestClassifier()
classifier.fit(X,Y)

# Making prediction
prediction = classifier.predict(df)

# Prediction probability
prediction_probability = classifier.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_probability)