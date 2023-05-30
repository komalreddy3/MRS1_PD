import pandas as pd
import numpy as np

from pickle import load
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Movie Recommendation System", page_icon="📽️",layout="wide")
#st.title("Movie Recommendation System- Popularity Based")
st.markdown(f'<h1 style="color:#ffffff;font-size:39px;background-color:#000000">{"Movie Recommendation System- Popularity Based"}</h1>', unsafe_allow_html=True)
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
add_bg_from_local('backgroundj2.jpg')

#weight_average = load(open('weight_average.pkl','rb'))
weight_average = pd.read_pickle(open('weight_average.pkl','rb'))
movies_popularity = pd.read_pickle(open('movies_popularity.pkl','rb'))

weight_average = weight_average[['title']]
movies_popularity = movies_popularity[['title']]

#filter = st.selectbox('Select or Type the Recommendation', ('Popularity','Average Votes'))
st.markdown(f'<h1 style="color:#ffffff;font-size:24px;background-color:#000000">{"Select or Type the Recommendation "}</h1>', unsafe_allow_html=True)
filter = st.selectbox(' ', ('Popularity','Average Votes'))


if st.button('Recommend'):
    if filter == 'Popularity':
        #st.header('Top 10 Popular movies')
        st.markdown(f'<h1 style="color:#ffffff;font-size:24px;background-color:#000000">{"Top 10 Popular movies"}</h1>', unsafe_allow_html=True)
        st.text("")
        for i in movies_popularity['title'][0:10]:
            #st.text(i)
            st.markdown(f'<h1 style="color:#ffffff;font-size:20px;background-color:#000000">{i}</h1>', unsafe_allow_html=True)
    if filter == 'Average Votes':
        #st.header('Best Movies by Average Votes')
        st.markdown(f'<h1 style="color:#ffffff;font-size:24px;background-color:#000000">{"Best Movies by Average Votes"}</h1>', unsafe_allow_html=True)
        st.text("")
        for i in weight_average['title'][0:10]:
            #st.text(i)
            st.markdown(f'<h1 style="color:#ffffff;font-size:20px;background-color:#000000">{i}</h1>', unsafe_allow_html=True)
