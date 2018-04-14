from flask import Flask, request, json
from pychain import node, models
app = Flask(__name__)
node = node.Node()


@app.route('/')
def health_check():
    return "Node alive"


@app.route('/transactions', methods=['GET', 'POST'])
def handle_transactions():
    if request.method == "GET":
        return json.jsonify(node.mem_pool)
    if request.method == "POST":
        transaction_json = request.json["transaction"]
        new_transaction = models.Transaction(
            value=transaction_json["value"],
            receiver=transaction_json["receiver"],
            sender=transaction_json["sender"],
            signature=transaction_json["signature"]
        )
        node.accept_transaction(str(new_transaction))

        return f"Added transaction {new_transaction}"


@app.route("/blockchain")
def handle_blockchain():
    return json.jsonify([str(block) for block in node.blockchain])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')