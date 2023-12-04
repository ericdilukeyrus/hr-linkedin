import streamlit as st
import pandas as pd
import json
import time
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
        st.caption("Edit the LinkedIn contracts below")
        edited_data = st.data_editor(
            dataset,
            column_config={
            "CONTRACT": st.column_config.SelectboxColumn("Contrat",options=["LinkedIn-1 Years","LinkedIn-2 Years","LinkedIn-3 Years"]),
            "TITLE": st.column_config.Column("Title"),
            "RECRUITER_SEATLICENCE_NUMBER": st.column_config.NumberColumn("Recruiter Seatlicence #", width="small"),
            "RECRUITER_SEAT_LICENCE_PRICE": st.column_config.NumberColumn("Recruiter Seat licence price", width="small"),
            "DISCOUNT_RECRUITER_SEAT_PERCENT": st.column_config.NumberColumn("Discount Recruiter Seat %", width="small"),
            "JOB_SLOTS_NUMBER": st.column_config.NumberColumn("Job slots #"),
            "JOB_SLOTS_TOTAL_PRICE": st.column_config.NumberColumn("Job slots total price", width="small"),
            "JOB_SLOT_DISCOUNT_PERCENT": st.column_config.NumberColumn("Job Slot Discount %"),
            "CAREER_PAGE": st.column_config.NumberColumn("Career page"),
            "CAREER_PAGE_DISCOUNT_PERCENT": st.column_config.NumberColumn("Career Page discount %", width="small"),
            "START_DATE": st.column_config.DateColumn("Start date"),
            "END_DATE": st.column_config.DateColumn("End date"),
            "CONTRACT_END_DATE": st.column_config.DateColumn("Contract End Date"),
            "OWNER": st.column_config.Column("Owner"),
            "CONTRACT": st.column_config.Column("Contract"),
            "VALID_END_DATE": st.column_config.DateColumn("Valid End Date"),
            "VALID_CONTRACT_END_DATE": st.column_config.DateColumn("Valid Contract End Date"),
            "IS_VALID": st.column_config.Column("Is Valid"),
            "TEST": st.column_config.Column("Test")
        },
            use_container_width=True,
            num_rows="dynamic")
        submit_button = st.form_submit_button("Submit")

    #Date
    edited_data["START_DATE"] = edited_data["START_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["END_DATE"] = edited_data["END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["CONTRACT_END_DATE"] = edited_data["CONTRACT_END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["VALID_END_DATE"] = edited_data["VALID_END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["VALID_CONTRACT_END_DATE"] = edited_data["VALID_CONTRACT_END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")


    if submit_button:
        try:
            session.sql("TRUNCATE TABLE LINKEDINLICENSES_").collect() #Truncate table
            session.write_pandas(edited_data,"LINKEDINLICENSES_",overwrite=False)
            st.success("Table updated")
            time.sleep(5)
        except:
            st.warning("Error updating table")
        #st.rerun()

st.set_page_config(page_title="HR - Linkedin Licenses", layout="wide")


hr_data_frame()


