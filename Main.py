import streamlit as st
from pdf2docx import Converter
import pikepdf
import os

#def pdf_to_docx(pdf_path, docx_path):
#    cv = Converter(pdf_path)
#    cv.convert(docx_path, start=0, end=None)
#    cv.close()


def pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    total_pages = cv.num_pages
    progress_bar = st.progress(0)

    for page_num in range(total_pages):
        # Convert each page
        cv.convert(docx_path, start=page_num, end=page_num + 1)

        # Update progress bar
        progress_bar.progress((page_num + 1) / total_pages)

    cv.close()
# Function to create a download link for files
def get_binary_file_downloader_html(file_path, file_label='File'):
    with open(file_path, 'rb') as file:
        data = file.read()
    bin_str = data
    bin_str = bin_str.decode('latin1')
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}.docx">Download {file_label}</a>'
    return href
    
# Streamlit UI
st.title("PDF to Word Converter")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Display PDF
    bytes_data = uploaded_file.read()
    pdf = pikepdf.open(uploaded_file)
    pdf.save(uploaded_file.name)
    filename = uploaded_file.name
    #st.subheader("Uploaded PDF Preview:")
    #st.pdf(filename)

    # Convert PDF to Word
    convert_button = st.button("Convert to Word")

    if convert_button:
        # Temporary path for converted Word file
        temp_docx_path = "converted_docx.docx"
        pdf_to_docx(filename, temp_docx_path)

        # Display download button
        st.subheader("Download Converted Word File:")
        st.markdown(get_binary_file_downloader_html("converted_docx.docx", "Word file"), unsafe_allow_html=True)

        # Remove temporary Word file after download
        os.remove(temp_docx_path)
