from flask import Flask,redirect

app = Flask(__name__)

#routes
@app.route("/")
def home():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == "__main__":
    app.run(host="0.0.0.0") 
