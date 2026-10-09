# STEP 1A
# Import SQL library and pandas (standard alias: pd)
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database file
conn = sqlite3.connect("data.sqlite")

# Reference code: view all employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Only employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Same columns, last name first
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Alias employeeNumber as ID
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# CASE bins job titles into Executive / Not Executive
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
                THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
# LENGTH() gives the character count of the last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# SUBSTR(text, start, length) -> first two letters of the job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# Reference code: view order details
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Round each line total first, then sum them all
total_prices = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""", conn)
# Wrap the total in a Series so sum_total_price[0] works on any pandas version
sum_total_price = pd.Series([total_prices["total_price"].sum()])

# STEP 9
# orderDate lives in the orders table (not orderDetails) as YYYY-MM-DD,
# so slice out day, month and year with SUBSTR
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)

# Close the connection
conn.close()