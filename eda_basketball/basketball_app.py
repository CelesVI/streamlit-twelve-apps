import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import seaborn as sns

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscrping of NBA player stats data!

""")

st.sidebar.header('User input features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2023))))

#Web scraping of NBA player stats.

@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats

playerstats = load_data(selected_year)

# Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Posistion selection
unique_pos = ["C", "PF", "SF", "PG", "SG"]
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtered data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]
st.header('Display player stats of selected team(s)')
st.write('Data dimension: ' + str(df_selected_team.shape[0])+' rows and ' + str(df_selected_team.shape[1])+ ' columns.')
st.dataframe(df_selected_team.astype(str))

def filedownload(df):
    csv = df.to_csv(index=False)
    base_64 = base64.b64encode(csv.encode()).decode() # Strings <-> bytes conversions.
    href = f'<a href="data:file/csv;base64,{base_64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

#Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('playerstats.csv',index=False)
    df = pd.read_csv('playerstats.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)