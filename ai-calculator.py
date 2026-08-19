from flask import Flask, render_template, request, jsonify
import math

# Create Flask application
app = Flask(__name__)

# Calculator functions
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b
def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def square_root(a):
    """Calculate square root of a number"""
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(a)

# Main page route
@app.route('/')
def home():
    """Display the calculator homepage"""
    return render_template('index.html')

# Calculate route - handles calculation requests
@app.route('/calculate', methods=['POST'])
def calculate():
    """Process calculation requests from the frontend"""
    try:
        data = request.json
        operation = data.get('operation')
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        
        # Perform the requested operation
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'sqrt':
            result = square_root(num1)
        else:
            result = "Error: Invalid operation"
        
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'})

# Run the application
if __name__ == '__main__':
    print("Starting Calculator App...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)