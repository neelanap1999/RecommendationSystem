import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c2f9fdd8825f92b6aa56719956327975'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']



def recommend(movie):
    index = movies[movies['title'] == str(selected_movie_name)].index[0]
    sim = similarity[index]
    movie_list = sorted(list(enumerate(sim)),reverse=True , key = lambda x : x[1])[1:6]
    y = []
    recommendation_movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendation_movie_poster.append(fetch_poster(movie_id))
        y.append(movies.iloc[i[0]].title)
    return y,recommendation_movie_poster


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Select Movie',
    movies['title'].values)

if st.button('Recommend'):
    recommendations,movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(movie_posters[0])

    with col2:
        st.text(recommendations[1])
        st.image(movie_posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(movie_posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(movie_posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(movie_posters[4])


