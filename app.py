from flask import Flask, render_template, request

app = Flask(__name__)


career_skills = {

    "Cyber Security": [
        "Networking",
        "Linux",
        "Python",
        "Cyber Security Basics",
        "Cryptography",
        "Ethical Hacking"
    ],

    "Data Scientist": [
        "Python",
        "Statistics",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "Git",
        "React",
        "Backend Development"
    ],

    "Game Developer": [
        "C++",
        "Data Structures",
        "Game Physics",
        "Unity",
        "3D Mathematics",
        "Game Design"
    ],

    "AI Developer": [
        "Python",
        "Statistics",
        "NumPy",
        "Machine Learning",
        "Deep Learning",
        "Neural Networks"
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        career = request.form["career"]

        skills = career_skills[career]

        return render_template(
            "skills.html",
            career=career,
            skills=skills
        )

    return render_template(
        "skills.html",
        career=None
    )


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/analyse", methods=["POST"])
def analyse():

    career = request.form["career"]

    selected_skills = request.form.getlist("skills")

    required_skills = career_skills[career]

    missing_skills = []

    for skill in required_skills:

        if skill not in selected_skills:
            missing_skills.append(skill)

    return render_template(
        "result.html",
        career=career,
        selected_skills=selected_skills,
        missing_skills=missing_skills
    )

from flask import Flask, render_template, request

app = Flask(__name__)


career_skills = {

    "Cyber Security": [
        "Networking",
        "Linux",
        "Python",
        "Cyber Security Basics",
        "Cryptography",
        "Ethical Hacking"
    ],

    "Data Scientist": [
        "Python",
        "Statistics",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "Git",
        "React",
        "Backend Development"
    ],

    "Game Developer": [
        "C++",
        "Data Structures",
        "Game Physics",
        "Unity",
        "3D Mathematics",
        "Game Design"
    ],

    "AI Developer": [
        "Python",
        "Statistics",
        "NumPy",
        "Machine Learning",
        "Deep Learning",
        "Neural Networks"
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        career = request.form["career"]

        skills = career_skills[career]

        return render_template(
            "skills.html",
            career=career,
            skills=skills
        )

    return render_template(
        "skills.html",
        career=None
    )


@app.route("/analyse", methods=["POST"])
def analyse():

    career = request.form["career"]

    selected_skills = request.form.getlist("skills")

    required_skills = career_skills[career]

    missing_skills = []

    for skill in required_skills:

        if skill not in selected_skills:
            missing_skills.append(skill)

    return render_template(
        "result.html",
        career=career,
        selected_skills=selected_skills,
        missing_skills=missing_skills
    )


if __name__ == "__main__":
    app.run(debug=True)