import streamlit as st
from pages import globals


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
""", unsafe_allow_html=True,)

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
        .btn1 {
            background-color: #ffffff;
            color: #000000;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px 20px;
            text-decoration: none;
            transition: all 0.3s ease;
            margin-left:220px;
        }
        .btn1:hover {
            background-color: #008080;
            color: #ffffff;
            text-decoration: none;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
        
                <a href="http://localhost:8501/register_page" target='_self' class="btn">New User?? Register Here</a>
        
        """, unsafe_allow_html=True
)

def login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    login_button_clicked = st.button("Login")
    url = 'http://localhost:8501/register_page'



    if login_button_clicked:
        # Establish database connection
        conn = st.connection('mysql', type='sql')

        # Perform query
        query = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}';"
        df = conn.query(query, ttl=600)

        # Check if any rows are returned
        if not df.empty:
            email1 = df.iloc[0].email
            password1 = df.iloc[0].password

            # Authentication logic
            if email == email1 and password == password1:
                st.success("Login successful!")
                globals.set_user(email)

                

                st.markdown(
                    """
                        
                                <a href="http://localhost:8501/home_page" target='_self' class="btn1">Continue to Movie Recommender</a>
                        
                        """, unsafe_allow_html=True
                )
            else:
                st.error("Invalid email or password. Please try again.")
        else:
            st.error("User not found. Please register first.")


if __name__ == "__main__":
    # if globals.get_user()==None:
    #     login()
    # else:
    #     home()
    login()
