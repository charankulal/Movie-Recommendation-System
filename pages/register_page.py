import streamlit as st
from sqlalchemy import create_engine, text

def register():
    st.title("Register")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
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
