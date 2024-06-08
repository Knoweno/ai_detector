from flask import Flask, request, render_template
import spacy
from docx import Document
import fitz  # PyMuPDF

app = Flask(__name__)

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze_file():
    uploaded_file = request.files['file']
    
    if uploaded_file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.filename.endswith('.docx'):
        text = extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file format. Please upload a PDF or Word document."

    ai_generated_content, total_text = analyze_text(text)
    ai_percentage = (len(ai_generated_content) / len(total_text)) * 100

    return render_template('result.html', ai_percentage=ai_percentage, ai_content=ai_generated_content)

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(file) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def analyze_text(text):
    doc = nlp(text)
    ai_generated_content = []
    total_text = []

    # Example of simple AI detection based on named entities
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            ai_generated_content.append(entity.text)
        total_text.append(entity.text)

    return ai_generated_content, total_text

if __name__ == '__main__':
    app.run(debug=True)
