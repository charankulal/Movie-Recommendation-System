import streamlit as st
import pickle
import requests


# Define your existing functions here, e.g., recommend, fetch_poster

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


def home():
   

    conn = st.connection('mysql', type='sql')

    # Perform query.
    # query = f"SELECT * FROM users WHERE email = '{email}' ;"
    # df = conn.query(query, ttl=600)
    
    # st.write()

 
        
    st.header("Movies Recommendation System")
    

    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data= requests.get(url=url)
        data=data.json()
        poster_path=data['poster_path']
        full_path="http://image.tmdb.org/t/p/w500/"+poster_path
        return full_path

    def recommend(movie):
        index=movies[movies['title']==movie].index[0]
        distances=sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
        recommended_movies_name=[]
        recommended_movies_poster=[]
        for i in distances[1:11]:
            movie_id=movies.iloc[i[0]].movie_id
            # recommended_movies_poster.append(fetch_poster(movie_id))
            recommended_movies_name.append(movies.iloc[i[0]].title)
        return recommended_movies_name, recommended_movies_poster

    # load the model
    movies=pickle.load(open('artifacts/movie_list.pkl','rb'))

    similarity=pickle.load(open('artifacts/similarity.pkl','rb'))

    movie_list= movies['title'].values

    selected_movie=st.selectbox('Search for a movie', movie_list)
    
    col1, col2 = st.columns([2, 1])  # Adjust column widths as needed

    show_button = col1.button('Show recommendation')  # Use col1 for the button

    

    url = 'http://localhost:8501/login_page'
    col2.markdown(f'''
    <a href="{url}" target="_self"><button style="background-color:white;color:black">Back</button></a>
    ''', unsafe_allow_html=True)  # Use col2 for the button
    if show_button:
        recommended_movies_name, recommended_movies_poster=recommend(selected_movie)
        for i in range(0,10):
            st.markdown("{0}. {1}".format(i+1,recommended_movies_name[i]))
if __name__ == "__main__":
    home()
