import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c2100333e202bcdf9a3673f9c344f17b'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]# this code is actually coveerting tbe list into the tuple havinf first elemtn the index, then it sortd=s it in reverse order , and lambda function inspecifying that the sortinf should be done on the basis of second element only
    recommended_movies = []
    recommended_moviesposter = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_moviesposter.append(fetch_poster(movie_id))
    return recommended_movies , recommended_moviesposter
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name= st.selectbox(
'Select a Movie',movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    cols= st.columns(5)
    with cols[0]:
        st.text(names[0])
        st.image(posters[0])
    with cols[1]:
        st.text(names[1])
        st.image(posters[1])
    with cols[2]:
        st.text(names[2])
        st.image(posters[2])
    with cols[3]:
        st.text(names[3])
        st.image(posters[3])
    with cols[4]:
        st.text(names[4])
        st.image(posters[4])

