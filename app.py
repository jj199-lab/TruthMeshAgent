from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/agent", methods=["POST"])
def agent():
    user_input = request.json.get("message", "")
    response = f"TruthMeshAgent received: {user_input}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
