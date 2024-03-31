import streamlit as st
from pages.register_page import register
from pages.login_page import login
from pages.home_page import home


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

login()



    
  
    