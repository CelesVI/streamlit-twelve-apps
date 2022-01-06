import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

penguins = pd.read_csv('penguins_cleaned.csv')

df = penguins.copy()
# Set target for predict.
target = 'species'

# Qualitative encode to predict the penguin's specie.
encode = ['sex', 'island']

# Encoding sex and island to dataset.
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

target_mapper = {'Adelie': 0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

X = df.drop('species', axis=1)
Y = df['species']

# Build random forest model.
classification = RandomForestClassifier()
classification.fit(X,Y)

# Sacve the model with pickle
pickle.dump(classification, open('penguins_clf.pkl', 'wb'))

