from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Define the URL of the external API endpoint
API_URL = 'http://127.0.0.1:5000/system-analytics-raw'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    try:
        # Make a GET request to the external API endpoint
        response = requests.get(API_URL)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            return data
        else:
            return jsonify({'error': 'Failed to fetch data from the API'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run the Flask app on port 8000
    app.run(port=8000, debug=True)
