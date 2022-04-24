import streamlit as st
import pickle
import pandas as pd
import  requests

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# get functions paramter is the api link taken from TMDB website -
# https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
# and api key is taken from TMDB account

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=6c3efdc49e3d3b1cbc917acfc0d18503&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# here our dataset is movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:10]
    
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
          # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

 
    return recommended_movies , recommended_movies_posters


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
     'Select movie name',
     movies['title'].values)

st.write('You selected:', selected_movie_name)


if st.button('Recommend Movies'):
    name , poster = recommend(selected_movie_name)
    
    col1, col2, col3  = st.columns(3)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    
             
    col4, col5 , col6 = st.columns(3)
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4]) 
    with col6:
        st.text(name[5])
        st.image(poster[5])


    col7 , col8, col9 = st.columns(3)
    with col7:
        st.text(name[6])
        st.image(poster[6])
    with col8:
        st.text(name[7])
        st.image(poster[7])
    with col9:
        st.text(name[8])
        st.image(poster[8])
