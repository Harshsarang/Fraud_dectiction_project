import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/ {}?api_key=4e0e1d79d4b3ad7998770663f336b2ba&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.loads(open('movies_dict.pkl', 'rb').read())
movies = pd.DataFrame(movies_dict)

similarity = pickle.loads(open('similarity.pkl', 'rb').read())

st.title('Movie Recommendation System')

selected_movies_name = st.selectbox(
    'How you like to be contacted?',
    movies['title'].values
)

if st.button('Get Movie Recommendations'):
    names, posters = recommend(selected_movies_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])

