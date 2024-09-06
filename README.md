
## Instructions to set up the application and execute the application
# Data Visualization Application

## Setup Instructions

1. **Clone the Repository:**

   >> https://github.com/RohitKumar2511/dash-database-visualization.git
   
   >> cd dash-database-visualization 

3. Create a Virtual Environment: 

   >> python -m venv venv
   >> source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install Dependencies:

    >> pip install -r requirements.txt

5. Initialize the Database:

    >> python initialize_db.py

6. Run the Dash Application:

    >> python data_viz_app.py

7. Open the Application in Your Browser:

    >> Navigate to http://127.0.0.1:8050 to view the dashboard.


Description: 

This application connects to a local SQLite database, performs specific data queries, and visualizes the results using Dash.


This should cover setting up your environment, initializing the database, and running your Dash application.



## Testing and Validation for Your SQLite and Dash Project

>> When we are working on a project like this, we'd want to make sure it handles different scenarios smoothly. We have used some practicla approach for testing and validating, making sure the app doesn't crash when facing unusual or extremen cases.


1.1 Sometimes, we'll have users in the database who haven’t made any transactions yet. We’ll still want to show those users in reports without the app throwing errors.

Solution: We can use a LEFT JOIN in our SQL query to include users even if they haven’t made any transactions.

    >> SELECT u.user_id, u.name, u.email, IFNULL(SUM(t.amount), 0) AS total_spent
    FROM users u
    LEFT JOIN transactions t ON u.user_id = t.user_id
    GROUP BY u.user_id;

1.2 1.2 Empty Date Ranges

If a user selects an invalid or empty date range (like the start date is after the end date or no dates are selected), we need to catch this early to avoid running bad queries.

Solution: Add date validation in our Python code. 
    
    >> def validate_dates(start_date, end_date):
    if not start_date or not end_date:
        raise ValueError("Date range can't be empty.")
    if start_date > end_date:
        raise ValueError("Start date can't be after end date.")

1.3 Large Datasets  
    For SQLite, create an index like this: 
    
    >> CREATE INDEX idx_user_id ON transactions(user_id);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);


