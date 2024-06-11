# Flask Notes

Created: May 31, 2024 6:12 PM

## Quick Notes

## What is Flask?

Flask is a micro web framework for Python mainly used to to create APIs.

## Basic Example

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api', methods=['GET'])
def api():
    data = {"message": "Welcome to the API"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```