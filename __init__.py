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
        width=1200,
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic")
    
    last_id = edited_data.loc[edited_data["ID"].idxmax()]["ID"]
    st.markdown(f"The last ID used is {last_id}")
  
    #Date
    edited_data["START_DATE"] = edited_data["START_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["END_DATE"] = edited_data["END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["CONTRACT_END_DATE"] = edited_data["CONTRACT_END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["VALID_END_DATE"] = edited_data["VALID_END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    edited_data["VALID_CONTRACT_END_DATE"] = edited_data["VALID_CONTRACT_END_DATE"].dt.strftime("%Y-%m-%d %H:%M:%S.%f")

    table_name = 'LINKEDINLICENSES'
     # Button to submit changes
    if st.button('Submit Changes'):
        session.sql("TRUNCATE TABLE LINKEDINLICENSES").collect() #Truncate table
        conn.write_pandas(edited_data,table_name, overwrite=False)
        #st.rerun()
    
st.set_page_config(layout="wide")
hr_data_frame()


