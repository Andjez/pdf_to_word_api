import streamlit as st
from flask import Flask, request, send_file
from pdf2docx import Converter
import os

app = Flask(__name__)

def pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

@app.route('/convert', methods=['POST'])
def convert_pdf_to_docx():
    pdf_path = request.form.get('pdf_path')
    docx_path = request.form.get('docx_path')

    pdf_to_docx(pdf_path, docx_path)

    return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    # Run Streamlit app in the background
    st_process = st._create_process('streamlit run --server.port 8501 Main_api.py', 'global')

    # Run Flask app
    app.run(port=5000, host='0.0.0.0')  # Allow external access

    # Close Streamlit app when Flask app exits
    st_process.terminate()
