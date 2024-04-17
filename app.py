import streamlit as st

def main():
    # Custom CSS for hiding Streamlit sidebar
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none;
        }
        [data-testid="stSidebarContent"] {
            display: none;
        }
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True
    )

    # Set page title and center it
    
    st.markdown("<h1 style='text-align: center; color: #008080;'>Welcome to Movie Recommendation System</h1>", unsafe_allow_html=True)

    # Create a card with a background image
    st.markdown(
        """
        <style>
            .movie-card {
                background-image: url('https://images.unsplash.com/photo-1544022618-7d5f4db7b098');
                background-size: cover;
                background-position: center;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.5);
            }
            .card-content {
                color: #ffffff;
                text-align: center;
                padding: 20px;
            }
            .btn {
                background-color: #00ffff;
                color: #000000;
                border-radius: 5px;
                font-weight: bold;
                padding: 10px 20px;
                text-decoration: none;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background-color: #008080;
                color: #ffffff;
                text-decoration: none;
            }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Card content
    st.markdown(
        """
        <div class="movie-card">
            <div class="card-content">
                <h2 style='font-size: 24px;'>Join Us Now!</h2>
                <p>Unlock a world of movies tailored just for you.</p>
                <a href="http://localhost:8501/login_page" target='_self' class="btn">Login</a>
                <a href="http://localhost:8501/register_page" target='_self' class="btn">Register</a>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
