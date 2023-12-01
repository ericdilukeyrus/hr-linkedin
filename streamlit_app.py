import streamlit as st
import pandas as pd

def hr_data_frame():
    # Initialize connection.
    conn = st.connection("snowflake")
    session = conn.session()

    #@st.cache_data()
    def get_hr_data():
        df = session.table("LINKEDINLICENSES").to_pandas() #get all data from the table
        return  df

    df = get_hr_data() 
     
    edited_data = st.data_editor(
        df,
        column_config={
            "CONTRACT": st.column_config.SelectboxColumn("Contrat",options=["LinkedIn-1 Years","LinkedIn-2 Years","LinkedIn-3 Years"])
        },
        width=1200,
        use_container_width=True,
        num_rows="dynamic")
    
    table_name = 'LINKEDINLICENSES'
     # Button to submit changes
    if st.button('Submit Changes'):
        session.sql("TRUNCATE TABLE LINKEDINLICENSES").collect() #Truncate table
        conn.write_pandas(edited_data,table_name, overwrite=False)

hr_data_frame()


