from flask import Flask, render_template
from services.careers_service import get_careers

app = Flask(__name__)

@app.route("/")
def home():
    careers = get_careers()
    return render_template("index.html", careers=careers)

if __name__ == "__main__":
    app.run(debug=True)




