import streamlit as st
import pandas as pd
import json
from snowflake.snowpark import Session

def hr_data_frame():

    #Initialize connection.
    if 'snowflake_connection' not in st.session_state:
        #Connect to Snowflake
        with open('creds.json') as f:
            connection_param = json.load(f)
        st.session_state.snowflake_connection = Session.builder.configs(connection_param).create()   
        session = st.session_state.snowflake_connection
    else: 
        session = st.session_state.snowflake_connection
    
    def get_dataset():
        #Load table to df
        df = session.table("LINKEDINLICENSES_")
        return df

    dataset = get_dataset()
    #st.write(dataset)

    with st.form("data_editor_form"):
        st.caption("Edit the datafrae below")
        edited_data = st.data_editor(
            dataset,
            use_container_width=True,
            num_rows="dynamic")
        submit_button = st.form_submit_button("Submit")

hr_data_frame()


