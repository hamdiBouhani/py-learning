from flask import Flask, request, jsonify

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return "Welcome to my Web Server!"

# Endpoint with parameters
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# Endpoint handling query parameters
@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = int(request.args.get('num1', 0))
        num2 = int(request.args.get('num2', 0))
        result = num1 + num2
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid numbers provided'}), 400

# POST endpoint
@app.route('/postdata', methods=['POST'])
def postdata():
    data = request.json
    return jsonify({
        'received': data,
        'message': 'Data received successfully!'
    })

if __name__ == '__main__':
    app.run(debug=True)
