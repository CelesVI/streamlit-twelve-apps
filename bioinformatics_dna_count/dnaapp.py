import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('images/dna-logo.jpg')

#Allows to expand image.
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA

***
""")
#Title to box.
st.header('Enter DNA sequence')

sequence_input = ">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#Text box to insert dna sequence.
sequence = st.text_area("Sequence input", sequence_input, height=150)
sequence = sequence.splitlines() #Split the sequence name
sequence = sequence[1:] #Skips first line
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

# Prints the input DNA
st.header('Input DNA Query')
sequence

# prints the output dna
st.header('Output DNA Query')

#Dict to count proteins with dict.
st.subheader('Print Dictionary')
def dna_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C')),
    ])
    return d

#Showing dict
axis_x = dna_nucleotide_count(sequence)
axis_x

#axis_x_label = list(axis_x)
#axis_x_values = list(axis_x.values())

#Print text
st.subheader('Print text')
st.write('There are  ' + str(axis_x['A']) + ' adenine (A)')
st.write('There are  ' + str(axis_x['T']) + ' thymine (T)')
st.write('There are  ' + str(axis_x['G']) + ' guanine (G)')
st.write('There are  ' + str(axis_x['C']) + ' cytosine (C)')

# Displying dataframe
st.subheader('Print dataframe')
df = pd.DataFrame.from_dict(axis_x, orient='index')
df = df.rename({0:'count'}, axis='columns') # rename column 0 to count
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

# Displayin bar chart
st.subheader('Display bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p) # To show plot