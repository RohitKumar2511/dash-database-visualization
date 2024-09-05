
## Instructions to set up the application and execute the application
# Data Visualization Application

## Setup Instructions

1. **Clone the Repository:**
   https://github.com/RohitKumar2511/dash-database-visualization.git
   cd dash-database-visualization 

2. Create a virtual Environment: 

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies:

    pip install -r requirements.txt

4. Initialize the Database:

    python initialize_db.py

5. Run the Dash Application:

    python data_viz_app.py

6. Open the Application in Your Browser:

    Navigate to http://127.0.0.1:8050 to view the dashboard.


Description: 

This application connects to a local SQLite database, performs specific data queries, and visualizes the results using Dash.


This should cover setting up your environment, initializing the database, and running your Dash application.
