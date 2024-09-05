import dash
from dash import html, dcc
from dash import dash_table
from dash.dash_table.Format import Group
# import dash_core_components as dcc
# import dash_html_components as html
# from dash_table import DataTable
import pandas as pd
import plotly.express as px
import sqlite3

app = dash.Dash(__name__)

def open_db_connection():
    return sqlite3.connect('example.db')

def get_users_by_date_range(start_date, end_date):
    with open_db_connection() as conn:
        query = '''
            SELECT * FROM users
            WHERE join_date BETWEEN ? AND ?
        '''
        df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    return df

def get_user_spending():
    with open_db_connection() as conn:
        query = '''
            SELECT user_id, SUM(amount) as total_spent
            FROM transactions
            GROUP BY user_id
        '''
        df = pd.read_sql_query(query, conn)
    return df

def get_user_spending_report():
    with open_db_connection() as conn:
        query = '''
            SELECT u.name, u.email, COALESCE(SUM(t.amount), 0) as total_spent
            FROM users u
            LEFT JOIN transactions t ON u.user_id = t.user_id
            GROUP BY u.user_id
        '''
        df = pd.read_sql_query(query, conn)
    return df

def top_users_by_expenditure():
    spending_df = get_user_spending()
    top_users = spending_df.nlargest(3, 'total_spent')
    return top_users

def avg_spending_per_transaction():
    with open_db_connection() as conn:
        query = '''
            SELECT AVG(amount) as avg_amount
            FROM transactions
        '''
        df = pd.read_sql_query(query, conn)
    return df['avg_amount'].values[0]

def users_with_zero_spending():
    user_report_df = get_user_spending_report()
    no_spending = user_report_df[user_report_df['total_spent'] == 0]
    return no_spending

def transaction_amounts_over_time():
    with open_db_connection() as conn:
        query = '''
            SELECT transaction_date, amount
            FROM transactions
        '''
        df = pd.read_sql_query(query, conn)
    return df

app.layout = html.Div([
    html.H1("Comprehensive Data Dashboard"),

    html.Div([
        html.H2("Expenditure of Top 3 Users"),
        dcc.Graph(
            id='top-users-bar-chart',
            figure=px.bar(
                top_users_by_expenditure(),
                x='user_id',
                y='total_spent',
                title="Top 3 Users by Total Spending",
                labels={'user_id': 'User ID', 'total_spent': 'Total Spent'}
            )
        )
    ]),

    html.Div([
        html.H2("Transaction Trends Over Time"),
        dcc.Graph(
            id='transaction-trends-line-chart',
            figure=px.line(
                transaction_amounts_over_time(),
                x='transaction_date',
                y='amount',
                title="Transaction Trends Over Time",
                markers=True
            )
        )
    ]),

    html.Div([
        html.H2("Detailed User Spending Report"),
        dash_table.DataTable(
            id='user-spending-table',
            columns=[
                {'name': 'Name', 'id': 'name'},
                {'name': 'Email', 'id': 'email'},
                {'name': 'Total Spent', 'id': 'total_spent'},
                {'name': 'Average Transaction', 'id': 'avg_transaction'}
            ],
            data=get_user_spending_report().to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
        )
    ]),

    html.Div([
        html.H2("Users with No Recorded Transactions"),
        dash_table.DataTable(
            id='no-transactions-table',
            columns=[
                {'name': 'Name', 'id': 'name'},
                {'name': 'Email', 'id': 'email'}
            ],
            data=users_with_zero_spending().to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
