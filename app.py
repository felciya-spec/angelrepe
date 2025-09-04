from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    try:
        marks = float(request.form['marks'])
        grade = calculate_grade(marks)
        return render_template("index.html", marks=marks, grade=grade)
    except:
        return render_template("index.html", error="Invalid input! Please enter a number.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
