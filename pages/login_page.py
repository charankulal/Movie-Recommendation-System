import streamlit as st
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",unsafe_allow_html=True,)

def login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    

    login_button_clicked = st.button("Login")
    st.link_button("New user? Register","http://localhost:8501/register_page")

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
                st.markdown("[Visit Home Page](http://localhost:8501/home_page)")
            else:
                st.error("Invalid email or password. Please try again.")
        else:
            st.error("User not found. Please register first.")

if __name__ == "__main__":
    login()
