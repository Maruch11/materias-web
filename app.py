from flask import Flask, render_template
from services.careers_service import get_careers
from services.subjects_service import get_subjects_by_career

app = Flask(__name__)

@app.route("/")
def home():
    careers = get_careers()
    return render_template(
        "index.html", 
        careers=careers
    )

@app.route("/careers/<int:career_id>")
def career_detail(career_id):
    subjects = get_subjects_by_career(career_id)
    return render_template(
        "subjects.html",
        subjects=subjects,
        career_id=career_id
    )

if __name__ == "__main__":
    app.run(debug=True)




