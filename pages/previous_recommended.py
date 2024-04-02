import streamlit as st
import pickle
import requests
# from sqlalchemy import create_engine, text
from pages import globals 
from pages.login_page import login

st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        [data-testid="stSidebarContent"] {
            display: none
        }
        [data-testid="stSidebar"] {
            display: none
        }
    </style>
    """,unsafe_allow_html=True,)

def recommended_movies():
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        [data-testid="stSidebarContent"] {
            display: none
        }
        [data-testid="stSidebar"] {
            display: none
        }
    </style>
    """,unsafe_allow_html=True,)
    
    st.markdown(
    """
    <style>
        
        .btn {
            background-color: #ffffff;
            color: #000000;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px 20px;
            text-decoration: none;
            transition: all 0.3s ease;
            margin-left:400px;
        }
        .btn:hover {
            background-color: #008080;
            color: #ffffff;
            text-decoration: none;
        }
        
    </style>
    """, unsafe_allow_html=True
    )

    st.markdown(
        """
            
                    <a href="http://localhost:8501/home_page" target='_self' class="btn">Back</a>
            
            """, unsafe_allow_html=True
    )

    st.header("Previously Recommended Movies")
    user = globals.get_user()
    conn = st.connection('mysql', type='sql')

        # Perform query
    query = f"SELECT * FROM users WHERE email = '{user}';"
    df = conn.query(query, ttl=600)

    if user is None:
        st.error("User not logged in.")
        st.write("Please login to view previously recommended movies.")
        return

    # Fetch previously liked movie from the database
    # selected_movie = None
    selected_movie = df.iloc[0].recently_liked
    st.write(selected_movie)
    # Load the movie list and similarity data
    movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl','rb'))
    
    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies_name = []
        
        for i in distances[1:11]:
            
            recommended_movies_name.append(movies.iloc[i[0]].title)
        return recommended_movies_name

    # Get recommendations for the previously liked movie
    if selected_movie:
        recommended_movies_name = recommend(selected_movie)
        
    else:
        st.write("We have no data to show!! Please use recommendation system")
        return

    # Display recommended movies
    for i, movie_title in enumerate(recommended_movies_name[:10]):
        st.markdown(f"{i+1}. {movie_title}")

    st.write("Recommended similar movies will be displayed here.")

if __name__ == "__main__":
    recommended_movies()
