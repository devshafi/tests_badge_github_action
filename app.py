"""
Simple Flask application with calculator endpoints.
"""
from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide, power

app = Flask(__name__)


@app.route('/')
def home():
    """Home page with API documentation."""
    return {
        "message": "Simple Calculator API",
        "endpoints": {
            "/add": "POST with 'a' and 'b' parameters",
            "/subtract": "POST with 'a' and 'b' parameters",
            "/multiply": "POST with 'a' and 'b' parameters",
            "/divide": "POST with 'a' and 'b' parameters",
            "/power": "POST with 'a' and 'b' parameters"
        }
    }


@app.route('/add', methods=['POST'])
def add_endpoint():
    """Add two numbers."""
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return {"error": "Missing parameters 'a' and 'b'"}, 400
    
    try:
        result = add(float(data['a']), float(data['b']))
        return {"result": result}
    except (ValueError, TypeError):
        return {"error": "Invalid number format"}, 400


@app.route('/subtract', methods=['POST'])
def subtract_endpoint():
    """Subtract two numbers."""
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return {"error": "Missing parameters 'a' and 'b'"}, 400
    
    try:
        result = subtract(float(data['a']), float(data['b']))
        return {"result": result}
    except (ValueError, TypeError):
        return {"error": "Invalid number format"}, 400


@app.route('/multiply', methods=['POST'])
def multiply_endpoint():
    """Multiply two numbers."""
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return {"error": "Missing parameters 'a' and 'b'"}, 400
    
    try:
        result = multiply(float(data['a']), float(data['b']))
        return {"result": result}
    except (ValueError, TypeError):
        return {"error": "Invalid number format"}, 400


@app.route('/divide', methods=['POST'])
def divide_endpoint():
    """Divide two numbers."""
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return {"error": "Missing parameters 'a' and 'b'"}, 400
    
    try:
        result = divide(float(data['a']), float(data['b']))
        return {"result": result}
    except (ValueError, TypeError):
        return {"error": "Invalid number format"}, 400
    except ValueError as e:
        return {"error": str(e)}, 400


@app.route('/power', methods=['POST'])
def power_endpoint():
    """Raise first number to the power of second number."""
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return {"error": "Missing parameters 'a' and 'b'"}, 400
    
    try:
        result = power(float(data['a']), float(data['b']))
        return {"result": result}
    except (ValueError, TypeError):
        return {"error": "Invalid number format"}, 400


if __name__ == '__main__':
    app.run(debug=True)