from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"

@app.route("/")
def home():
    return "Astra AI Backend Running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    reply = response["choices"][0]["message"]["content"]

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)