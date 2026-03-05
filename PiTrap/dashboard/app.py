from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {
        "attacks": 42,
        "top_ip": "192.168.1.25",
        "latest_attack": "SSH brute force"
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)