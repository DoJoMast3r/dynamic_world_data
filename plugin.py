from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, static_folder="ui", template_folder="ui")

# Load stop words from file
with open('stopwords.txt', 'r') as file:
    stop_words = set(file.read().splitlines())

def clean_message(text):
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(cleaned_words)

def search_world_info(cleaned_text):
    # This function should interact with your world info data
    # Here we return a dummy response for demonstration
    # Replace this with actual search logic
    keywords = cleaned_text.split()
    relevant_data = " ".join([f"info_about_{keyword}" for keyword in keywords])
    return relevant_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_message', methods=['POST'])
def process_message():
    data = request.json
    text = data.get('text', '')
    cleaned_text = clean_message(text)
    world_info = search_world_info(cleaned_text)
    updated_message = f"{text} {world_info}"
    return jsonify({
        'original_message': text,
        'cleaned_message': cleaned_text,
        'world_info': world_info,
        'updated_message': updated_message
    })

if __name__ == '__main__':
    app.run(port=5000)
