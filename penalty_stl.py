import streamlit as st
import pandas as pd
from openpyxl import *
import tkinter as tk
from tkinter import filedialog

st.title('PROCESSING DATA')
uploaded_file = st.file_uploader('Please select a XLSX file:',type="xlsx", accept_multiple_files=False)
if uploaded_file:
	df = pd.read_excel(uploaded_file)
	#st.dataframe(df)


# Set up tkinter
root = tk.Tk()
root.withdraw()


# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)


def open_savedfile():
	global path_out
	files = [('Excel file', '*.xlsx')]
	out_file = filedialog.asksaveasfile(master=root, filetypes = files, defaultextension = files)
	path_out=out_file.name
	return path_out

download=st.button('Download Excel File')
if download:
	open_savedfile()
	writer = pd.ExcelWriter(path_out, engine='xlsxwriter')
	df.to_excel(writer, sheet_name='welcome', index=False, startrow=3)
	writer.save()
	'Download Finished! Your file is in: '
	st.write(path_out)