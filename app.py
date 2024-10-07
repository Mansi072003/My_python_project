from flask import Flask, render_template, request, jsonify
from gensim.summarization import summarize, keywords

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['input_text']
    word_limit = int(request.form['word_limit'])
    summary = summarize(text, word_count=word_limit)
    return summary

@app.route('/keywords', methods=['POST'])
def extract_keywords():
    text = request.form['input_text']
    extracted_keywords = keywords(text).split('\n')
    return jsonify({'keywords': extracted_keywords})

if __name__ == '__main__':
    app.run(debug=True)
