from openai import OpenAI

client = OpenAI()
MODEL_NAME = "gpt-4o"

# Function to ask OpenAI for a SQL query based on a question and schema
def ask_openai(query, schema):
    prompt = f"""Here is the schema for a database:

{schema}

Given this schema, can you output a SQL query to answer the following question? 
Only output the SQL query and nothing else.

Question: {query}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2048
    )
    return response.choices[0].message.content

# Connect to the SQLite database
import sqlite3
connection = sqlite3.connect("my.db")
cursor = connection.cursor()

# Get the database schema
schema = cursor.execute("PRAGMA table_info(employees)").fetchall()
schema_str = "CREATE TABLE EMPLOYEES (\n" + "\n".join([f"{col[1]} {col[2]}" for col in schema]) + "\n)"
print("===== Database Schema =====")
print(schema_str)

# Example natural language question
question = "List all employees in the Sales department with a salary greater than 55000."
# Send the question to OpenAI and get the SQL query
sql_query = ask_openai(question, schema_str)
print("\n===== Generated SQL Query =====")
print(sql_query)

# remove the comment from the SQL query
sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

# Execute the query and show results
print("\n===== Executing SQL Query =====")
try:
    results = cursor.execute(sql_query).fetchall()
    print("\nQuery Results:")
    for row in results:
        print(row)
except sqlite3.Error as e:
    print("Error executing query:", e)

connection.close()
