# main_api.py

from flask import Flask, request, send_file
from pdf2docx import Converter
import os
import subprocess

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
    # Start the Streamlit app as a separate process
    streamlit_command = 'streamlit run Main_api.py'
    subprocess.Popen(streamlit_command, shell=True)

    # Run the Flask app
    app.run(port=5000, host='0.0.0.0')
