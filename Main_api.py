# main_api.py

from flask import Flask, request, send_file
import threading
import os
from pdf2docx import Converter

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
    # Run Flask app in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'port': 5000, 'host': '0.0.0.0'})
    flask_thread.start()

    # Run Streamlit app in the main thread
    os.system('streamlit run Main_api.py')

    # Wait for Flask thread to finish
    flask_thread.join()
