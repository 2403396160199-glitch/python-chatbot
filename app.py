from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "your name" in message:
        return "I am a Python Chatbot."

    elif "how are you" in message:
        return "I am fine. Thanks for asking!"

    elif "bye" in message:
        return "Goodbye! Have a nice day."

    elif "python" in message:
        return "Python is a powerful programming language."

    else:
        return "Sorry, I don't understand that yet."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
