import streamlit as st
import pandas as pd
import json
from snowflake.snowpark import Session

def hr_data_frame():

    #Initialize connection.
    if 's'
    with open('creds.json') as f:
        connection_param = json.load(f)
    ses = Session.builder.configs(connection_param).create()   
    st.write(ses.table("LINKEDINLICENSES_"))

hr_data_frame()


