import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect('example.db')

def fetch_users_by_date(start_date, end_date):
    with get_connection() as conn:
        sql = '''
            SELECT * FROM users
            WHERE join_date BETWEEN ? AND ?
        '''
        df = pd.read_sql_query(sql, conn, params=(start_date, end_date))
    return df

def fetch_spending_summary():
    with get_connection() as conn:
        sql = '''
            SELECT user_id, SUM(amount) as total_spent
            FROM transactions
            GROUP BY user_id
        '''
        df = pd.read_sql_query(sql, conn)
    return df

def fetch_user_spending_report():
    with get_connection() as conn:
        sql = '''
            SELECT u.name, u.email, COALESCE(SUM(t.amount), 0) as total_spent
            FROM users u
            LEFT JOIN transactions t ON u.user_id = t.user_id
            GROUP BY u.user_id
        '''
        df = pd.read_sql_query(sql, conn)
    return df

def top_spenders():
    spending_df = fetch_spending_summary()
    top_users = spending_df.nlargest(3, 'total_spent')
    return top_users

def average_transaction_amount():
    with get_connection() as conn:
        sql = '''
            SELECT AVG(amount) as avg_amount
            FROM transactions
        '''
        df = pd.read_sql_query(sql, conn)
    return df['avg_amount'].values[0]

def users_with_no_transactions():
    spending_df = fetch_user_spending_report()
    no_transactions = spending_df[spending_df['total_spent'] == 0]
    return no_transactions

if __name__ == "__main__":
    print("Users who joined between '2023-01-01' and '2023-06-30':")
    print(fetch_users_by_date('2023-01-01', '2023-06-30'))

    print("\nTotal amount spent by each user:")
    print(fetch_spending_summary())

    print("\nUser spending report (name, email, total spent):")
    print(fetch_user_spending_report())

    print("\nTop 3 users who spent the most:")
    print(top_spenders())

    print("\nAverage transaction amount:")
    print(average_transaction_amount())

    print("\nUsers with no transactions:")
    print(users_with_no_transactions())
