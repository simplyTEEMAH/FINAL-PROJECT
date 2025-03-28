from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient

# initialise the flask app
app= Flask("__name__")

# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client['users_database']  # Database name
collection = db['user']  # Collection name

# Route for displaying the form
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route("/submit", methods=["POST"])
def submit():      
        age=request.form["age"]
        gender=request.form["gender"]
        total_income=request.form["total_income"]
        # initialise the expense data

        expenses={}

        # store the amoutn spent for each expense category when selected
        if "utilities" in request.form:
            expenses["utilities"] = request.form.get("utilities_amount", 0)
        if "entertainment" in request.form:
            expenses["entertainment"] = request.form.get("entertainment_amount", 0)
        if "school_fees" in request.form:
            expenses["school_fees"] = request.form.get("school_fees_amount", 0)
        if "shopping" in request.form:
            expenses["shopping"] = request.form.get("shopping_amount", 0)
        if "healthcare" in request.form:
            expenses["healthcare"] = request.form.get("healthcare_amount", 0)

        return f'Thank you {name},! We received your details.'

        user_data={
            "age":age,
            "gender":gender,
            "total_income":total_income,
            "expenses":expenses
        }

            # Insert the user data into MongoDB Collection
        collection.insert_one(user_data)

        # Redirect to a thank you page after successful submission
        return redirect(url_for('thank_you'))

if __name__=="__main__":
    app.run(debug=True, port=5000)
