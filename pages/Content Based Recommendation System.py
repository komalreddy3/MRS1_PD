import pandas as pd
import numpy as np

from pickle import load
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Content Based Recommendation", page_icon="🎥",layout="wide")
#st.title("Movie Recommendation System- Content Based")
st.markdown(f'<h1 style="color:#ffffff;font-size:39px;background-color:#000000">{"Movie Recommendation System- Content Based"}</h1>', unsafe_allow_html=True)
#image = Image.open('backgroundj3.jpg')
#st.image(image)
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-attachment: fixed;
             background-position: center;
             background-repeat:no-repeat;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('backgroundj3.jpg')


sig = load(open('sig.pkl','rb'))
#df_act = load(open('MRS1/df.pkl','rb'))
#pd.read_pickle(open('test_report.pickle', 'rb'))
df_act = pd.read_pickle(open('MRS1/df.pkl','rb'))

    # Reverse mapping of indices and movie titles
indices = pd.Series(df_act.index, index = df_act['title']).drop_duplicates()

#movie_name = st.selectbox("Type or select a movie from the dropdown",df_act['title'])
movie_name = st.selectbox(" ",
                                  df_act['title'])

if st.button('Show Recommendation'):
        # Get the index corresponding to original_title
    idx = indices[movie_name]

        # Get the pairwsie similarity scores
    sig_scores = list(enumerate(sig[idx]))

        # Sort the movies
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Scores of the 10 most similar movies
    sig_scores = sig_scores[1:11]

        # Movie indices
    movie_indices = [i[0] for i in sig_scores]

        # Top 10 most similar movies
    for i in df_act['title'].iloc[movie_indices]:
        #st.text(i)
        st.markdown(f'<h1 style="color:#ffffff;font-size:20px;background-color:#000000">{i}</h1>', unsafe_allow_html=True)
