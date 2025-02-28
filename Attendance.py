import streamlit as st
import sqlite3
# Attendance.py
import AttendanceDB

# Create the database and table on import
AttendanceDB.create_database()

# Streamlit settings
st.set_page_config(
    page_title="Attendance",
    page_icon="📅",
    layout="wide"
)