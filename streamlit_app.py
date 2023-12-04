import streamlit as st
import pandas as pd

def hr_data_frame():
    # Initialize connection.
    conn = st.connection("snowflake")
    session = conn.session()
    
hr_data_frame()


