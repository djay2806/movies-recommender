import pandas as pd
import streamlit as st
import pickle
import pandas
st.title('Movie Recommender System')
similarity = pickle.load(open('similarity.pkl', 'rb'))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    l=[]
    for i in movies_list:
        l.append(movies.iloc[i[0]]['title'])
    return l

movies_dict=pickle.load(open('movies.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
option = st.selectbox(
    "How would you like to be contacted?",
    (movies['title'].values),
)

st.write("You selected:", option)
if st.button("Recommend"):
    recommendation=recommend(option)
    for i in recommendation:
        st.write(i)

