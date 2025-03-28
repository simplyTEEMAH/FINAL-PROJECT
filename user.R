# Define the expense category class
ExpenseCategory <- setRefClass(
    "ExpenseCategory",
    fields = list(
        name="character", amount="numeric"
    ),

    methods = list (
        initialize = function(name) {
            name <<- name
            amount <<- 0
        },
        update_amount = function (amount) {
            amount <<- amount
        },
        display = function () {
            cat (paste(name, ":", amount, "/n"))
        }
    )
)
# Define the user class
User <- setRefClass(
    "User", 
    fields = list (
        age="numeric",
        gender = "character",
        total_income="numeric",
        expenses = "list"
    ),
    methods = list (
        initialize = function (age, gender, total_income){
            age <<- age
            gender <<- gender
            total_income <<- total_income
            # Using the Expense Category, initialise the various expense categories
            expenses <<- list(
                Utilities = ExpenseCategory$new (name="Utilities"),
                Entertainment = ExpenseCategory$new (name="Entertainment"),
                SchoolFees = ExpenseCategory$new (name="SchoolFees"),
                Shopping = ExpenseCategory$new (name="Shopping"),
                HealthCare = ExpenseCategory$new (name="HealthCare")
            )     
        },
        update_expenses = function (category, amount) { #update each expense category
            if (category %in%names(expenses)){
                expenses[[category]] $update_amount (amount)
            } else {
                cat ("Category", Category, "does not exist.\n")
            }
        },
        get_total_expenses = function () { # get the total expenses
            total <- 0
            for (expense in expenses) {
                total <- total + expense$amount
            }
            return (total)
        },
        display_user_info = function () { #display the user information for all parameters
            cat ("Age:", age, "/n")
            cat ("Gender:", gender, "/n")
            cat ("Total_Income:", total_income, "/n")
            cat ("Expenses:/n")
        # display all the expense categories
        for (expense in expenses) {
            expense$display()
        }
        # display the total expenses
        cat ("Total Expenses:", get_total_expenses(), "/n")
        },
        # convert user information and expenses to a dataframe for CSV output
        to_data_frame = function () {
            user_info <- data.frame (
                Age=age,
                Gender=gender,
                Total_Income=total_income
            )
        # extract the expenses as a dataframe
        expense_data <- data.frame (
            Category = names (expenses),
            Amount = sapply (expenses, function(expenses) expenses$amount)
        )
        # Merge user information with expenses
        user_expenses <- cbind(user_info, expense_data)
        return(user_expenses)
        }

    )     
)
# Create 10 random users
generate_random_users <- function(n) {
  genders <- c("female", "male")
  users <- list()

  for (i in 1:n) {
    age <- sample(30:55, 1)  # Random age between 30 and 55
    gender <- sample(genders, 1)  # Random gender
    total_income <- sample(55000:300000, 1)  # Random total income between 55k and 300k

# Create a new user instance
    user <- User$new(age = age, gender = gender, total_income = total_income)

# Update expenses randomly
    categories <- c("Utilities", "Entertainment", "SchoolFees", "Shopping", "HealthCare")
    for (category in categories) {
      amount <- sample(5000:55000, 1)  # Random expense amount between 5000 and 55000
      user$update_expenses(category, amount)
    }
# add user to the list
users[[i]] <- user
  }
  return (users)
}
# Generate 10 random users list
users_list <- generate_random_users(10)

# Display the user list
for (user in users_list) {
  user$display_user_info()
  cat("\n")  # Add a newline for better readability between users
}

# Convert user data to a data frame
user_data_list <- do.call(rbind, lapply(users_list, function(user) user$to_data_frame()))

# Write the user data to a CSV file
write.csv(user_data_list, "user_data.csv", row.names = FALSE)
cat("User data has been saved to user_data.csv\n")