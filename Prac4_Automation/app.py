from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = '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'  # Replace with your API key

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data['message']
    
    # Use OpenAI GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return jsonify({"response": response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(debug=True)
