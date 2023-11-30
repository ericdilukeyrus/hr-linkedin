import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
#df = conn.query("SELECT * from LINKEDINLICENSES;", ttl=600)

# Load the table as a dataframe usng the Snowpark session.
#@st.cache_data
session  =conn.session()
df = session.table("LINKEDINLICENSES")


# Display data in an editable table

edited_data = st.data_editor(
    df,    
    num_rows="dynamic",
    column_config={
        "TITLE": st.column_config.Column("Title"),
        "RECRUITER_SEATLICENCE_NUMBER": st.column_config.Column("Recruiter Seatlicence #", width="small"),
        "RECRUITER_SEAT_LICENCE_PRICE": st.column_config.Column("Recruiter Seat licence price"),
        "DISCOUNT_RECRUITER_SEAT_PERCENT": st.column_config.Column("Discount Recruiter Seat %"),
        "JOB_SLOTS_NUMBER": st.column_config.Column("Job slots #"),
        "JOB_SLOTS_TOTAL_PRICE": st.column_config.Column("Job slots total price"),
        "JOB_SLOT_DISCOUNT_PERCENT": st.column_config.Column("Job Slot Discount %"),
        "CAREER_PAGE": st.column_config.Column("Career page"),
        "CAREER_PAGE_DISCOUNT_PERCENT": st.column_config.Column("Career Page discount %"),
        "START_DATE": st.column_config.Column("	Start date"),
        "END_DATE": st.column_config.Column("End date"),
        "CONTRACT_END_DATE": st.column_config.Column("Contract End Date"),
        "OWNER": st.column_config.Column("Owner"),
        "CONTRACT": st.column_config.Column("Contract"),
        "VALID_END_DATE": st.column_config.Column("Valid End Date"),
        "VALID_CONTRACT_END_DATE": st.column_config.Column("Valid Contract End Date"),
        "IS_VALID": st.column_config.Column("Is Valid"),
        "TEST": st.column_config.Column("Test")
    },
    hide_index=True
)


table_name = 'LINKEDINLICENSES'
# Button to submit changes
if st.button('Submit Changes'):
    #session.sql("TRUNCATE TABLE LINKEDINLICENSES").collect() #Truncate table
    conn.write_pandas(edited_data,table_name, auto_create_table=True, overwrite=True)
    
    


