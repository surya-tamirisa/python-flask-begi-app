from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = []

@app.route('/')
def home():
    return "Welcome to the Personal Expense Tracker API!"

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses), 200

@app.route('/expense', methods=['POST'])
def add_expense():
    required_keys = ['amount', 'category', 'date', 'description']
    missing_keys = []
    data = request.get_json()
    for key in required_keys:
        if key not in data:
            missing_keys.append(key)
    if missing_keys:
        return jsonify({"error": f"Missing keys: {', '.join(missing_keys)}"}), 400

    expenses.append(data)
    return jsonify({"message": "expense added Successfully!", "expense": data}), 201


@app.route('/easteregg')
def winter():
    return "<h1>Winter is coming</h1>"

if __name__ == "__main__":
    app.run(debug=True)