# define a class named User with all the required attributes
class User:
    def __init__ (self, age, gender, total_income):
        self.age = age
        self.gender = gender
        self.total_income = total_income
    # Use dictionary to define the various expense categories
        self.expenses = {
            "Utilities": 0,
            "Entertainment": 0,
            "School Fees": 0,
            "Shopping": 0,
            "Healthcare": 0,
        }
    #update the amount for each expense category
    def update_expenses(self, category, amount):
        if category in self.expenses:
            self.expenses[category] = amount
        else:
            print(f"Category '{category}' does not exist")
   # calculate the total expenses from each expense category 
    def get_total_expenses(self):
        return sum(self.expenses.values())
    
    def display_user_info(self):
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Total Income: {self.total_income}")

        print("Expenses")
        for category, amount in self.expenses.items():
            print(f"{category}: {amount}")

        print(f"Total Expenses: {self.get_total_expenses()}")

# loop through collected data and store in a csv file

import pandas as pd
import random

# define a function to return the user's information using dictionary
def to_data_dict(self):
        user_data = {
            "Age": self.age,
            "Gender": self.gender,
            "Total_Income": self.total_income,
        }
# add the expenses data
        for category, amount in self.expenses.values ():
            user_data[category] = amount
        
        return user_data

# create 10 users randomly and update expenses
genders = ["female", "male"]
users = []

for i in range (10):
    age = random.randint(30, 55)
    gender = random.choice (genders)
    total_income = random.randint(55000, 300000)

# create a new user instance
user = User(age=age, gender=gender, total_income=total_income)

# Update expenses randomly
categories = ["utilities", "entertainment", "schoolfees", "shopping", "healthcare"]
for category in categories:
    user.update_expenses(category, random.randint(5000, 55000)) # Assign random expense amounts for each category

#add users to the list
users.append(user)

for user in users:
    user.display_user_info()

# Create a list of dictionaries for CSV
user_data_list = [user.to_data_dict() for user in users]

# Convert to DataFrame and save to CSV
df = pd.DataFrame(user_data_list)
df.to_csv("user_data.csv", index=False)

print("User data has been saved to 'user_data.csv'.")