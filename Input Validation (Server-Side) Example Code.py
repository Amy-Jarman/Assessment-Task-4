from flask import Flask, request, render_template, jsonify
import re
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    errors = {}

    name = request.form.get("name", "")
    email = request.form.get("email", "")
    dob = request.form.get("dob", "")
    
    # Validate name
    if not name or not re.match("^[a-zA-Z\s]+$", name): # Checks the input only uses letters and spaces
        errors["name"] = "Name must only contain letters and spaces"

    # Validate email
    if not email or not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email): # Checks input follows regular email format
        errors["email"] = "Invalid Email Address"
    
    # Validate date of birth
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d") # Makes input fit datetime format and checks date is not in the future.
        if dob_date >= datetime.now():
            errors["dob"] = "Date of Birth must be a past date"
    except ValueError:
        errors["dob"] = "Invalid Date of Birth" 
    
    if errors:
        return jsonify(errors), 400
    
    return jsonify({"message": "Form Submitted Successfully!"})


if __name__ == "__main__":
    app.run(debug=True)