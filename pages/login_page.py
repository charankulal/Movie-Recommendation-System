import streamlit as st


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

def login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    

    login_button_clicked = st.button("Login")
    url = 'http://localhost:8501/register_page'

    st.markdown(f'''
    <a href={url} target="_self"><button style="background-color:white;color:black">Are New User?? Register</button></a>
    ''',
    unsafe_allow_html=True)

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
                # Provide link to the home page
                
                url = 'http://localhost:8501/home_page'

                st.markdown(f'''
                <a href={url} target="_self"><button style="background-color:white;color:black">Home Page</button></a>
                ''',
                unsafe_allow_html=True)
            else:
                st.error("Invalid email or password. Please try again.")
        else:
            st.error("User not found. Please register first.")

if __name__ == "__main__":
    login()
