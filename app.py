from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

load_dotenv()
app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = os.environ.get('OPENAI_API_BASE')

@app.route('/query-openai', methods=['POST'])
def query_openai():
    try:
        data = request.get_json()
        user_input = data['user_input']

        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Choose the appropriate engine
            prompt=user_input,
            max_tokens=50  # Adjust the response length as needed
        )

        return jsonify({'response': response.choices[0].text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
