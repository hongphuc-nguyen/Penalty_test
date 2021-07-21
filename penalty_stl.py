import streamlit as st
import pandas as pd
from openpyxl import *
import os



st.title('PROCESSING DATA')
uploaded_file = st.file_uploader('Please select a XLSX file:',type="xlsx", accept_multiple_files=False)
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    path_out=os.getcwd()+r'\Penalty test.xlsx'


st.title('DOWNLOAD DATA')
download=st.button('Download Excel File')
if download:
    writer = pd.ExcelWriter(path_out, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False, startrow=3)
    writer.save()
    'Download Finished! Your file is in: '
    st.success("Download Finished! Your file is in: {0}".format(path_out))
