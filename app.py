from flask import Flask, render_template, request
import os
from utils.score_resume import evaluate_resume
import docx2txt
import fitz  

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        keywords = request.form['keywords'].split(',')

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        text = ''
        if file.filename.endswith('.pdf'):
            with fitz.open(filepath) as doc:
                for page in doc:
                    text += page.get_text()
        elif file.filename.endswith('.docx'):
            text = docx2txt.process(filepath)
        else:
            return "Unsupported file format."

        score, feedback = evaluate_resume(text, keywords)
        return render_template('index.html', score=score, feedback=feedback)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)