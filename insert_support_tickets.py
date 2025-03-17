import pandas as pd
import mysql.connector

# Step 1: Read the categorized CSV file
data = pd.read_csv('support_tickets_categorized.csv')

# Step 2: Connect to Railway MySQL database
connection = mysql.connector.connect(
    host='ballast.proxy.rlwy.net',        # ballast.proxy.rlwy.net
    port=38663,                  # e.g., 38663
    user='root',
    password='JIOorQVZejOXBuPTfclVUiCwJEkJLZhW',
    database='support_ticket_analyzer'  # Use the new database name
)

cursor = connection.cursor()

# Step 3: Insert data into support_tickets table
for index, row in data.iterrows():
    sql = """
    INSERT INTO support_tickets (ticket_id, message, category)
    VALUES (%s, %s, %s)
    """
    values = (int(row['ticket_id']), row['message'], row['category'])
    cursor.execute(sql, values)

# Step 4: Commit and close connection
connection.commit()
cursor.close()
connection.close()

print("✅ Support tickets inserted successfully!")
