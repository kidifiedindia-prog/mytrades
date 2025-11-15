from flask import Flask, request
import os

# Create a basic Flask app
app = Flask(__name__)

# Simple home endpoint to check if backend is alive
@app.get("/")
def home():
    return "Backend is alive"

# This is where TradingView will send alerts later
@app.post("/tv-signal")
def tv_signal():
    # Raw body sent by TradingView alert
    body_text = request.data.decode("utf-8") if request.data else ""
    print("Received TradingView signal:", body_text)
    # For now just return OK
    return "OK"

# This part actually starts the web server on Render
if __name__ == "__main__":
    # Render provides the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    # Listen on all interfaces so Render can route traffic
    app.run(host="0.0.0.0", port=port)
