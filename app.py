from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    # Get the JSON data from the request
    data = request.json.get('data', [])

    # Initialize arrays for numbers and alphabets
    numbers = []
    alphabets = []
    highest_lowercase = None

    # Iterate over the data and separate numbers and alphabets
    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            # Check if the alphabet is lowercase and update the highest lowercase alphabet
            if item.islower() and (highest_lowercase is None or item > highest_lowercase):
                highest_lowercase = item

    # Prepare the response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    # Return the operation_code as requested
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
