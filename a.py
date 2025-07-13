import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Authenticate using secrets.toml ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)

# --- Your private Google Sheet ID ---
SHEET_ID = "1RexcfpskciE8VCWAiyx7db9LC6PCKOMZl__oy3Niw68"
sheet = client.open_by_key(SHEET_ID).sheet1  # Default first worksheet

# --- Get data
data = sheet.get_all_values()
letter = data[0][0] if data else "No data found"

# --- Display
st.title("🔤 Display Letter from Private Sheet")
st.success(f"Letter in cell A1: {letter}")
