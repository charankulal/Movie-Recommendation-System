import streamlit as st
from sqlalchemy import create_engine, text

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
            margin-left:220px;
        }
        .btn:hover {
            background-color: #008080;
            color: #ffffff;
            text-decoration: none;
        }
        
    </style>
    """, unsafe_allow_html=True
    )

   


def register():
    st.title("Register")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    register_button_clicked = st.button("Register")
    url = 'http://localhost:8501/login_page'

    st.markdown(
        """
            
                    <a href="http://localhost:8501/login_page" target='_self' class="btn">Already registered? Login!!</a>
            
            """, unsafe_allow_html=True
    )

    if register_button_clicked:
        if password != confirm_password:
            st.error("Passwords do not match.")
        else:
            try:
                # Establish database connection
                engine = create_engine('mysql://root:Charan@localhost/mrs_user')
                conn = engine.connect()

                # Perform query to insert user data
                query = text(f"INSERT INTO users VALUES ('{name}', '{email}', '{password}','')")
                conn.execute(query)
                conn.commit()

                st.success("Registration successful. You can now log in.")
            except Exception as e:
                st.error(f"Registration unsuccessful: {str(e)}")
            finally:
                # Close the database connection
                conn.close()
                
            

if __name__ == "__main__":
    register()
